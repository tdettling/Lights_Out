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
tells us if the "Lights Out" game has been won.

Groups are represented by integers starting at zero.  The group structure is
stored in a Cayley table (matrix)."""

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

class LabeledGraph(Graph):
    """Creates a labeled graph, and includes methods that can be used in the
    Lights Out games"""
    def __init__(adj_dict,num_lab,vert_lab,win):
        # cardinality of label set, Cayley table, vertex labeling, have we won?
        Graph.__init__(self,num_vert,adj_dict,edge_set)
        self.num_lab = num_lab
        self.vert_lab = vert_lab
        self.win = win
    def incrementLabelZn(self,vert):
        # Increments labels after the vertex vert is toggled in "Plus 1" LO game
        self.vert_lab[vert] = (self.vert_lab[vert] + 1) % self.num_lab
        for x in self.adj_dict[vert]:
            self.vert_lab[x] = self.vert_lab[x]+1 % self.num_lab
    def incrementGroupLabelZn(self,vert):
        # Increments labels after vertex vert is toggled in group labeling LO game with Zn labels
        for x in adj_dict[vert]:
            self.vert_lab[x] = self.vert_lab[x]+self.vert_lab[vert] % self.num_lab
        self.vert_lab[vert] = (self.vert_lab[vert] + self.vert_lab[vert]) % self.num_lab        

class Group(object):
    """Creates a group describing number of elements and Cayley table.  Includes
    methods to construct Cayley tables, multiply elements, and construct common groups"""
    def __init__(self,num_elements,cayley):
        #Number of elements and Cayley table
        self.num_elements = num_elements
        self.cayley = cayley

    def printCayley(self):
        for row in self.cayley:
            print (row)
            
    def mult(self,x,y):
        #For group elements x and y, computes the product xy
        return self.cayley[x][y]
    
    def constCayley(self):
        #Allows manual construction of a Cayley table
        pass
    def constSymmetric(self,n):
        #Constructs the symmetric group on n letters
        pass
    def constAlternating(self,n):
        #Constructs the alternating group on n letters
        pass
    def constDihedral(self,n):
        #Constructs the dihedral group D_n of order 2n
        pass
    
    def constWreathProduct(self,C1,C2):
        #Constructs the wreath product of the groups with Cayley tables C1 and C2
        pass

print (decodeDirectProduct(constCyclicGroup(2),constCyclicGroup(3),4))
