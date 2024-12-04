import pytest
from planner.graph import build_graph
from planner.optimizer import calculate_edge_weights, find_optimal_route
from planner.data import relatives

transport_modes = [
    {"mode": "Bus", "speed_kmh": 40, "cost_per_km": 2, "transfer_time_min": 5},
    {"mode": "Train", "speed_kmh": 80, "cost_per_km": 5, "transfer_time_min": 2},
    {"mode": "Bicycle", "speed_kmh": 15, "cost_per_km": 0, "transfer_time_min": 1},
    {"mode": "Walking", "speed_kmh": 5, "cost_per_km": 0, "transfer_time_min": 0},
]

def test_build_graph():
    graph = build_graph(relatives)
    assert graph is not None
    nodes = set(graph.nodes())
    expected_nodes = set(relative['name'] for relative in relatives)
    assert nodes == expected_nodes
    for u, v, data in graph.edges(data=True):
        assert 'distance' in data
        assert data['distance'] > 0

def test_calculate_edge_weights():
    graph = build_graph(relatives)
    calculate_edge_weights(graph, transport_modes)
    for u, v, data in graph.edges(data=True):
        assert 'modes' in data
        assert isinstance(data['modes'], list)
        assert len(data['modes']) == len(transport_modes)
        for mode_data in data['modes']:
            assert 'mode' in mode_data
            assert 'time' in mode_data
            assert 'cost' in mode_data
            assert 'combined_score' in mode_data
            assert mode_data['time'] > 0
            assert mode_data['cost'] >= 0
            assert mode_data['combined_score'] > 0

def test_find_optimal_route():
    graph = build_graph(relatives)
    calculate_edge_weights(graph, transport_modes)
    start_node = "Tarjan's Home"
    criteria = 'both'
    route = find_optimal_route(graph, start_node, criteria)
    print("Route:", route)
    assert route[0] == start_node
    assert route[-1] == start_node
    visited_nodes = route[1:-1] 
    expected_nodes = [relative['name'] for relative in relatives if relative['name'] != start_node]
    assert set(visited_nodes) == set(expected_nodes)
    assert len(visited_nodes) == len(set(visited_nodes))


@pytest.mark.parametrize("criteria", ["time", "cost", "both"])
def test_find_optimal_route_criteria(criteria):
    graph = build_graph(relatives)
    calculate_edge_weights(graph, transport_modes)
    start_node = "Tarjan's Home"
    route = find_optimal_route(graph, start_node, criteria)
    assert route[0] == start_node
    assert route[-1] == start_node
    visited_nodes = route[:-1]
    expected_nodes = [relative['name'] for relative in relatives if relative['name'] != start_node]
    assert set(visited_nodes) == set(expected_nodes)
    assert len(route) == len(relatives) + 1

@pytest.mark.parametrize("criteria", ["time", "cost", "both"])
def test_find_optimal_route_criteria(criteria):
    graph = build_graph(relatives)
    calculate_edge_weights(graph, transport_modes)
    start_node = "Tarjan's Home"
    route = find_optimal_route(graph, start_node, criteria)
    assert route[0] == start_node
    assert route[-1] == start_node
    visited_nodes = route[1:-1]  # Exclude start and end nodes
    expected_nodes = [relative['name'] for relative in relatives if relative['name'] != start_node]
    assert set(visited_nodes) == set(expected_nodes)
    # Optional: Ensure no duplicates in visited_nodes
    assert len(visited_nodes) == len(set(visited_nodes))


def test_build_graph_empty():
    empty_relatives = []
    graph = build_graph(empty_relatives)
    assert graph.number_of_nodes() == 0
    assert graph.number_of_edges() == 0
