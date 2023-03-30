import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define the Node class to represent each resource
class Node:
    def __init__(self, name):
        self.name = name
        self.usable = True
        self.dependencies = set()
        
    def __repr__(self):
        return self.name

# Define the Resource Manager class to manage the graph
class ResourceManager:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.nodes = {}
        self.canvas = None
        self.pos = None

    def load_resources(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                start_node, end_node = line.strip().split()
                if start_node not in self.nodes: # Avoid duplicate nodes from file
                    self.nodes[start_node] = Node(start_node)
                if end_node not in self.nodes:
                    self.nodes[end_node] = Node(end_node)
                self.graph.add_edge(start_node, end_node)
                self.nodes[start_node].dependencies.add(end_node)

    def print_graph(self):
        print("Resources graph:")
        for node in self.graph.nodes():
            print(node, " -> ", list(self.graph.successors(node)))

    def print_usable_resources(self):
        print("Usable resources:")
        for node in self.nodes.values():
            if node.usable:
                print(node.name, "is usable")
            else:
                print(node.name, "is not usable")

    def delete_node(self, name):
        if name not in self.nodes:
            print(name, "does not exist")
            return
        self.nodes.pop(name)
        self.graph.remove_node(name)
        #print(list(self.graph.nodes()))
        for current_node in list(self.graph.nodes()):
            if name in self.graph.successors(current_node):
                self.graph.remove_edge(current_node, name)
                self.nodes[current_node].dependencies.remove(name)
            if name in self.nodes[current_node].dependencies:
                self.nodes[current_node].usable = False
        self.print_usable_resources()

    def draw_graph(self, root):
        colors = []
        for node in self.graph.nodes():
            if self.nodes[node].usable:
                colors.append('lightblue')
            else:
                colors.append((1.0,0.75,0.796))
        if self.canvas is not None:
            self.canvas.get_tk_widget().destroy()
        if self.pos is None:
            self.pos = nx.spring_layout(self.graph)
        fig = plt.figure(figsize=(5,4), dpi=100)
        nx.draw(self.graph, pos=self.pos, with_labels=True, node_color=colors)
        self.canvas = FigureCanvasTkAgg(fig, master=root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
