from planner.data import relatives
from planner.graph import build_graph
from planner.optimizer import find_optimal_route
from planner.visualizer import draw_graph


# Define transport modes
transport_modes = [
    {"mode": "Bus", "speed_kmh": 40, "cost_per_km": 2, "transfer_time_min": 5},
    {"mode": "Train", "speed_kmh": 80, "cost_per_km": 5, "transfer_time_min": 2},
    {"mode": "Bicycle", "speed_kmh": 15, "cost_per_km": 0, "transfer_time_min": 1},
    {"mode": "Walking", "speed_kmh": 5, "cost_per_km": 0, "transfer_time_min": 0},
]

def main():
    # Build the graph
    graph = build_graph(relatives, transport_modes)

    # Display available locations
    print("Available locations:")
    for relative in relatives:
        print(f"- {relative['name']} ({relative['street']})")

    # Get user inputs
    start = input("\nEnter the starting location (e.g., Relative_1): ").strip()
    end = input("Enter the ending location (e.g., Relative_10): ").strip()
    criteria = input("Optimize by (time/cost): ").strip().lower()

    # Validate inputs
    if start not in graph:
        print(f"Error: '{start}' is not a valid location.")
        return
    if end not in graph:
        print(f"Error: '{end}' is not a valid location.")
        return
    if criteria not in ["time", "cost"]:
        print("Error: Invalid criteria. Please choose 'time' or 'cost'.")
        return

    # Debugging: Print edges with weights
    print("\nGraph edges with weights:")
    for edge in graph.edges(data=True):
        print(edge)

    # Find the optimal route
    try:
        route = find_optimal_route(graph, start, end, criteria)

        print("\nOptimal route details:")
        for i in range(len(route) - 1):
            edge_data = graph[route[i]][route[i + 1]]
            print(f"{route[i]} -> {route[i + 1]}: Time = {edge_data['time']:.2f} minutes, Cost = {edge_data['cost']:.2f} units")

        # Calculate total weight (time or cost)
        total_weight = sum(
            graph[route[i]][route[i + 1]][criteria]
            for i in range(len(route) - 1)
        )

        print("\nOptimal route:", route)
        if criteria == "time":
            print(f"Total time: {total_weight:.2f} minutes")
        else:
            print(f"Total cost: {total_weight:.2f} units")

        # Visualize the graph and the optimal route
        draw_graph(graph, route)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
