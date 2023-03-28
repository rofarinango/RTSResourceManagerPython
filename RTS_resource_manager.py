import networkx as nx
import matplotlib.pyplot as plt

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

    def load_resources(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                parent, child = line.strip().split()
                if parent not in self.nodes:
                    self.nodes[parent] = Node(parent)
                if child not in self.nodes:
                    self.nodes[child] = Node(child)
                self.graph.add_edge(parent, child)
                self.nodes[child].dependencies.add(parent)

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
        for child in list(self.graph.nodes()):
            if name in self.graph.successors(child):
                self.graph.remove_edge(child, name)
                self.nodes[child].dependencies.remove(name)
            if not self.check_usable(child):
                self.nodes[child].usable = False

    def check_usable(self, name):
        node = self.nodes[name]
        for parent in node.dependencies:
            if parent not in self.nodes:
                return False
            if not self.nodes[parent].usable:
                return False
        return True

    def run(self):
        self.load_resources("resources.txt")
        while True:
            nx.draw(self.graph, with_labels=True)
            plt.show()
            self.print_graph()
            self.print_usable_resources()
            command = input("Enter a node name to delete, or 'q' to quit: ")
            if command == 'q':
                break
            else:
                self.delete_node(command)

# Create a new ResourceManager instance and run it
rm = ResourceManager()
rm.run()
