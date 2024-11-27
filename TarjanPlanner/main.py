from planner.data import relatives
from planner.graph import build_graph
from planner.optimizer import calculate_edge_weights, find_optimal_route
from planner.visualizer import draw_graph
from planner.timer import timeit
import logging

transport_modes = [
    {"mode": "Bus", "speed_kmh": 40, "cost_per_km": 2, "transfer_time_min": 5},
    {"mode": "Train", "speed_kmh": 80, "cost_per_km": 5, "transfer_time_min": 2},
    {"mode": "Bicycle", "speed_kmh": 15, "cost_per_km": 0, "transfer_time_min": 1},
    {"mode": "Walking", "speed_kmh": 5, "cost_per_km": 0, "transfer_time_min": 0},
]

@timeit
def build_the_graph():
    graph = build_graph(relatives)
    return graph

@timeit
def calculate_weights(graph, transport_modes):
    calculate_edge_weights(graph, transport_modes)

@timeit
def find_route(graph, start_node, criteria):
    route = find_optimal_route(graph, start_node, criteria)
    return route

@timeit
def compute_totals_and_print(graph, route, criteria):
    total_time = 0
    total_cost = 0
    total_distance = 0

    print("\nOptimal route details:")
    for i in range(len(route) - 1):
        u = route[i]
        v = route[i + 1]
        edge_data = graph[u][v]
        distance = edge_data["distance"]
        total_distance += distance
        mode_key = f"{criteria}_mode"
        mode = edge_data[mode_key]

        # Find time and cost for this mode
        for mode_data in edge_data["modes"]:
            if mode_data["mode"] == mode:
                time_value = mode_data["time"]
                cost = mode_data["cost"]
                break

        total_time += time_value
        total_cost += cost
        print(f"{u} -> {v}: Distance = {distance:.2f} km, Mode = {mode}, Time = {time_value:.2f} minutes, Cost = ₩{cost:,.2f}")

    print(f"\nTotal distance: {total_distance:.2f} km")
    print(f"Total time: {total_time:.2f} minutes")
    print(f"Total cost: ₩{total_cost:,.2f}")

    return total_time, total_cost, total_distance

def main():
    # User input (not timed)
    criteria = input("Optimize by (time/cost/both): ").strip().lower()
    if criteria not in ["time", "cost", "both"]:
        print("Error: Invalid criteria. Choose 'time', 'cost', or 'both'.")
        return

    total_execution_time = 0  # Initialize total execution time

    # Step 1: Build the graph
    (graph, elapsed_time) = build_the_graph()
    total_execution_time += elapsed_time

    # Step 2: Calculate edge weights
    (_, elapsed_time) = calculate_weights(graph, transport_modes)
    total_execution_time += elapsed_time

    # Step 3: Find the optimal route
    (route, elapsed_time) = find_route(graph, "Tarjan's Home", criteria)
    total_execution_time += elapsed_time

    # Step 4: Compute totals and print route details
    (_, elapsed_time) = compute_totals_and_print(graph, route, criteria)
    total_execution_time += elapsed_time

    # Display the total execution time
    print(f"\nTotal execution time: {total_execution_time:.4f} seconds.")

    # Log the total execution time
    logging.info(f"Total execution time: {total_execution_time:.4f} seconds.")

    # Plotting (not timed)
    draw_graph(graph, route, criteria)

if __name__ == "__main__":
    main()
