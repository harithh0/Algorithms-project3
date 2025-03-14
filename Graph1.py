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

# Function for Depth-First Search (DFS)
def depth_first_search(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")  # Process the current node (e.g., print it)

    for neighbor in graph[start]:
        if neighbor not in visited:
            depth_first_search(graph, neighbor, visited)

# Function for Breadth-First Search (BFS)
def breadth_first_search(graph, start):
    visited = set()
    queue = deque([start])  # Queue to hold nodes to explore
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")  # Process the current node (e.g., print it)
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Initialize visited nodes set
visited_nodes = set()

# Perform the search based on user choice
if algorithm_choice == '1':
    print("Performing Depth-First Search (DFS):")
    depth_first_search(G, start_node)
elif algorithm_choice == '2':
    print("Performing Breadth-First Search (BFS):")
    breadth_first_search(G, start_node)
else:
    print("Invalid choice for search algorithm.")
    exit()

# Draw the graph
plt.figure(figsize=(6, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
plt.show(block=False)

plt.pause(10)
