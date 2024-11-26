from planner.data import relatives
from planner.graph import build_graph
from planner.optimizer import calculate_edge_weights, find_optimal_route
from planner.visualizer import draw_graph


transport_modes = [
    {"mode": "Bus", "speed_kmh": 40, "cost_per_km": 2, "transfer_time_min": 5},
    {"mode": "Train", "speed_kmh": 80, "cost_per_km": 5, "transfer_time_min": 2},
    {"mode": "Bicycle", "speed_kmh": 15, "cost_per_km": 0, "transfer_time_min": 1},
    {"mode": "Walking", "speed_kmh": 5, "cost_per_km": 0, "transfer_time_min": 0},
]

def main():
    graph = build_graph(relatives)
    calculate_edge_weights(graph, transport_modes)

    criteria = input("Optimize by (time/cost/both): ").strip().lower()
    if criteria not in ["time", "cost", "both"]:
        print("Error: Invalid criteria. Choose 'time', 'cost', or 'both'.")
        return

    # Find the optimal route
    route = find_optimal_route(graph, "Tarjan's Home", criteria)

    # Calculate total time and cost
    total_time = 0
    total_cost = 0

    print("\nOptimal route details:")
    for i in range(len(route) - 1):
        u = route[i]
        v = route[i + 1]
        edge_data = graph[u][v]
        mode_key = f"{criteria}_mode"
        mode = edge_data[mode_key]
        # Find time and cost for this mode
        for mode_data in edge_data["modes"]:
            if mode_data["mode"] == mode:
                time = mode_data["time"]
                cost = mode_data["cost"]
                break
        total_time += time
        total_cost += cost
        print(f"{u} -> {v}: Mode = {mode}, Time = {time:.2f} minutes, Cost = ₩{cost:.2f}")

    print(f"\nTotal time: {total_time:.2f} minutes")
    print(f"Total cost: ₩{total_cost:.2f}")

    draw_graph(graph, route, criteria)

if __name__ == "__main__":
    main()
