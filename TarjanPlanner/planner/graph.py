import networkx as nx
from geopy.distance import geodesic

def build_graph(relatives):
    """Build a graph with distances between relatives."""
    graph = nx.Graph()

    # Add nodes with positions
    for relative in relatives:
        graph.add_node(
            relative["name"],
            pos=(relative["lon"], relative["lat"])  # Using corrected `lon` and `lat` fields
        )

    # Add edges with geodesic distances
    for i, relative1 in enumerate(relatives):
        for j, relative2 in enumerate(relatives):
            if i < j:
                pos1 = (relative1["lat"], relative1["lon"])
                pos2 = (relative2["lat"], relative2["lon"])
                distance_km = geodesic(pos1, pos2).kilometers
                graph.add_edge(
                    relative1["name"],
                    relative2["name"],
                    distance=distance_km
                )

    return graph
