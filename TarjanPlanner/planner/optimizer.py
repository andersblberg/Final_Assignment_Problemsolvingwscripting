import networkx as nx

def find_optimal_route(graph, start, end, criteria):
    if criteria not in ['time', 'cost']:
        raise ValueError("Invalid criteria. Choose 'time' or 'cost'.")
    
    # Check if a path exists
    if not nx.has_path(graph, start, end):
        raise nx.NetworkXNoPath(f"No path exists between {start} and {end}.")
    
    # Use NetworkX shortest_path with the selected weight
    return nx.shortest_path(graph, source=start, target=end, weight=criteria)
