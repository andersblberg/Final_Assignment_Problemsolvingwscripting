def build_graph(relatives, transport_modes):
    import networkx as nx
    from geopy.distance import geodesic

    G = nx.Graph()

    # Add nodes
    for relative in relatives:
        G.add_node(relative["name"], pos=(relative["lat"], relative["lon"]))

    # Add edges with weights
    for i, relative1 in enumerate(relatives):
        for relative2 in relatives[i+1:]:
            # Calculate distance between nodes
            distance_km = geodesic(
                (relative1["lat"], relative1["lon"]),
                (relative2["lat"], relative2["lon"])
            ).km

            # Calculate weights for each transport mode
            for mode in transport_modes:
                travel_time = (distance_km / mode["speed_kmh"]) * 60  # Time in minutes
                cost = distance_km * mode["cost_per_km"]

                # Add edge with weights for "time" and "cost"
                if not G.has_edge(relative1["name"], relative2["name"]):
                    G.add_edge(
                        relative1["name"],
                        relative2["name"],
                        time=travel_time,
                        cost=cost
                    )

    return G
