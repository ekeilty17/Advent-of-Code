import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def visualize_graph(adj, start_node, intermediary_nodes, end_node):
    plt.figure(figsize=(12, 10))

    G = nx.from_dict_of_lists(adj)
    anchors = [start_node, end_node] + intermediary_nodes

    # ---- place anchors on a circle ----
    # Note I don't think this actually does anything, but whatever
    radius = 2.0
    fixed_pos = {}
    for i, n in enumerate(anchors):
        angle = 2 * np.pi * i / len(anchors)
        fixed_pos[n] = (radius * np.cos(angle), radius * np.sin(angle))

    # ---- Calculate position of nodes ----
    # this function treats nodes like repelling particles and edges like springs
    # it tries to find the "minimum energy" layout
    pos = nx.spring_layout(
        G,
        pos=fixed_pos,
        k=2 / (len(G) ** 0.5),   # larger spacing for large graphs
        iterations=50
    )

    # --- draw non-anchor nodes ---
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=[n for n in G.nodes() if n not in anchors],
        node_size=20,
        node_color="#1f77b4",
        alpha=0.8,
    )

    # --- draw edges ---
    nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.4)

    # --- draw anchor nodes (big and red) ---
    color_map = {
        start_node: "red",
        end_node: "purple",
        **{node: "orange" for node in intermediary_nodes}
    }
    anchor_colors = [color_map.get(n, "#1f77b4") for n in anchors]
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=anchors,
        node_size=50,
        node_color=anchor_colors,
        edgecolors="black",
    )

    # plt.savefig("device_graph.png", dpi=300, bbox_inches="tight")
    plt.show()