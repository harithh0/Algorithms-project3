import matplotlib.pyplot as plt
import networkx as nx

meta_G = nx.DiGraph()

scc_nodes = {
    "SCC1 (12)": {12},
    "SCC2 (11)": {11},
    "SCC3 (5,6,7,8,9,10)": {5, 6, 7, 8, 9, 10},
    "SCC4 (1,2,3)": {1, 2, 3},
    "SCC5 (4)": {4},
}

meta_G.add_nodes_from(scc_nodes.keys())

meta_edges = [
    ("SCC5 (4)", "SCC4 (1,2,3)"),  # 4 → {1,2,3}
    ("SCC5 (4)", "SCC1 (12)"),  # 4 → 12
    ("SCC4 (1,2,3)", "SCC3 (5,6,7,8,9,10)"),  # 3 → {5,6,7,8,9,10}
    ("SCC3 (5,6,7,8,9,10)", "SCC2 (11)"),  # 9 → 11, 10 → 11
    ("SCC2 (11)", "SCC1 (12)"),  # 11 → 12
]

meta_G.add_edges_from(meta_edges)

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(meta_G, seed=42)
nx.draw(
    meta_G,
    pos,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
    edge_color="black",
    arrowsize=20,
)

plt.title("Meta Graph of Strongly Connected Components")
plt.show()
