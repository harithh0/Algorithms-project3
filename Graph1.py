import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque  # For BFS

# Create an empty graph
G = nx.Graph()

# Add nodes
nodes = set(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"])
G.add_nodes_from(nodes)

# Define the edges, including the newly added (K, L)
edges = [
    ("A", "B"), ("B", "C"), ("C", "D"), ("A", "F"), ("A", "E"),
    ("I", "M"), ("I", "J"), ("M", "N"), ("E", "I"), ("C", "G"),
    ("B", "F"), ("E", "F"), ("G", "J"), ("H", "K"), ("H", "L"),
    ("K", "O"), ("L", "P"), ("D", "G"), ("K", "L")  # Added this edge
]
G.add_edges_from(edges)

# Define custom positions to create a square-like layout
pos = {
    "A": (0, 3), "B": (1, 3), "C": (2, 3), "D": (3, 3),
    "E": (0, 2), "F": (1, 2), "G": (2, 2), "H": (3, 2),
    "I": (0, 1), "J": (1, 1), "K": (2, 1), "L": (3, 1),
    "M": (0, 0), "N": (1, 0), "O": (2, 0), "P": (3, 0)
}

# Ask user which search algorithm to use and start node
choice = input("1. Random vertex 2. Specific vertex: ")
if choice == '1':
    # Select a random node to start DFS/BFS
    start_node = random.choice(list(G.nodes))
    print(f"Starting search from random node: {start_node}")
elif choice == '2':
    # Print available vertex options
    print("The vertex options are:", list(G.nodes))
    start_node = input("Enter the specific vertex: ")
    if start_node not in G.nodes:
        print("Invalid vertex. Please try again.")
        exit()
else:
    print("Invalid choice.")
    exit()

# Ask which search algorithm to use (DFS or BFS)
algorithm_choice = input("1. Depth-First Search (DFS) 2. Breadth-First Search (BFS): ")

# Function for Depth-First Search (DFS) - Handles disjointed regions
def depth_first_search(graph, start):
    visited = set()

    def dfs(node):
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Ensure all disconnected components are searched
    for node in graph.nodes:
        if node not in visited:
            dfs(node)

# Function for Breadth-First Search (BFS) - Handles disjointed regions
def breadth_first_search(graph, start):
    visited = set()

    def bfs(start_node):
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                print(node, end=" ")
                queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    # Ensure all disconnected components are searched
    for node in graph.nodes:
        if node not in visited:
            bfs(node)

# Function to check if a path exists using DFS
def dfs_path_exists(graph, start, target, visited=None):
    if visited is None:
        visited = set()
    
    if start == target:
        return True  # Found the target
    
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs_path_exists(graph, neighbor, target, visited):
                return True  # Path found

    return False  # No path found

# Function to check if a path exists using BFS
def bfs_path_exists(graph, start, target):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        
        if node == target:
            return True  # Found the target
        
        if node not in visited:
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return False  # No path found

# Perform the search based on user choice
if algorithm_choice == '1':
    print("\nPerforming Depth-First Search (DFS):")
    depth_first_search(G, start_node)
elif algorithm_choice == '2':
    print("\nPerforming Breadth-First Search (BFS):")
    breadth_first_search(G, start_node)
else:
    print("Invalid choice for search algorithm.")
    exit()

# Check if a path exists between two given nodes
source = input("\nEnter the source node to check for a path: ")
destination = input("Enter the destination node: ")

if source in G.nodes and destination in G.nodes:
    dfs_result = dfs_path_exists(G, source, destination)
    bfs_result = bfs_path_exists(G, source, destination)

    print(f"\nPath exists (DFS): {dfs_result}")
    print(f"Path exists (BFS): {bfs_result}")
else:
    print("Invalid nodes. Please enter valid nodes from the graph.")

# Draw the graph
plt.figure(figsize=(6, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
plt.show(block=False)

plt.pause(10)   
