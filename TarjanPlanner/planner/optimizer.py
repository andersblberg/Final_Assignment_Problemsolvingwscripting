def calculate_edge_weights(graph, transport_modes):
    """Calculate time and cost for all edges in the graph."""
    for u, v, data in graph.edges(data=True):
        distance = data["distance"]
        best_time = float("inf")
        best_cost = float("inf")
        best_mode_time = None
        best_mode_cost = None

        for mode in transport_modes:
            travel_time = (distance / mode["speed_kmh"]) * 60
            travel_cost = distance * mode["cost_per_km"]

            # Choose best mode for time
            if travel_time < best_time:
                best_time = travel_time
                best_mode_time = mode["mode"]

            # Choose best mode for cost
            if travel_cost < best_cost:
                best_cost = travel_cost
                best_mode_cost = mode["mode"]

        data["time"] = best_time
        data["cost"] = best_cost
        data["time_mode"] = best_mode_time
        data["cost_mode"] = best_mode_cost


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
            weight = graph[current][node][criteria]
            if weight < best_weight:
                best_weight = weight
                best_node = node

        route.append(best_node)
        nodes.remove(best_node)

    route.append(start)  # Return to start
    return route
