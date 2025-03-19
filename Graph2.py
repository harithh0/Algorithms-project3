import matplotlib.pyplot as plt
import networkx as nx

edges = [
    (1, 3),
    (3, 5),
    (3, 2),
    (4, 1),
    (4, 2),
    (4, 12),
    (2, 1),
    (5, 6),
    (5, 8),
    (9, 5),
    (9, 11),
    (8, 9),
    (8, 10),
    (11, 12),
    (10, 11),
    (10, 9),
    (7, 10),
    (6, 7),
    (6, 10),
    (6, 8),
]

G = nx.DiGraph()

G.add_edges_from(edges)

plt.figure(figsize=(10, 8))
nx.draw(
    G,
    with_labels=True,
    node_size=500,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
    arrows=True,
)
plt.title("Original Digraph")
plt.show()

scc = list(nx.strongly_connected_components(G))
print("Strongly Connected Components:", scc)

# doing meta graph here..
meta_graph = nx.DiGraph()

scc_mapping = {}
for i, component in enumerate(scc):
    for node in component:
        scc_mapping[node] = i

for u, v in G.edges():
    if scc_mapping[u] != scc_mapping[v]:
        meta_graph.add_edge(scc_mapping[u], scc_mapping[v])

plt.figure(figsize=(10, 8))
pos_meta = nx.spring_layout(meta_graph, seed=42)  # 'seed' for consistency
nx.draw(
    meta_graph,
    pos=pos_meta,
    with_labels=True,
    node_size=500,
    node_color="lightgreen",
    font_size=10,
    font_weight="bold",
    arrows=True,
)
plt.title("Meta Graph (SCCs)")
plt.show()

# sort of meta graph
if nx.is_directed_acyclic_graph(meta_graph):
    topological_order = list(nx.topological_sort(meta_graph))
    print("Topological Order of Meta Graph:", topological_order)
else:
    print("The meta graph is not a DAG.")
