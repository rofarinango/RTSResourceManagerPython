import networkx as nx
import matplotlib as plt

def build_graph_from_file(file_path: str):
    rts = nx.Graph()
    with open(file_path, 'r') as f:
        for line in f:
            current_edge = line.strip().split()
            if not rts.has_node(current_edge[0]):
                rts.add_node(current_edge[0])
            if not rts.has_node(current_edge[1]):
                rts.add_node(current_edge[1])
            print(rts.nodes[current_edge[0]])
            rts.add_edge(rts.nodes[current_edge[0]], rts.nodes[current_edge[1]])
    
    return rts

RTSGraph = build_graph_from_file("resources.txt")

nx.draw(RTSGraph, with_labels=True)
plt.show()