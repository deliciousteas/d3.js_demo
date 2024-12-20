import json
import networkx as nx
import os
#原始数据矩阵
matrix = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
]

# Create an undirected graph from the matrix
G = nx.Graph(matrix)

# Create nodes with attribute 'k' representing the number of edges
nodes = [{"id": node, "k": len(list(G.edges(node)))} for node in G.nodes()]
print(nodes)

# Create edges
edges = [{"source": u, "target": v} for u, v in G.edges()]

# Combine nodes and edges into graph data
graph_data = {
    "nodes": nodes,
    "links": edges
}

# Define the file path
file_path = 'graph_data_01.json'

# Write the graph data to the file
with open(file_path, 'w') as f:
    json.dump(graph_data, f, indent=2)

print("Graph data saved to 'graph_data_01.json'")
