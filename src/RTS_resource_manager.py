import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define the Node class to represent each resource
class Node:
    """Class to represent each resource.

    Attributes:
        name (str): The name of the node.
        usable (bool): Whether or not the node is currently usable.
        dependencies (set): A set of the names of nodes that this node depends on.
    """
    def __init__(self, name):
        """Initialize a Node object.

        Args:
            name (str): The name of the node.
        """
        self.name = name
        self.usable = True
        self.dependencies = set()
        
    def __repr__(self):
        """Returns the string representation of the node."""
        return self.name

# Define the Resource Manager class to manage the graph
class ResourceManager:
    """Class that represents a graph implementation containing resources.

    Attributes:
        graph (networkx.DiGraph): The resource graph.
        nodes (dict): A dictionary mapping node names to Node objects.
        canvas (FigureCanvasTkAgg): A Matplotlib canvas for displaying the graph.
        pos (dict): A dictionary mapping node names to their positions in the graph visualization.
    """
    def __init__(self):
        """Initialize a ResourceManager object."""
        self.graph = nx.DiGraph()
        self.nodes = {}
        self.canvas = None
        self.pos = None

    def load_resources(self, filename):
        """Load resource links from a file.

        The file should contain one link per line, in the format 'start_node end_node'.

        Args:
            filename (str): The name of the file to load.
        
        Raises:
        ValueError: If the file has an invalid format.

        """
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    # Skip empty lines
                    continue
                try:
                    start_node, end_node = line.split()
                except ValueError:
                    # Skip lines that don't have exactly two words
                    raise ValueError(f"Skipping line '{line}' in file '{filename}': format should be 'start_node end_node'")
                self.add_link(start_node, end_node)

    def print_graph(self):
        """Print the resource graph."""
        print("Resources graph:")
        for node in self.graph.nodes():
            print(node, " -> ", list(self.graph.successors(node)))

    def print_usable_resources(self):
        """Print the usable resources."""
        print("Usable resources:")
        for node in self.nodes.values():
            if node.usable:
                print(node.name, "is usable")
            else:
                print(node.name, "is not usable")

    def delete_node(self, name):
        """Delete a node from the resource graph.

        Args:
            name (str): The name of the node to delete.
        """
        if name not in self.nodes:
            print(name, "does not exist")
            return
        self.nodes.pop(name)
        self.graph.remove_node(name)
        #Iterate over the nodes dicitonary to search for the node to delete in the adjacency list
        # If found, remove the edge from the graph and from the dependencies set of the current node
        for current_node in list(self.graph.nodes()):
            if name in self.graph.successors(current_node):
                self.graph.remove_edge(current_node, name)
                self.nodes[current_node].dependencies.remove(name)
            if name in self.nodes[current_node].dependencies:
                self.nodes[current_node].usable = False
        self.print_usable_resources()

    def draw_graph(self, root):
        """Draw the resource graph using Matplotlib.

        Args:
            root (tk.Tk): The root Tkinter window to display the graph in.
        """
        colors = []
        # Make the usable nodes get lightblue colored while the unusable nodes get a lightred color.
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
        self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=2)

    def add_node(self, name):
        """
        Adds a new node with the specified name to the graph, if it does not already exist.

        Args:
            name (str): The name of the node to add.
        """
        if name not in self.nodes:
            self.nodes[name] = Node(name)
            self.graph.add_node(name)
        self.pos = None

    def add_link(self, start_node, end_node):
        """
        Adds a new link from the start_node to the end_node in the graph.

        If either node does not exist in the graph, a new node is created with the given name and added to the graph.

        Args:
            start_node (str): The name of the node from which the link starts.
            end_node (str): The name of the node to which the link is directed.
        """
        # Avoid duplicate nodes from file
        if start_node not in self.nodes: 
            self.nodes[start_node] = Node(start_node)
        if end_node not in self.nodes:
            self.nodes[end_node] = Node(end_node)
        self.graph.add_edge(start_node, end_node)
        self.nodes[start_node].dependencies.add(end_node)
        self.pos = None
