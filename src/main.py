import tkinter as tk
from RTS_resource_manager import ResourceManager

root = tk.Tk()
# Create a new ResourceManager instance and run it
rm = ResourceManager()
rm.load_resources("src/resources.txt")

# Delete a node and redraw the graph
def delete_and_redraw():
    name = entry.get()
    rm.delete_node(name)
    rm.draw_graph(root)
    rm.print_graph()

def add_and_redraw():
    name = entry_adding_node.get()
    rm.add_node(name)
    rm.draw_graph(root)
    rm.print_graph()

# Add a label and an entry box for node deletion
label = tk.Label(root, text="Enter a node name to delete:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Delete button and handle on click
button = tk.Button(root, text="Delete", command=delete_and_redraw)
button.pack()

#Add a label and an entry box for adding node
add_node_label = tk.Label(root, text="Enter a node name to add:")
add_node_label.pack()
entry_adding_node = tk.Entry(root)
entry_adding_node.pack()
# Add node button and handle on click
add_node_btn = tk.Button(root, text="Add Node", command=add_and_redraw)
add_node_btn.pack()


rm.draw_graph(root)
root.mainloop()