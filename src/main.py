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

# Add a label and an entry box for node deletion
label = tk.Label(root, text="Enter a node name to delete:")
label.pack()
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Delete", command=delete_and_redraw)
button.pack()
rm.draw_graph(root)
root.mainloop()