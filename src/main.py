import tkinter as tk
from rts_resource_manager import ResourceManager

def main():
    """
    Entry point of the application.
    """
    root = tk.Tk()
    resource_manager = ResourceManager()
    resource_manager.load_resources("src/resources.txt")
    help(ResourceManager)

    # GUI creation
    gui = GUI(root, resource_manager)
    gui.create_gui()
    gui.start()

    root.mainloop()

class GUI:
    """
    A class for the GUI of the resource manager application.
    """
    def __init__(self, root, resource_manager):
        """
        Initializes the GUI.

        Parameters:
        root (tk.Tk): The root window of the application.
        resource_manager (ResourceManager): The resource manager object to be used.
        """
        self.root = root
        self.resource_manager = resource_manager
        self.canvas = None

    def create_gui(self):
        """
        Creates the GUI.
        """
        self.create_delete_node_widgets()
        self.create_add_link_widgets()
        self.resource_manager.draw_graph(self.root)

    def create_delete_node_widgets(self):
        """
        Creates the widgets for deleting a node.
        """
        label = tk.Label(self.root, text="Enter a node name to delete:")
        label.grid(row=0, column=0, columnspan=2)
        entry = tk.Entry(self.root)
        entry.grid(row=1, column=0, columnspan=2)
        button = tk.Button(self.root, text="Delete", command=lambda: self.on_delete_node_click(entry.get()))
        button.grid(row=2, column=0, columnspan=2)

    def create_add_link_widgets(self):
        """
        Creates the widgets for adding a link.
        """
        start_node_label = tk.Label(self.root, text="Start node:")
        start_node_label.grid(row=3, column=0)
        start_node_entry = tk.Entry(self.root)
        start_node_entry.grid(row=4, column=0)
        end_node_label = tk.Label(self.root, text="End node:")
        end_node_label.grid(row=3, column=1)
        end_node_entry = tk.Entry(self.root)
        end_node_entry.grid(row=4, column=1)
        add_link_btn = tk.Button(self.root, text="Add Link",
                                 command=lambda: self.on_add_link_click(start_node_entry.get(), end_node_entry.get()))
        add_link_btn.grid(row=5, column=0, columnspan=2)

    def start(self):
        """
        Starts the main event loop of the application.
        """
        self.root.mainloop()

    def on_delete_node_click(self, node_name):
        """
        Event handler for when the delete button is clicked.

        Parameters:
        node_name (str): The name of the node to be deleted.
        """
        self.resource_manager.delete_node(node_name)
        self.resource_manager.draw_graph(self.root)
        self.resource_manager.print_graph()

    def on_add_link_click(self, start_node, end_node):
        """
        Event handler for when the add link button is clicked.

        Parameters:
        start_node (str): The name of the start node.
        end_node (str): The name of the end node.
        """
        if start_node == '' and end_node == '':
            return
        if start_node == '':
            self.resource_manager.add_node(end_node)
        elif end_node == '':
            self.resource_manager.add_node(start_node)
        else:
            self.resource_manager.add_link(start_node, end_node)
        self.resource_manager.draw_graph(self.root)
        self.resource_manager.print_graph()

if __name__ == '__main__':
    main()