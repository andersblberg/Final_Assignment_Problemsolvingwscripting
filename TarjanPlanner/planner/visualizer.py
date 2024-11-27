import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph, route, criteria):
    """
    Draw the graph with specified edge colors for transport modes, display only the optimal route,
    and include a comprehensive legend for all visual elements.
    """
    # Define node positions
    pos = nx.get_node_attributes(graph, 'pos')

    # Define edge colors for different modes
    edge_colors = {
        "Bus": "darkblue",
        "Train": "green",
        "Bicycle": "orange",
        "Walking": "red",
    }

    # Draw nodes
    nx.draw_networkx_nodes(
        graph, pos,
        nodelist=[node for node in graph.nodes if node != "Tarjan's Home"],
        node_size=200, node_color='lightblue', label="Relatives (light blue circles)"
    )
    nx.draw_networkx_nodes(
        graph, pos,
        nodelist=["Tarjan's Home"],
        node_size=700, node_color='green', node_shape='s', label="Home (green square)"
    )
    nx.draw_networkx_labels(graph, pos, font_size=8, font_color='black')

    # Highlight the optimal route with specific colors
    path_edges = list(zip(route[:-1], route[1:]))
    for i, (u, v) in enumerate(path_edges):
        edge_data = graph[u][v]
        mode = edge_data[f"{criteria}_mode"]
        nx.draw_networkx_edges(
            graph, pos, edgelist=[(u, v)],
            edge_color=edge_colors[mode],
            width=2.5, label=f"{mode} ({edge_colors[mode]})" if i == 0 else None
        )

    # Add a legend for all visual elements
    legend_elements = [
        plt.Line2D([0], [0], color='darkblue', lw=2, label='Bus (dark blue)'),
        plt.Line2D([0], [0], color='green', lw=2, label='Train (green)'),
        plt.Line2D([0], [0], color='orange', lw=2, label='Bicycle (orange)'),
        plt.Line2D([0], [0], color='red', lw=2, label='Walking (red)'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightblue', markersize=10, label='Relatives'),
        plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='green', markersize=10, label="Home"),
    ]
    plt.legend(handles=legend_elements, loc="upper right", fontsize="small", title="Legend")

    mode_key = f"{criteria}_mode"
    for i, (u, v) in enumerate(zip(route[:-1], route[1:])):
        edge_data = graph[u][v]
        mode = edge_data[mode_key]
        nx.draw_networkx_edges(
            graph, pos, edgelist=[(u, v)],
            edge_color=edge_colors[mode],
            width=2.5
        )

    # Add axes labels and a title
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Optimal Route Visualization")
    plt.show()
