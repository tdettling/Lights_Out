"""This module gives the infrastructure for representing graphs, labeled graphs,
and groups, mainly for the study of the "Lights Out" games.  Vertices
are represented by integers starting at zero.  Edges are represented either by
dictionaries stored in "vert_dict" (where the keys are the vertices and the values
are a list of vertices adjacent to the key) or ordered pairs stored in "edge_set",
which correspond to the two vertices in the edge.  Later, when we want to study
multigraphs, we will let them be triples whose third component is the number of
edges between the two vertices.  We will also have to figure out how to store
multiple edges in the edge dictionary.  Labels are represented by integers
that are either integers modulo some integer k or integers representing group
elements as described below.  It also includes a boolean variable "win" that
tells us if the "Lights Out" game has been won."""

error_dict = {
    1 : "Invalid Input",
    2 : "Connection(s) does not exist",
    3 : "Vertex does not exist",
    4 : "Cannot create vertex - it already exists"
}
class Graph(object):
    """Creates a graph, describing the number of vertices (num_vert) as well as
        the edges (adj_mat or edge_set)"""
    def __init__(self,max_vertex_value):
        # number of vertices, adjacency matrix, edge set
        self.edge_dict = {}
        self.max_vertex_value = max_vertex_value
        self.vertex_values = {}
        self.throw_error = "No Error Present"
        
    def printError(self, error_code):
        global error_dict

        temp_contains = False
        for key in error_dict:
            if key == error_code:
                temp_contains = True
                print(str(error_dict[error_code]))
        if not temp_contains:
            print("Error code does not exist")
    
    def printAdjacency(self):
        for vert in self.edge_dict:
            print (vert)


    def containsVertexInValues(self, vertex):
        contains = False
        for key in self.vertex_values:
            if key == vertex:
                contains = True
        return contains

    def containsVertexInEdgeConnectionDict(self, vertex):
        contains = False
        for key in self.edge_dict:
            if key == vertex:
                contains = True
        return contains

    def containsConnection(self, vertex, connection):
        contains = False
        for key in self.edge_dict:
            if vertex == key:
                if connection in self.edge_dict[key]:
                    contains = True
        return contains 


    def getConnections(self, vertex_name):
        if vertex_name not in self.edge_dict:
            self.printError(3)
            return -1
        else:
            edgeSet = ""
            temp_edge = ""
            for key in self.edge_dict:
                if key == vertex_name:
                    temp_edge = self.edge_dict[key]
            if len(temp_edge) == 0:
                self.printError(2)
                return -1
    
            return edgeSet

    def parseEdges(self, vertex_name):
        if vertex_name in self.edge_dict:
            edges = self.edge_dict[vertex_name]
        else:
            self.printError(3)
            return

        if edges == "null":
            self.printError(2)
            return
        else: 
            edgeList = edges.split(',')
            return edgeList

    def addConnection(self, vertex_name, adjacent_vertex):
        for key in self.edge_dict:
            if key == vertex_name:
                self.edge_dict[key] = self.edge_dict[key] + adjacent_vertex
                print(str(self.edge_dict[key]))


    def addVertex(self, vertex_name, connection = "null", vertex_value = 1):
        if connection not in self.edge_dict and connection != "null":
            print("fixme")
            return
        for key in self.vertex_values:
            if key == vertex_name:
                self.printError(4)
                return
        #edgeSet = 
        self.vertex_values[vertex_name] == vertex_value
        self.addConnection(vertex_name, )
        
            
        self.vertex_values[vertex_name] = vertex_value
        self.edge_dict[vertex_name] = connection
        
        
    def removeVertex(self, vertex_name):
        del self.adj_dict[vertex_name]

    def editVertexValue(self, vertex_name, new_value):
        self.vertex_values[vertex_name] = (new_value) % self.max_vertex_value

    def addOneToVertexValue(self, vertex_name):
        for key in self.vertex_values:
            if key == vertex_name:
                self.vertex_values[key] = (self.vertex_values[key] + 1) % self.max_vertex_value
                return    

    def changeConnection(self, connection_change, new_connection):
        pass

    def toggleVertex(self, vertex_name):
        #toggle desired vertex
        self.addOneToVertexValue(vertex_name)

        #toggle all adjacent verticies
        edges_of_vertex = self.parseEdges(vertex_name)
        #['A', "B", ...]
        for vertex in edges_of_vertex:
            self.addOneToVertexValue(vertex)

    def checkWinner(self):
        for key in self.vertex_values:
            if self.vertex_values[key] != 0:
                return False
        return True

def main_run():
    graph = Graph(1)
    graph.addVertex('A')
    graph.addVertex('B', 'A', 1)

#main_run()
print("done")
