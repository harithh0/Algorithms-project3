import networkx as nx
import matplotlib.pyplot as plt

# Kruskal's Algorithm
def kruskal_mst(graph):
    edges = sorted(graph.edges(data=True), key=lambda edge: edge[2]['weight'])
    mst = nx.Graph()  # Minimum Spanning Tree
    mst.add_nodes_from(graph.nodes)

    parent = {node: node for node in graph.nodes}  # Union-Find parent mapping
    rank = {node: 0 for node in graph.nodes}      # Rank mapping

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])  # Path compression
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    for u, v, data in edges:
        if find(u) != find(v):  # Check for cycle
            mst.add_edge(u, v, weight=data['weight'])
            union(u, v)

    return mst

# Dijkstra's Algorithm
def dijkstra(graph, start_node):
    visited = {start_node: 0}
    path = {}
    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for neighbor, edge_data in graph[min_node].items():
            weight = current_weight + edge_data['weight']
            if neighbor not in visited or weight < visited[neighbor]:
                visited[neighbor] = weight
                path[neighbor] = min_node

    return visited, path

# Main Function
def main():
    # Initialize the graph
    G = nx.Graph()
    G.add_nodes_from(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
    G.add_weighted_edges_from([
        ("A", "B", -22), ("A", "C", 9), ("A", "D", 12),
        ("B", "H", 34), ("B", "F", 36), ("C", "F", 42),
        ("C", "E", 65), ("C", "D", 4), ("D", "E", 33),
        ("D", "I", 30), ("F", "H", 24), ("F", "G", 39),
        ("F", "E", 18), ("E", "G", 23), ("G", "H", 25),
        ("G", "I", 21), ("H", "I", 19)
    ])

    # Draw the graph
    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(
        G, pos, edge_color='black', width=1, linewidths=1,
        node_size=500, node_color='pink', alpha=0.9,
        labels={node: node for node in G.nodes()}
    )
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Graph Tree")
    plt.show()

    # Apply Kruskal's Algorithm for MST
    mst = kruskal_mst(G)
    print("Edges in the Minimum Spanning Tree:")
    for edge in mst.edges(data=True):
        print(edge)

    # Draw the MST
    plt.figure()
    nx.draw(
        mst, pos, edge_color='blue', width=2, linewidths=2,
        node_size=500, node_color='green', alpha=0.9,
        labels={node: node for node in mst.nodes()}
    )
    edge_labels = nx.get_edge_attributes(mst, "weight")
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels)
    plt.title("MST Using Kruskal's Algorithm")
    plt.show()

    # Apply Dijkstra's Algorithm
    start_node = "A"
    visited, path = dijkstra(G, start_node)
    print(f"Dijkstra's paths from {start_node}:")
    print("Visited vs Cost to path from A: \n", visited)
    print(" Path (Target node: Predecessor node):\n", path)
    
    # Construct the Dijkstra's shortest path tree as a subgraph
    dijkstra_tree = nx.DiGraph()
    for node, predecessor in path.items():
        dijkstra_tree.add_edge(predecessor, node, weight=visited[node])
    
    # Draw the Dijkstra's shortest path tree
    plt.figure()
    nx.draw(
        dijkstra_tree, pos, edge_color='red', width=2, linewidths=2,
        node_size=500, node_color='grey', alpha=0.9,
        labels={node: node for node in dijkstra_tree.nodes()}
    )
    edge_labels = nx.get_edge_attributes(dijkstra_tree, "weight")
    nx.draw_networkx_edge_labels(dijkstra_tree, pos, edge_labels=edge_labels)
    plt.title(f"Dijkstra's Shortest Path Tree (from {start_node})")
    plt.show()

    
    
if __name__ == "__main__":
    main()
