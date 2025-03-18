import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque  # For BFS

# Create an empty graph
G = nx.Graph()

# Add nodes
nodes = sorted(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"])  # Sorted order
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

# Ask user for starting node
choice = input("1. Random vertex 2. Specific vertex: ")
if choice == '1':
    start_node = random.choice(nodes)
    print(f"Starting search from random node: {start_node}")
elif choice == '2':
    print("The vertex options are:", nodes)  # Sorted node list
    start_node = input("Enter the specific vertex: ")
    if start_node not in nodes:
        print("Invalid vertex. Please try again.")
        exit()
else:
    print("Invalid choice.")
    exit()

# Ask user which search algorithm to use
algorithm_choice = input("1. Depth-First Search (DFS) 2. Breadth-First Search (BFS): ")
search_type = input("1. Original (single region) 2. Modified (search all disconnected regions): ")

# Original DFS (searches from a single node)
def original_dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in sorted(graph[start]):  # Sort neighbors for consistent order
        if neighbor not in visited:
            original_dfs(graph, neighbor, visited)

# Original BFS (searches from a single node)
def original_bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            queue.extend(sorted(neighbor for neighbor in graph[node] if neighbor not in visited))  # Sort for consistency

# Modified DFS (searches all disconnected regions)
def modified_dfs(graph):
    visited = set()

    def dfs(node):
        visited.add(node)
        print(node, end=" ")
        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                dfs(neighbor)

    for node in nodes:  # Sorted order
        if node not in visited:
            dfs(node)

# Modified BFS (searches all disconnected regions)
def modified_bfs(graph):
    visited = set()

    def bfs(start_node):
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                print(node, end=" ")
                queue.extend(sorted(neighbor for neighbor in graph[node] if neighbor not in visited))  # Sort for consistency

    for node in nodes:  # Sorted order
        if node not in visited:
            bfs(node)

# Function to check if a path exists using DFS
def dfs_path_exists(graph, start, target, visited=None):
    if visited is None:
        visited = set()
    
    if start == target:
        return True  

    visited.add(start)

    for neighbor in sorted(graph[start]):  # Sort neighbors for consistent order
        if neighbor not in visited:
            if dfs_path_exists(graph, neighbor, target, visited):
                return True  

    return False  

# Function to check if a path exists using BFS
def bfs_path_exists(graph, start, target):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        
        if node == target:
            return True  
        
        if node not in visited:
            visited.add(node)
            queue.extend(sorted(neighbor for neighbor in graph[node] if neighbor not in visited))  # Sort for consistency

    return False  

# Perform the search based on user choice
if algorithm_choice == '1':
    print("\nPerforming Depth-First Search (DFS):")
    if search_type == '1':
        original_dfs(G, start_node)
    elif search_type == '2':
        modified_dfs(G)
    else:
        print("Invalid search type choice.")
        exit()
elif algorithm_choice == '2':
    print("\nPerforming Breadth-First Search (BFS):")
    if search_type == '1':
        original_bfs(G, start_node)
    elif search_type == '2':
        modified_bfs(G)
    else:
        print("Invalid search type choice.")
        exit()
else:
    print("Invalid choice for search algorithm.")
    exit()

# Check if a path exists between two given nodes
print("\nThe vertex options are:", nodes)  # Ensure consistent ordering when displaying nodes again
source = input("\nEnter the source node to check for a path: ")
destination = input("Enter the destination node: ")

if source in nodes and destination in nodes:
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
