class Directed_Graph:
    def __init__(self):
        self.graph_dict = {}
    def add_vertex(self, vertex):
        if  vertex in self.graph_dict:
            return "Vertex is already in graph"
        self.graph_dict[vertex] = []
    def add_edge(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        if v1 not in self.graph_dict:
            raise ValueError(f'Vertex {v.get_name()} not in graph')
        if v2 not in self.graph_dict:
            raise ValueError(f'Vertex {v2.get_name()} not in graph')
        self.graph_dict[v1].append(v2)
    def is_vertex_in(self, vertex):
        return vertex in self.graph_dict
    
    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name(): 
                return v
        print(f'Vertex {vertex_name} does not exist')

    def get_neighbours(self, vertex):
        return self.graph_dict[vertex]

    def __str__(self):
        all_edges = ''
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name() + '--->' + v2.get_name() + '\n'
        return all_edges
class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def get_v1(self):
        return self.v1
    def get_v2(self):
        return self.v2
    def __str__(self):
        return self.v1.get_name() + ' ----> ' + self.v2.get_name()

class Vertex:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def __str__(self):
        return self.name