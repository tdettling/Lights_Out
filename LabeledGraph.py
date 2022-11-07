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

import Graph

class LabeledGraph(Graph):
    """Creates a labeled graph, and includes methods that can be used in the
    Lights Out games"""
    def __init__(self, adj_dict,num_lab,vert_lab,win):
        # cardinality of label set, Cayley table, vertex labeling, have we won?
        #Graph.__init__(self,num_vert,adj_dict,edge_set)
        self.num_lab = num_lab
        self.vert_lab = vert_lab
        self.win = win
        Graph.__init__(self,Graph.num_vert,adj_dict,Graph.edge_set)
    def incrementLabelZn(self,vert):
        # Increments labels after the vertex vert is toggled in "Plus 1" LO game
        self.vert_lab[vert] = (self.vert_lab[vert] + 1) % self.num_lab
        for x in self.adj_dict[vert]:
            self.vert_lab[x] = self.vert_lab[x]+1 % self.num_lab
    def incrementGroupLabelZn(self,vert):
        # Increments labels after vertex vert is toggled in group labeling LO game with Zn labels
        for x in self.adj_dict[vert]:
            self.vert_lab[x] = self.vert_lab[x]+self.vert_lab[vert] % self.num_lab
        self.vert_lab[vert] = (self.vert_lab[vert] + self.vert_lab[vert]) % self.num_lab
