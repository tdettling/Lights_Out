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

class Graph(object):
    """Creates a graph, describing the number of vertices (num_vert) as well as
        the edges (adj_mat or edge_set)"""
    def __init__(self, adj_dict):
        # number of vertices, adjacency matrix, edge set
        self.adj_dict = adj_dict
        
    def printAdjacency(self):
        for vert in self.adj_dict:
            print (vert)
    
    def checkAdjacency(self):
        # checks consistency of adjacency matrix
        result = True
        for x in self.adj.dict:
            for vert in self.adj.dict[x]:
                if vert not in self.adj.dict:
                    result = False
                    print ("Vertex " + str(vert) + " is adjacent to " + str(x) + " but is not a key.")
                    break
                if x not in self.adj.dict[vert]:
                    result = False
                    print ("Vertex " + str(x) + " is missing from key " + str(vert) + ".")
        for x in self.adj.dict:
                if x in self.adj_dict[x]:
                    result = False
                    print ("You have a loop on vertex" + str(x) + ".")
        return result
