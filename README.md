# Resource Manager Application
The Resource Manager Application is a graphical user interface (GUI) program for managing resources and their dependencies. It allows users to create, delete, and link resources in a graph-like structure.

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

