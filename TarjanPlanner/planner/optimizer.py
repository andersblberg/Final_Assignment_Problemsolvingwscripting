def calculate_edge_weights(graph, transport_modes):
    """Calculate time and cost for all edges in the graph with adjusted cost scaling."""
    all_times = []
    all_costs = []

    # First pass: calculate times and costs, collect for scaling
    for u, v, data in graph.edges(data=True):
        distance = data["distance"]
        data["modes"] = []

        for mode in transport_modes:
            travel_time = (distance / mode["speed_kmh"]) * 60 + mode["transfer_time_min"]
            travel_cost = distance * mode["cost_per_km"]

            data["modes"].append({
                "mode": mode["mode"],
                "time": travel_time,
                "cost": travel_cost
            })
            all_times.append(travel_time)
            all_costs.append(travel_cost)

    # Compute mean values for scaling
    mean_time = sum(all_times) / len(all_times)
    mean_cost = sum(all_costs) / len(all_costs) if sum(all_costs) > 0 else 1  # Avoid division by zero

    # Set adjustment factor to increase cost influence
    adjustment_factor = 0.15 # You can experiment with this value

    # Compute scaling factor with adjustment
    scaling_factor = (mean_time / mean_cost) * adjustment_factor

    # Second pass: calculate combined scores using adjusted cost
    epsilon = 0.01  # Small constant to prevent zero cost
    for u, v, data in graph.edges(data=True):
        best_time = min(data["modes"], key=lambda x: x["time"])
        best_cost = min(data["modes"], key=lambda x: x["cost"])
        best_combined = None
        min_combined_score = float("inf")

        for mode_data in data["modes"]:
            # Adjust cost by scaling factor
            adjusted_cost = (mode_data["cost"] + epsilon) * scaling_factor

            # Combined score is the sum of time and adjusted cost
            combined_score = mode_data["time"] + adjusted_cost
            mode_data["combined_score"] = combined_score

            if combined_score < min_combined_score:
                min_combined_score = combined_score
                best_combined = mode_data

        data["time"] = best_time["time"]
        data["cost"] = best_cost["cost"]
        data["both"] = min_combined_score
        data["time_mode"] = best_time["mode"]
        data["cost_mode"] = best_cost["mode"]
        data["both_mode"] = best_combined["mode"]


def find_optimal_route(graph, start, criteria):
    """Find the optimal route visiting all nodes and returning to start."""
    nodes = list(graph.nodes())
    nodes.remove(start)
    route = [start]

    while nodes:
        current = route[-1]
        best_node = None
        best_weight = float("inf")

        for node in nodes:
            edge_data = graph[current][node]
            if criteria == "both":
                weight = edge_data["both"]
            else:
                weight = edge_data[criteria]
            if weight < best_weight:
                best_weight = weight
                best_node = node

        route.append(best_node)
        nodes.remove(best_node)

    route.append(start)  # Return to start
    return route
