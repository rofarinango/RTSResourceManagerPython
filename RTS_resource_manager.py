import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
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
                parent, child = line.strip().split()
                if parent not in self.nodes:
                    self.nodes[parent] = Node(parent)
                if child not in self.nodes:
                    self.nodes[child] = Node(child)
                self.graph.add_edge(parent, child)
                self.nodes[parent].dependencies.add(child)

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

    def draw_graph(self):
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

    

    def run(self):
        self.load_resources("resources.txt")
        while True:
            
            self.print_graph()
            self.print_usable_resources()
            command = input("Enter a node name to delete, or 'q' to quit: ")
            if command == 'q':
                break
            else:
                self.delete_node(command)
                nx.draw(self.graph, with_labels=True)
                plt.show()
                
# Create a new ResourceManager instance and run it
rm = ResourceManager()
rm.load_resources("resources.txt")

# Delete a node and redraw the graph

def delete_and_redraw():
    name = entry.get()
    rm.delete_node(name)
    rm.draw_graph()

# Add a label and an entry box for node deletion

label = tk.Label(root, text="Enter a node name to delete:")
label.pack()
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Delete", command=delete_and_redraw)
button.pack()
rm.draw_graph()
root.mainloop()



