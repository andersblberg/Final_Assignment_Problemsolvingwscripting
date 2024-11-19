import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph, route):
    pos = nx.get_node_attributes(graph, 'pos')  # Get node positions
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500)
    path_edges = list(zip(route[:-1], route[1:]))  # Create edges for the route
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)
    plt.title("Optimal Route Visualization")
    plt.show()
