# Resource Manager Application

Resource Manager for a Real Time Strategy (RTS) game. 


The Resource Manager Application is a graphical user interface (GUI) program for managing resources and their dependencies. It allows users to create, delete, and link resources in a graph-like structure.

The program manages a "directed graph" (a system of nodes and links between them going in one direction, much like web pages and their links). On startup, the program reads a file "resource.txt" (from the src directory) which describes resources and the resources they depend on. The file resource.txt could, for example, contain (exactly 4 lines):

```
handgun bullets
bullets ore
bombs ore
turret bullets
```

The first line says that there is a link from a node called "handgun" to a node called 'bullet". This means for a handgun to be a useable, it relies on the resource bullets.

## Requirements:

The program work with any amount of nodes and any amount of links between them. To this end, the program represent nodes with a Node class, and the set of links for a single node using set container.
The program display a current view of the graph. For any current node, if any of the nodes it relies on get deleted that node becomes unusable.

A user should be allowed to delete a node and quit at any time.

A user should be allowed to insert new nodes and new links.


## Installation
To run the Resource Manager Application, you need to have Python 3 and the Tkinter library installed on your machine. If you don't have them installed, you can download them from the official websites:

Python: https://www.python.org/downloads/

Tkinter: https://docs.python.org/3/library/tkinter.html

After installing Python and Tkinter, you can download or clone the application source code from the GitHub repository:

GitHub repository: https://github.com/rofarinango/RTSResourceManagerPython

## Usage
Install the requriments with the following command:

`pip install -r requirements.txt`

### On Ubuntu:

If tkinter is not install, run the following command:
`sudo apt-get install python3-tk`

## Run
To run the application run the following command:

`python src/main.py`

This will start the application and open the main window.

## Test

To run tests run the following commando in the root directory:
`pytest`


## Graphical User Interface
The Resource Manager Application GUI consists of two main components:

Graph Area
The graph area is the main display of the application. It shows the resources and their dependencies as nodes and links, respectively. Users can zoom in and out of the graph using the mouse wheel or the zoom buttons on the control panel.

Control Panel
The control panel is located on the right side of the main window. It provides the following buttons and input fields:

"Enter a node name to delete" input field: Allows users to delete a resource by entering its name and clicking the "Delete" button.

"Start node" and "End node" input fields: Allow users to add a link between two resources by entering their names and clicking the "Add Link" button.

"Add Link" button: Adds a link between two resources.

"Delete" button: Deletes a resource from the graph.

![image](https://user-images.githubusercontent.com/47066093/229018826-b551def5-d41b-46a3-ad21-81b532e4890c.png)

