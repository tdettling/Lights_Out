"""This module gives the infrastructure for representing graphs,
 mainly for the study of the "Lights Out" games.  Vertices
are represented by integers starting at zero.  Edges are represented by
dictionaries stored in "edge_dict" (where the keys are the vertices and the values
are a list of vertices adjacent to the key),
which correspond to the two vertices in the edge. Labels  (on/off) are represented by integers
that are either integers modulo some integer k or integers representing group
elements as described below.  It also includes a fucntion "checkWinner() that
tells us if the "Lights Out!" game has been won."""


error_dict = {
    1 : "Invalid Input",
    2 : "Connection(s) does not exist",
    3 : "Vertex does not exist",
    4 : "Cannot create vertex - it already exists"
}
class Graph(object):
    """
    Creates a graph, describing the number of 
    vertices (num_vert) as well as
    the edges (adj_mat or edge_set)"""
    def __init__(self,max_vertex_value=2):
        # number of vertices, adjacency matrix, edge set
        self.edge_dict = {}
        self.max_vertex_value = max_vertex_value
        self.vertex_values = {}
        self.throw_error = "No Error Present"

    """
    Creates a graph given a set of verticies, edges, and values.
    """
    def addSetGraph(self, edge_dict, vertex_values_dict, mod):
        self.edge_dict.clear()
        self.edge_dict = {}
        self.vertex_values.clear()
        self.vertex_values = {}

        self.edge_dict = edge_dict
        self.vertex_values = vertex_values_dict
        self.max_vertex_value = mod

    """
    Clears out any previous values for the graph. 
    For future use.
    """
    def resetGraph(self):
        self.edge_dict = {}
        self.vertex_values = {}


    """
    Prints out an error code given a problem.
    Used for debugging purposes.
    """
    def printError(self, error_code):
        global error_dict

        temp_contains = False
        for key in error_dict:
            if key == error_code:
                temp_contains = True
                print(str(error_dict[error_code]))
        if not temp_contains:
            print("Error code does not exist")

    """
    Returns T/F depending on if the given vertex is 
    stored in the vertrx_values dictonary. 
    Used for debugging/input-checking purposes.
    """
    def containsVertexInValues(self, vertex):
        contains = False
        for key in self.vertex_values:
            if key == vertex:
                contains = True
        return contains

    """
    Returns T/F depending on if the given vertex is 
    stored in the edge_dict dictonary. 
    Used for debugging/input-checking purposes.
    """
    def containsVertexInEdgeConnectionDict(self, vertex):
        contains = False
        for key in self.edge_dict:
            if key == vertex:
                contains = True
        return contains

    """
    Returns T/F depending on if the given vertex contains 
    the given connection in the edge_dict dictonary. 
    Used for debugging purposes.
    """
    def containsConnection(self, vertex, connection):
        contains = False
        for key in self.edge_dict:
            if vertex == key:
                if connection in self.edge_dict[key]:
                    contains = True
        return contains 

    """
    Returns a string type edge list given a vertex name. 
    Used for debugging purposes.
    """
    def getConnections(self, vertex_name):
        if not self.containsVertexInEdgeConnectionDict(vertex_name) or not self.containsVertexInValues(vertex_name):
            return False

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
                return False
    
            return edgeSet
    """
    Returns a string type edge list given a vertex.  
    Contains a check for empty edge lists. 
    For future use.
    """
    def parseEdges(self, vertex_name):
        if not self.containsVertexInEdgeConnectionDict(vertex_name) or not self.containsVertexInValues(vertex_name):
            return False

        edgeList = ""
        if vertex_name in self.edge_dict:
            edges = self.edge_dict[vertex_name]
        else:
            self.printError(3)
            return

        if len(edges) == 0:
            self.printError(2)
            return edgeList
        else: 
            for edge in edges:
                edgeList = edgeList + str(edge)
            return edgeList

    """
    Saves the adjacent vertex given the starting vertex.  
    Using to add connections.
    """
    def addConnectionForeExsistingNode(self, vertex_name, adjacent_vertex):
        if not self.containsVertexInEdgeConnectionDict(vertex_name) or not self.containsVertexInValues(vertex_name) \
            or self.containsConnection(vertex_name, adjacent_vertex):
            return False
        self.edge_dict[vertex_name].append(adjacent_vertex)
        return True

    """
    Adds a vertex to both edge_list and vertex_values dictonary. 
    Will NOT add if the vertex already exists, or
    if the user gives a connection, and the connection already exsists with the vertex. 
    Returns T/F
    Using for adding a vertex. 
    """
    def addVertex(self, vertex_name, connection = "none", vertex_value = 1):
        if self.containsVertexInEdgeConnectionDict(vertex_name) or self.containsVertexInValues(vertex_name) \
            or self.containsConnection(vertex_name, connection):
            return False  

        self.vertex_values[vertex_name] = vertex_value

        if connection != "none":
            self.edge_dict[vertex_name].append(connection)
        else:
            self.edge_dict[vertex_name] = []
        return True

    """
    Removes a vertex from both edge_dict and vertex_values dictonary. 
    Returns a T/F  value based on if the vertex exists or not. 
    For future use.
    """        
    def removeVertex(self, vertex_name):
        if not self.containsVertexInEdgeConnectionDict(vertex_name) or not self.containsVertexInValues(vertex_name):
            return False
        del self.edge_dict[vertex_name]
        del self.vertex_values[vertex_name]

    """
    Edits a vertex value given the vertex name, and the new value.  
    For future use.
    """
    def editVertexValue(self, vertex_name, new_value):
        self.vertex_values[vertex_name] = (new_value) % self.max_vertex_value
        
    """
    Adds one to vertex_value based on a provided vertex. 
    ONLY for graphs that are over Z{2} ( x mod 2 = [0,1]) 
    Returns a T/F  value based on if the vertex exists or not. 
    Using to toggle. 
    """
    def addOneToVertexValue(self, vertex_name):
        if not self.containsVertexInEdgeConnectionDict(vertex_name) or not self.containsVertexInValues(vertex_name):
            return False
        self.vertex_values[vertex_name] = (self.vertex_values[vertex_name] + 1) % self.max_vertex_value  
        return True

    """
    Chnages the connection between a givn vertex.  
    Returns a T/F  value based on if the vertex/connection exists or not. 
    For future use . 
    """
    def changeConnection(self, vertex, connection_change, new_connection):
        if not self.containsConnection(vertex, connection_change) or not self.containsVertexInEdgeConnectionDict(vertex) \
            or not self.containsVertexInValues:
            return False

        for key in self.edge_dict:
            if key == vertex:
                if len(new_connection) == 0:
                    temp_connection_list = self.edge_dict[key]
                    temp_connection_list.remove(connection_change)
                    self.edge_dict[key] = temp_connection_list
                elif connection_change in self.edge_dict[key]:
                    temp_connection_list = self.edge_dict[key]
                    temp_connection_list.remove(connection_change)
                    temp_connection_list.append(new_connection)
                    self.edge_dict[key] = temp_connection_list
        return True

    """
    Retunrs a list type edge_list. 
    For future use. 
    """
    def getListOfAdjacentVerticies(self, vertex):
        list_temp = self.edge_dict[vertex]
        return list_temp

    """
    Adds one to vertex_value based on a provided vertex. 
    Toggles all adjacent verticies. 
    Returns a T/F  value based on if the vertex exists or not. 
    Using to toggle. 
    """
    def toggleVertex(self, vertex_name):
        if not self.containsVertexInEdgeConnectionDict(vertex_name) or not self.containsVertexInValues(vertex_name):
            return False
        #toggle desired vertex
        self.addOneToVertexValue(vertex_name)
        #toggle all adjacent verticies
        for edge in self.edge_dict[vertex_name]:
            self.addOneToVertexValue(edge)
        True

    """
    Sorts the entire adjacent list in ascending order. 
    For future use. 
    """
    def sortAdjList(self):
        pass

    """
    Determines is a graph is Planar (if a graph G = (V,E) can be draw without any edge crossing one-another).  
    Returns T/F. 
        Euler's formula shows that for planar graph 
        G = (V, E), |E| <= 3*|V| - 6, so every planar graph contains a linear number of edges, 
        and further, every planar graph must contain a vertex of degree at most 5.
    For future use.  
    """
    def isPlanar(self):
        #Get num of verticies
        numVerticies = len(self.vertex_values)

        #Get num of edges
        #Get highest vertex degree
        numEdges = 0
        highestDegree = 0
        for vertex in self.edge_dict:
            degreeOfCurVertex = len(self.edge_dict[vertex])
            numEdges = numEdges + degreeOfCurVertex
            if degreeOfCurVertex > highestDegree:
                highestDegree = degreeOfCurVertex

        return (numEdges <= (3 * numVerticies) - 6) and (highestDegree < 6)
            
    """
    Used to determine if a created graph is rady to play. 
        The graph must have at least 2 verticies and 1 edge
    returns T/F 
    """
    def readyToPlay(self):
        numVerticies = len(self.edge_dict)

        numEdges = 0
        for vertex in self.edge_dict:
            degreeOfCurVertex = len(self.edge_dict[vertex])
            numEdges = numEdges + degreeOfCurVertex

        return ((numVerticies >= 2) and (numEdges >= 1))

    """
    Checks the graph to see if all vertex values are 0. 
    If all are 0, the user has won the game. 
    Returns T/F
    Used to determine winner. 
    """
    def checkWinner(self):
        for key in self.vertex_values:
            if self.vertex_values[key] != 0:
                return False
        return True

    """
    Prints the graph. 
        Lists vertex --> edge list
        Lists vertex --> value
    Used for debugging.  
    """
    def printGraph(self):
        for vertex, edgeconnections in self.edge_dict.items():
            stringVertex = str(vertex)
            print(stringVertex)
            print(str(edgeconnections))
            if len(edgeconnections) == 0: #if the vertex has at least one adjacent vertex
                stringEdgeconnections = "None"
            else:
                stringEdgeconnections = ','.join(str(item) for item in edgeconnections)
            print("Vertex: " + stringVertex + " is connected to: " + stringEdgeconnections)
            

        for vertex in self.vertex_values:
            print("Vertex " + str(vertex) + " has value " + str(self.vertex_values[vertex]))

"""
Print line "done" is used to make sure the program compiles. 
Having the word "done" on the console is easier to see (assessibility).  
"""
print("done")
