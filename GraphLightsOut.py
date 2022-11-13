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

import itertools
import LightsOutTrap

def initializeAdjDict(num_vertices):
    """Returns an adjacency dictionary (for directed or undirected graph) on "num_vertices" vertices, each having an empty adjacency list"""
    adj = dict()
    for x in range(0, num_vertices):
        adj[x] = []
    return adj

def constEdge(adj_graph, vertex1, vertex2):
    """Using the adjacency dictionary "adj_graph" for an undirected graph, this function puts an edge between the vertices
"vertex1" and "vertex2", if one does not exist already.  Otherwise, it does nothing."""
    if vertex2 not in adj_graph[vertex1]:
        adj_graph[vertex1].append(vertex2)
    if vertex1 not in adj_graph[vertex2]:
        adj_graph[vertex2].append(vertex1)

def removeEdge(adj_graph, vertex1, vertex2):
    """Using the adjacency dictionary "adj_graph" for an undirected graph, this function removes an existing edge between
the vertice "vertex1" and "vertex2".  If there is no edge between "vertex1" and "vertex2", the function does nothing."""
    if vertex2 in adj_graph[vertex1]:
        adj_graph[vertex1].remove(vertex2)
    if vertex1 in adj_graph[vertex2]:
        adj_graph[vertex2].remove(vertex1)

def constEdgeDigraph(adj_digraph, vertex1, vertex2):
    """Using the adjacency dictionary "adj_digraph" for a digraph, this function puts a directed edge from
"vertex1" to "vertex2"."""
    if vertex2 not in adj_digraph[vertex1]:
        adj_digraph[vertex1].append(vertex2)

def removeEdgeDigraph(adj_digraph, vertex1, vertex2):
    """Using the adjacency dictionary "adj_digraph" for a digraph, this function puts a directed edge from
"vertex1" to "vertex2"."""
    if vertex2 in adj_digraph[vertex1]:
        adj_digraph[vertex1].remove(vertex2)

def makeDigraphUndirected(adj_digraph):
    """The input "adj_digraph" is the adjacency dictionary for a directed graph.  This function outputs an adjacency dictionary for
the undirected graph obtained from "adj_digraph" by making all of its edges undirected."""
    adj_graph = adj_digraph # Start with the adjacency dictionary for the digraph.  This will contain all the edges; we just have to make the adjacency go both ways.
    for vertex in adj_digraph: # Look through all the vertices "vertex" that are in the adjacency dictionary for the digraph.
        for adj_vertex in adj_digraph[vertex]: # Look at all the vertices that are adjacent to "vertex".
            if vertex not in adj_graph[adj_vertex]: # Check to see that "vertex" is not already marked as adjacent to "adj_vertex".
                adj_graph[adj_vertex].append(vertex) # Make "vertex" adjacent to "adj_vertex".
    return adj_graph

def subPathAdj(adj_graph, start, end):
    """Puts edges in the adjacency dictionary "adj_graph" for an undirected graph that represent the edges in a subgraph that is
a path graph between consecutive vertices, starting at vertex "start" and
ending at vertex "end"."""
    if start < end: # Function only works if starting vertex is less than the ending vertex.
        for x in range(start, end): # Adds the edge {x,x+1} to both dictionary entries.
            constEdge(adj_graph, x, x + 1)
    elif start > end:
        print("Your first vertex cannot be greater than your last vertex.")

def constComplement(adj_graph):
    """Given the graph with adjacency dictionary "adj_graph", it gives as output the adjacency dictionary for the graph's complement.
In other words, a pair of vertices in the complementary matrix has an edge if and only if it is not an edge in the original graph."""
    adj_complement = initializeAdjDict(len(adj_graph))
    for vertex in adj_graph:
        for other_vertex in adj_graph:
            if other_vertex not in adj_graph[vertex] and vertex != other_vertex:
                adj_complement[vertex].append(other_vertex)

def constCompleteGraph(num_vertices):
    """Constructs and returns the adjacency dictionary for a complete graph with "num_vertices" vertices."""
    adj_graph = initializeAdjDict(num_vertices) # Initialize the adjacency dictionary.
    for vertex in adj_graph:
        for other_vertex in adj_graph:
            #if other_vertex vertex
            if vertex != other_vertex:
                adj_graph[vertex].append(other_vertex)

def constPathGraph(num_vertices):
    """Constructs and returns the adjacency dictionary for a path graph with "num_vertices" vertices."""
    adj_graph = initializeAdjDict(num_vertices) # Initialize the adjacency dictionary.
    subPathAdj(adj_graph, 0, num_vertices - 1) # Construct a path with edges between adjacent vertices, starting at "0" and ending at "num-1".
    return adj_graph

def constCycleGraph(num_vertices):
    """Constructs and returns the adjacency matrix for a cyclic graph with "num_vertices" vertices"""
    adj_graph = constPathGraph(num_vertices) # First construct a path.
    constEdge(adj_graph, 0, num_vertices - 1) # Connect beginning and end vertex.
    return adj_graph

def constWheelGraph(num_vertices):
    """Constructs and returns  the adjacency dictionary for a wheel graph with "num_vertices" vertices."""
    adj_graph = constCycleGraph(num_vertices - 1) # First construct a cycle
    adj_graph[num_vertices - 1] = []
    for vertex in range(num_vertices - 1): # For each vertex in the cycle, construct an edge between that vertex and the center vertex.
        constEdge(adj_graph, num_vertices - 1, vertex)
    return adj_graph

def constCompMultiGraph(parts):
    """Constructs and returns the adjacency dictionary for a complete multipartite graph.
The input "parts" is a list of the sizes of the parts of the partition of vertices."""
    vert = 0 # This keeps track of the number of vertices in the graph.  We start with 0.
    for x in parts:  # Uses "parts" to determine the number of vertices to add to the graph.
        vert = vert + x # This will give us the total number of vertices in the graph.
    adj_graph = initializeAdjDict(vert) # Initializes the adjacency dictionary with the proper number of vertices.
    first_vert = 0 # Represents vertex in first part.
    in_sec_vert = 0 # Represents the first vertex in the second part.
    for p in parts[:len(parts) - 1]: # This loop constructs an edge between every two vertices in different parts.
        in_sec_vert = in_sec_vert + p # Places the first vertex of the second part in the proper part.
        while first_vert < in_sec_vert:
            for sec_vert in range(in_sec_vert, vert):
                constEdge(adj_graph, first_vert, sec_vert) # Connects "first_vert" to every vertex in every part past the one "first_vert" is in.
            first_vert += 1 # Changes "first_vert" to the next vertex in the first part.
    return adj_graph

def constCaterGraph(spine):
    """Constructs adjacency matrix for a subdivided caterpillar tree.  The input
"spine" is a list whose components correspond to the spinal vertices.  Each of
these components is a list of the lengths of the legs adjacent to the given
spinal vertex.  If a spinal vertex has no legs, make its leg [0].  The
function returns the adjacency matrix, but it can be adapted to return the list
of spinal vertices and the list of all leaves of the legs as well."""
    vert = len(spine) # Count vertices on spine.
    for leg_list in spine: # Focus on the lengths of the legs on each spinal vertex.
        for leg in leg_list: # Here "leg" is the length of one of the legs of a spinal vertex.
            vert = vert + leg # Add up the vertices in each leg to find the total number of vertices in the graph.
    adj_graph = initializeAdjDict(vert) # Initializes adjacency dictionary with the proper number of vertices.
    spine_list = [] # Initializes list of spinal vertices.
    leaves = [] # Initializes list of leaves.
    spine_vert = 0 # Represents the current spinal vertex.
    spine_list.append(spine_vert) # Lists first spinal vertex.
    leg_vert = 0 # Represents the current leg vertex.
    for leg_list in spine: # Look at each list of leg lengths for the current spine vertex.
        for leg in leg_list: # Look at each leg length in the list of leg lengths  for the current spine vertex.
            if leg > 0: # Only add edges if we have a leg of positive length.
                leg_vert += 1
                constEdge(adj_graph, spine_vert, leg_vert) # Make an edge between the spinal vertex and the first vertex on the current leg.
                subPathAdj(adj_graph, leg_vert, leg_vert + leg - 1) # Construct the rest of the leg.
                leg_vert = leg_vert + leg - 1 # Keep track of the current leg vertex.
                leaves.append(leg_vert) # That last vertex was a leaf.  Record that value in the "leaves" list.
            elif leg < 0:
                print ("You have negative length for leg %d" % (leg_vert)) # Legs cannot have negative length.
        if leg_vert < vert - 1: # If the leg did not mark the end of the graph, keep going.
            constEdge(adj_graph, spine_vert, leg_vert + 1) # Make an edge between the current spinal vertex and the next spinal vertex.
            spine_vert = leg_vert + 1 # Mark this vertex as the next spinal vertex.
            spine_list.append(spine_vert) # Record the new spinal vertex in the "spine_list" list.
            leg_vert = leg_vert + 1 # The new leg vertex becomes the new spinal vertex.
    return adj_graph

def constTheta(guts):
    """Constructs adjacency dictionary for a theta graph.  The list "guts"
has the lengths of all the paths between the two end vertices."""
    vert = 2 # Counts the end vertices.
    for path_length in guts:
        vert = vert + path_length - 1 # add one less than the length of each path to the total.           
    adj_graph = initializeAdjDict(vert) # Initializes adjacency dictionary with the proper number of vertices.
    path_vert = 2 # This is the first vertex in the path that is not an end vertex.
    for path_length in guts:
        subPathAdj(adj_graph, path_vert, path_vert + path_length - 2) # Constructs the path without the end vertices.
        constEdge(adj_graph, 0, path_vert)
        constEdge(adj_graph, 1, path_vert + path_length - 2) # Connects path to the end vertices.
        path_vert += path_length - 1 # This is the first vertex on the next path between "0" and "1".
    return adj_graph

def constRemoveMaximumMatching(num_vertices):
    """Constructs adjacency dictionary for a graph obtained from the complete graph on "num_vertices" vertices by removing a
maximum perfect matching."""
    adj_graph = initializeAdjDict(num_vertices) # Initializes adjacency dictionary with the proper number of vertices.
    for x in range(0,num_vertices): # Look at all pairs of vertices in the graph.
        for y in range(x,num_vertices):
            if ((x % 2 == 1) or (x+1 != y)) and (x != y): # Constructs an edge between each even vertex and each vertex that is not its successor.
                constEdge(adj_graph, x, y)
    return adj_graph

def constRemoveMaxMatchPlusOne(num_vertices):
    """Constructs adjacency dictionary for a graph obtained from the complete graph on "num_vertices" vertices by removing a
maximum perfect matching plus one additional edge.  Note that we cannot do this unless "num_vertices" is at least 3."""
    if num_vertices < 3:
        print("You need at least 3 vertices for this graph")
        pass
    else:
        adj_graph = constRemoveMaximumMatching(num_vertices)
        removeEdge(adj_graph,0,2)
        return adj_graph

def constThreeCycleMatching(half_num_vertices):
    """Constructs a graph on an even number of vertices consisting of a 3-cycle and a maximal matching on the remaining
vertices.  Here "half_num_vertices" is half the number of vertices, which must be at least two (total number of vertices
is at least 4)."""
    num_vertices = 2 * half_num_vertices
    if num_vertices < 4:
        print("You need more vertices.")
        pass
    else:
        adj_dict = initializeAdjDict(num_vertices)
        constEdge(adj_dict, 0, 1)
        constEdge(adj_dict, 1, 2)
        constEdge(adj_dict, 0, 2) # These are for the 3-cycle.
        if num_vertices > 4:
            for x in range(3,num_vertices-2):
                if (x % 2) == 1:
                    constEdge(adj_dict, x, x+1)
        return adj_dict

def constAdjacency():
    """Allows manual construction of an adjacency dictionary.  First, you input the number of
vertices.  For each vertex, you input the adjacent vertices (one at a time).  When you are finished with the
adjacent vertices to a vertex, type in "-1" to go to the next vertex.  Do not put in loops; they will make you
cry."""
    num_vert = int(input("Here is where you make your own adjacency dictionary.  How many vertices do you want? "))
    adj_graph = initializeAdjDict(num_vert)
    for vertex in adj_graph:
        adj_vertex = -2 # We are not done (so we don't want "adj_vertex" to be -1), but we don't have an adjacent vertex to "vertex" yet (so we don't want "adj_vertex" to be nonnegative).
        while adj_vertex != -1: # The event y = -1 indicates that we are done.
            adj_vertex = int(input("What would you like to be adjacent to vertex " + str(vertex) + " ? (Input '-1' if you are done with this vertex) "))
            # Allows input of vertex "adj_vertex" to "vertex".
            if adj_vertex != -1 and adj_vertex not in adj_graph[vertex]: # Constructs the edge entered above, but only if it hasn't been constructed already.
                constEdge(adj_graph, vertex, adj_vertex)
    return adj_graph

def possibleLabelings(num_labels, num_vertices):
    """Given the number of labels "num_labels" and the number of vertices "num_vertices" of a graph, this function generates all possible
vertex labelings of the graph.  It returns a list of these labelings."""
    num_list = list(range(num_labels)) # This lists all possible labels.
    labeling_list = list(itertools.product(num_list, repeat=num_vertices))  # Generates list of tuples representing all possible labelings.
    return labeling_list

def incrementLabelZn(adj_graph, labeling, num_labels, vertex):
    """Records the result of toggling the vertex "vertex" in the generalized Lights Out
game.  The input "adj_graph" is the adjacency dictionary of the graph.  The tuple "labeling" represents the labeling of
the graph.  The integer "num_labels" is the number of possible labels.  The output will be the labeling
that results from toggling "vertex"."""
    list_labeling = list(labeling) # This converts the labeling to a list.
    for adj_vertex in adj_graph[vertex]: # Look through all vertices "adj_vertex" that are adjacent to "vertex".
        list_labeling[adj_vertex] = (list_labeling[adj_vertex] + 1) % num_labels # We add one to the label of "adj_vertex".
    list_labeling[vertex] = (list_labeling[vertex] + 1) % num_labels # We add one to the label of "vertex".
    new_labeling = tuple(list_labeling)
    return new_labeling

def incrementGroupLabelZn(adj_graph, labeling, num_labels, vertex):
    """Records the result of toggling the vertex "vertex" in the Group Labeling Lights Out
game over Z_n.  The input "adj_graph" is the adjacency dictionary of the graph.  The tuple "labeling" represents the labeling of
the graph.  The integer "num_labels" is the number of possible labels.  The output will be the labeling
that results from toggling "vertex"."""
    list_labeling = list(labeling) # This converts the labeling to a list.
    for adj_vertex in adj_graph[vertex]: # Look through all vertices "adj_vertex" that are adjacent to "vertex".
        list_labeling[adj_vertex] = (list_labeling[adj_vertex] + list_labeling[vertex]) % num_labels # We add the label of "vertex" to the label of "adj_vertex".
    list_labeling[vertex] = (list_labeling[vertex] + list_labeling[vertex]) % num_labels # We add the label of "vertex" to itself.
    new_labeling = tuple(list_labeling)
    return new_labeling

def incrementLabelCayley(adj_graph, labeling, cayley_table, vertex):
    #removed cayley_table as an input (x,y,cayley_table,z)
    """Records the result of toggling the vertex "vertex" in the Group Labeling Lights Out
game.  The input "adj_graph" is the adjacency dictionary of the graph.  The tuple "labeling" represents the labeling of
the graph.  The array "cayley_table" is the Cayley table for the graph labels.  The output will be the labeling
that results from toggling "vertex"."""
    #num_labels do not exist here
    list_labeling = list(labeling)
    num_labels = len(cayley_table)
    #num_labels = len(list_labeling) # This converts the labeling to a list.
    for adj_vertex in adj_graph[vertex]: # Look through all vertices "adj_vertex" that are adjacent to "vertex".
        #num_labels is Z_n? 
        list_labeling[adj_vertex] = (list_labeling[adj_vertex] + list_labeling[vertex]) % num_labels # We add the label of "vertex" to the label of "adj_vertex".
    list_labeling[vertex] = (list_labeling[vertex] + list_labeling[vertex]) % num_labels # We add the label of "vertex" to itself.
    new_labeling = tuple(list_labeling)
    return new_labeling

def constLabelingDigraphZn(adj_graph, num_labels):
    """Generates an adjacency dictionary for the "labeling digraph" of the undirected graph given by the adjacency
dictionary "adj_graph" and the labeling set given by "num_label" for the Multicolor Lights Out game.  The keys
are vertex labelings of the graph and the values are (adjacent) labelings obtained by toggling a vertex."""
    labeling_list = possibleLabelings(num_labels, len(adj_graph))  # Constructs a list of all possible labels.  These are the vertices of the digraph.
    adj_digraph = dict() # Initialize the adjacency dictionary for the "labeling digraph".
    for labeling in labeling_list:  # Take each labeling separately.
        adj_digraph[labeling] = list()  # Initialize the dictionary entry of "labeling" by making each value the empty list.
        for vertex, label in enumerate(labeling):  # This loop toggles every nonzero button and puts it in the value list.  Note that "vertex" represents
            # the toggled vertex, and "label" represents the label of the vertex.
            new_labeling = incrementLabelZn(adj_graph, labeling, num_labels, vertex)  # This is the labeling resulting from toggling "vertex".
            if new_labeling not in adj_digraph[labeling]:  # Check to see if the resulting labeling is already in the list
                adj_digraph[labeling].append(new_labeling)  # Append the labeling to the list if it is not already there.
    return adj_digraph

def constLabelingDigraphGroupZn(adj_graph, num_labels):
    """Generates an adjacency dictionary for the "labeling digraph" of the undirected graph given by the adjacency
dictionary "adj_graph" and the labeling set given by "num_label" for the Group Labeling Lights Out game over Z_{num_labels}.  The keys
are vertex labelings of the graph and the values are (adjacent) labelings obtained by toggling any vertices with nonzero labels"""
    labeling_list = possibleLabelings(num_labels, len(adj_graph))  # Constructs a list of all possible labels.  These are the vertices of the digraph.
    adj_digraph = dict() # Initialize the adjacency dictionary for the "labeling digraph".
    for labeling in labeling_list:  # Take each labeling separately.
        adj_digraph[labeling] = list()  # Initialize the dictionary entry of "labeling" by making each value the empty list.
        for vertex, label in enumerate(labeling):  # This loop toggles every nonzero button and puts it in the value list.  Note that "vertex" represents
            # the toggled vertex, and "label" represents the label of the vertex.
            if label != 0:  # We only toggle nonzero vertices.
                new_labeling = incrementGroupLabelZn(adj_graph, labeling, num_labels, vertex)  # This is the labeling resulting from toggling "vertex".
                if new_labeling not in adj_digraph[labeling]:  # Check to see if the resulting labeling is already in the list
                    adj_digraph[labeling].append(new_labeling)  # Append the labeling to the list if it is not already there.
    return adj_digraph

def constLabelingDigraphCayley(adj_graph, cayley_table):
    """Generates an adjacency dictionary for the "labeling digraph" of the undirected graph given by the adjacency
dictionary "adj_graph" and the labeling set given by "num_label" for the Group Labeling Lights Out game, where the
group is given by "cayley_table".  The keys
are vertex labelings of the graph and the values are (adjacent) labelings obtained by toggling any vertices with nonzero labels"""
    #num_labels does not exist here. 
    num_labels = len(cayley_table)
    labeling_list = possibleLabelings(num_labels, len(adj_graph))  # Constructs a list of all possible labels.  These are the vertices of the digraph.
    adj_digraph = dict() # Initialize the adjacency dictionary for the "labeling digraph".
    for labeling in labeling_list:  # Take each labeling separately.
        adj_digraph[labeling] = list()  # Initialize the dictionary entry of "labeling" by making each value the empty list.
        for vertex, label in enumerate(labeling):  # This loop toggles every nonzero button and puts it in the value list.  Note that "vertex" represents
            # the toggled vertex, and "label" represents the label of the vertex.
            if label != 0:  # We only toggle nonzero vertices.
                new_labeling = incrementLabelCayley(adj_graph, labeling, cayley_table, vertex)  # This is the labeling resulting from toggling "vertex".
                if new_labeling not in adj_digraph[labeling]:  # Check to see if the resulting labeling is already in the list
                    adj_digraph[labeling].append(new_labeling)  # Append the labeling to the list if it is not already there.
    return adj_digraph

def markFalse(adj_digraph):
    """Returns a dictionary whose keys are the keys of the adjacency dictionary "adj_digraph" for a digraph and
whose values are "false". These boolean values are used to keep track of the vertices that have been placed
in weakly connected components of the digraph."""
    labeling_dict = dict()
    for labeling in adj_digraph:
        labeling_dict[labeling] = False
    return labeling_dict

def findFalseVertex(vertex_dict):
    """The input is the dictionary "vertex_dict", whose keys are the vertices (labelings) of a digraph
and whose values are boolean.  A boolean value is "true" if the vertex (labeling) has been placed in a
connected component of the digraph, and the value is "false" otherwise.
The function returns either a vertex whose value is "false" or returns the value "true"
if all vertices have "true" values."""
    vertices = True # We begin optimistically by assuming that all vertices are "true", so all vertices have been placed in components.
    for vertex in vertex_dict: # We begin our search for a "false" vertex
        if vertex_dict[vertex] is False: # Yea!  We found a "false" vertex!
            false_vertex = vertex
            vertices = False # I guess not all vertices are "false" after all.
            break # Stop the loop since the search for a "false" label is over.
    if vertices is False:
        return false_vertex
    else:
        return True

def constDownstream(adj_digraph, source_vertex):
    """A function that takes in the adjacency dictionary "adj_digraph" for a digraph and a particular
vertex "source_vertex" in the digraph.  The output is a list containing "source_vertex" and all vertices "downstream"
from "source_vertex" (i.e. all vertices that are at the end of a directed path beginning with "source_vertex")."""
    stream_list = [source_vertex] # This will be the list of our "downstream" vertices.  Start with "source_vertex".
    recently_added = [source_vertex] # This will be a list of vertices most recently added to "stream_list".
    done = False # We are not done yet.
    while done is False: # We only want to continue searching for vertices when we are not done.
        done = True # We start out by optimistically assuming that we are done.
        vertex_temp = recently_added # Make a temporary list of vertices so we can put adjacent vertices into both "stream_list" and "recently_added".
        recently_added = list() # Clear "recently_added" to make room for new vertices.
        for vertex in vertex_temp: # We consider each recently added vertex.
            for adj_vertex in adj_digraph[vertex]: # We search for vertices adjacent to "vertex".
                if adj_vertex not in stream_list: # We add the adjacent vertex "adj_vertex" to "stream_list" if it is not there already
                    stream_list.append(adj_vertex)
                    recently_added.append(adj_vertex) # We add the adjacent vertex to "recently_added" for the next round.
                    done = False # If we have added a vertex to the list, we are not yet done.
    return stream_list
    
def findTrueVertex(vertex_list, vertex_dict):
    """Takes as inputs a list "vertex_list" of vertices in a digraph.  The input "vertex_dict" is
a dictionary whose keys are vertices and whose values are boolean values. If possible, the function
returns a vertex from "vertex_list" whose value is "true". Otherwise, it returns a value of "false".
In practical terms, "vertex_list" is a list of vertices in the same weakly connected component of
the digraph.  The function returns a vertex in the list that has appeared in a previously initialized
weakly connected component."""
    appeared = False # We begin by assuming temporarily that all vertices are false.
    for vertex in vertex_list: # We search through all labelings in the list.
        if vertex_dict[vertex] is True:
            appeared = True # If we find a true vertex, "appeared" becomes true.
            true_vertex = vertex # This is our "true" vertex.
            break
    if appeared is True:
        return true_vertex # Return the labeling whose value is "true".
    else:
        return False # Return "false" if there is no "true" labeling.
      
def constComponentList(adj_digraph, target_vertex):
    """This function takes as input an adjacency dictionary "adj_digraph" for a digraph.
The function returns a list of two items.  The first item is a list of the weakly connected components.
Each weakly connected component is represented by a list of its vertices.  The second item is an integer
that represents the weakly connected component containing the vertex "target_vertex"."""
    component_list = list() # This will be the list of weakly connected components.
    vertex_dict = markFalse(adj_digraph) # This is a dictionary that indicates which vertices have been placed in components.
    done = False # Sadly, we are not done yet.
    while done is False:  # We iterate through the while loop until all components have been constructed.
        new_vertex = findFalseVertex(vertex_dict)  # Find a vertex in "vertex_dict" that has not yet been placed in a component.
        if new_vertex is True:  # This means that all labelings have been placed in a component.
            done = True  # Yea!  We are done!  While loop ends.
        else:  # In this case, "new_vertex" is a vertex that has not yet been placed in a component.
            downstream_list = constDownstream(adj_digraph, new_vertex)  # Constructs a list of all vertices "downstream" from "new_vertex".
            true_vertex = findTrueVertex(downstream_list, vertex_dict)  # Determines whether any vertices in "downstream_list" have
            # been placed in a component.
            if true_vertex is False: # In this case, no vertices in "downstream_list" have been placed in a component.
                component_list.append(downstream_list)  # Make "downstream_list" the start of a new component.
                for vertex in downstream_list:  
                    vertex_dict[vertex] = True # Mark each vertex in "downstream_list" as "true" (i.e. it has been placed in a component).
            else:  # In this case, "true_vert" is a vertex that has previously been placed in a component.
                for index, component in enumerate(component_list):  # Look through each component for "true_vertex"
                    if true_vertex in component: # In this case, we found the component that contains "true_vertex".
                            for vertex in downstream_list:
                                if vertex_dict[vertex] is False: # Look only for labelings in "downstream_list" not already in the component.
                                    component_list[index].append(vertex) # Put "vertex" in the component.
                                    vertex_dict[vertex] = True  # Mark "vertex" as having been placed in a component.
    for index, component in enumerate(component_list): # Look through all components, keeping track of their indices.
        if target_vertex in component: # In this case, we found the component that "target_vertex" is in.
            target_component = index # This is index of our desired component.
            break
    return [component_list, target_component]


def findTrap(adj_digraph, target_vertex, target_component):
    """The input "adj_digraph" is the adjacency dictionary of a digraph.  The list "component list" is the list of
(weakly) connected components of the the digraph. The integer "zero_component" is a specific vertex of the digraph,
and "zero_component" is the index of the connected component containing "zero_vertex". The function determines whether
or not there is a directed path between every vertex in "zero_component" and "zero_vertex".  The function returns a
list of all vertices that cannot be the beginning of a directed path ending in "zero_vertex" (if it exists).
If no such vertex exists, the function returns "false".  In practical terms, The function determines whether or not every labeling
is winnable in the component containing the labeling where every vertex has label zero."""
    trap_verts = list() # This is a list that will house all non-winnable vertices.
    for vertex in target_component: # Search through all vertices in the connected component.
        if target_vertex not in constDownstream(adj_digraph, vertex): # In this case, there is no path between "vertex" and "zero_vertex".
            trap_verts.append(vertex) # Add "vertex" to our list of non-winnable vertices.
    return trap_verts

def componentCardinality(component_list):
    """Takes a list of connected components of a digraph (where each component is given as an adjacency dictionary),
and determines the cardinality of each list.  If all connected components are the same cardinality, the function returns that
number.  Otherwise, the function lists the cardinalities of all the connected components."""
    cardinality_list = list()  # initiates a list of the cardinalities of the connected components.
    for component in component_list:  # loop through every connected component
        cardinality_list.append(len(component))  # appending the length of the class
    if all(x == cardinality_list[0] for x in cardinality_list):  # checking whether length of a component is equal
        # to the length of the first one
        return cardinality_list[0]  # returns size of the component classes if they are all the same
    else:
        return cardinality_list  # return size_list if something is wrong

def componentMatch(fixed_labeling, fixed_component, zero_component, num_labels):
    """The labeling "fixed_labeling" is in the weakly connected component given by "fixed_component".  This
function subtracts "fixed_labeling" (as a vector) from every labeling in ``fixed_component".  The
resulting list is then compared to the weakly connected component "zero_component" to see if it matches it.
Returns "true" if there is a match and "false" otherwise."""
    new_list = list() # This will become the list we get by adding "fixed_labeling" to every labeling in the component.
    for labeling in fixed_component: # Take each labeling in the component.
        comparison_labeling_list = list() # We will initially make the labeling a list.
        for index, label in enumerate(labeling):
            comparison_labeling_list.append((label - fixed_labeling[index]) % num_labels) # Subtract "fixed_labeling" from it.
        comparison_labeling = tuple(comparison_labeling_list) # Turn the labeling back into a tuple.
    new_list.append(comparison_labeling)
    for labeling in new_list:
        if labeling in zero_component: # We check to see if each element of "new_list" is also in "zero_component".
            match = True # This indicates that it can still be a match.
        else:
            match = False # This happens when we do not have a match.
            break
    return match # This will be "true" if there is a match and "false" otherwise.

def determineParity(labeling):
    """Given the labeling "labeling", this function determines for each vertex in the labeling whether or not all the
labels are even.  If yes, then the function returns "0".  If not, the function returns "1"."""
    parity = 0
    for x in labeling:
        if x % 2 == 1:
            parity = 1
            break
    return parity

def parityLabelDigraph(adj_digraph):
    """The input "adj_digraph" is the adjacency dictionary for a Lights Out labeling digraph, which means all keys are vertex
labelings and all values are lists of vertex labelings.  This function creates a dictionary whose keys are the labelings and
whose values are "0" if the labeling is even and "1" if the labeling is not even."""
    parity_dict = dict()
    for labeling in adj_digraph:
        parity_dict[labeling] = determineParity(labeling)
    return parity_dict

def findEvenDetours(adj_digraph, even_vertex1, even_vertex2):
    """Given two vertices "even_vertex1" and "even_vertex2" in the digraph, the function finds, if possible, an undirected path
beween "even_vertex1" and "even_vertex2" consisting of even vertices."""
    pass

def zeroMatrix(num_row_col):
    """Creates a "num_row_col x num_row_col" matrix of zeros."""
    matrix = [[0 for x in range(num_row_col)] for y in range(num_row_col)]
    return matrix

def printMatrix(mat):
    """Prints a matrix so that it looks like a matrix, with columns and rows printed in a natural way.  Puts an extra blank row at the end in case
you want to print more than one matrix."""
    for row in range(len(mat)):
        print(mat[row])
    print("")

def dictionaryToMatrix(adj_dict):
    """Converts the adjacency dictionary for either a directed or undirected graph "adj_dict" to a neighborhood matrix.  The output is
the two-dimensional array "neighbor_mat"."""
    neighbor_mat = zeroMatrix(len(adj_dict))
    for i in range(len(adj_dict)):  # All diagonal entries on a neighborhood matrix are 1.
        neighbor_mat[i][i] = 1
    for i in range(len(adj_dict)): # The remaining 1's correspond to edges or arcs in the graph.
        for j in adj_dict[i]:
            neighbor_mat[i][j] = 1
    return neighbor_mat

def moveRowDown(mat, row_from, row_to):
    """Moves row "row_from" to row "row_to" of matrix, and shifts all rows between "row_from" (not inclusive) and "row_to"
(inclusive) up one row. Note that "row_from" must be less than "row_to", or this won't work."""
    if row_from > row_to:
        print("You cannot move a row up.  Try again.")
    else:
        temp_row = mat[row_from] # Place the row you are moving down place it in temporary storage.
        for j in range(row_from, row_to):
            mat[j] = mat[j+1] # Move everything up a row between "row_from" and "row_to".
        mat[row_to] = temp_row # Now it is safe to move "row_from" to "row_to".

def moveRowUp(mat, row_from, row_to):
    """Moves row "row_from" to row "row_to" of matrix, and shifts all rows between "row_from" (not inclusive) and "row_to"
(inclusive) up one row. Note that "row_from" must be greater than "row_to", or this won't work."""
    if row_from < row_to:
        print("You cannot move a row down.  Try again.")
    else:
        temp_row = mat[row_from] # Place the row you are moving down place it in temporary storage.
        for j in range(row_from, row_to, -1):
            mat[j] = mat[j-1] # Move everything down a row between "row_from" and "row_to".
        mat[row_to] = temp_row # Now it is safe to move "row_from" to "row_to".

def findInverse(num, mod_number):
    """Given a number "num", this function determines its inverse modulo "mod_number", if it exists.  If the inverse exists, the
function returns the inverse.  Otherwise, the function returns the boolean value "False"."""
    inverse = 0
    for i in range(1,mod_number):
        if (num * i) % mod_number == 1:
            inverse = i
            break
    if inverse == 0:
        return False
    else:
        return inverse

def checkZerosColumn(mat, pivot_row, pivot_column, mod_number):
    """This function checks to see if every entry in column "pivot_column" that is at or below row "pivot_row" is zero.  This helps
us see if there is any point to doing any row operations on this column."""
    all_zero = True # We begin by assuming that all entries in column "pivot_column" at or below row "pivot_row" are zero.
    for row in range(pivot_row,len(mat)):
        if (mat[row][pivot_column] % mod_number) != 0: # Give all_zero the value "False" if you find a nonzero value.
            all_zero = False
            break
    return all_zero # This is true if all entries in column "pivot_column" at or below row "pivot_row" are zero and false otherwise.

def reduceColumnSubtract(mat, pivot_row, pivot_column, mod_number):
    """This function takes a matrix and row reduces a given column at and below row "pivot_row" to its row reduced form.  The matrix
is "mat".  The column to be reduced is "pivot_column".  The computations are done modulo "mod_number".A row switch is done so that the
pivot position is row "pivot_row" and column "pivot_column"."""
    num_nonzero_column = 2 # The exit condition is when there is at most one nonzero entry in the column.  We're not ready to exit yet.
    while num_nonzero_column >= 2: # If we haven't satisfied the exit condition for this column.
        for row in range(pivot_row,len(mat)): # Look at all non-zero rows at or below the pivot row.  These will be our potential pivots.
            for non_pivot_row in range(pivot_row,len(mat)): # Look at all other non-zero rows at or below the pivot row.
                if row != non_pivot_row and mat[row][pivot_column] != 0 and mat[row][pivot_column] <= mat[non_pivot_row][pivot_column]: # Only subtract if they are different rows, the pivot entry is non-zero, and the pivot entry is smaller than the non-pivot entry.
                    for k in range(len(mat)): # Subtract the pivot row from the non-pivot row, where "k" is the column.
                        mat[non_pivot_row][k] = (mat[non_pivot_row][k] - mat[row][k]) % mod_number # Subtract pivot row from non-pivot row modulo "mod_number".
        num_nonzero_column = 0 # Start by assuming all entries  at or below the pivot row in pivot_column are zero.
        for row in range(pivot_row,len(mat)):
            if mat[row][pivot_column] != 0:
                num_nonzero_column += 1 # Add one for every nonzero entry in the column.  If this ends up being at least 2, we start the while loop again.
    for row in range(pivot_row,len(mat)):
        if mat[row][pivot_column] != 0: # Look for the nonzero entry in "pivot_column" and at or below "pivot_row".
            moveRowUp(mat, row, pivot_row) # Move  the nonzero entry (and the rest of the row) up to "pivot_row".
            break

def normalizePivotRow(mat, pivot_row, pivot_column, mod_number):
    """This function determines if row "pivot_row", column "pivot_column" is a true pivot position.  If it is a pivot position, the
function multiplies each entry of row "pivot_row" by the multiplicative inverse of the leading entry.  Otherwise, the function does nothing."""
    factor = findInverse(mat[pivot_row][pivot_column], mod_number)
    for column in range(len(mat)):
        mat[pivot_row][column] = (factor * mat[pivot_row][column]) % mod_number

def clearPivotColumn(mat, pivot_row, pivot_column, mod_number):
    """If the matrix "mat" has a 1 in row "pivot_row" and column "pivot_column", this function does row operations to
make all other entries in the column equal to zero."""
    for row in range(len(mat)): # Look at all columns.
        if row != pivot_row: # Only put a zero in a row that is not the pivot row.
            for column in range(len(mat)): # Apply the row operation to the entire row.
                mat[row][column] = mat[row][column] - (mat[pivot_row][column] * mat[row][pivot_column])  # Multiply the pivot row by the entry in the pivot column to cancel out the entry in the pivot column and row.

def reduceColumnModulo(mat, mod_number):
    """This function takes the matrix "mat" and puts it in reduced echelon form, with all arithmetic done modulo "mod_number"."""
    pivot_row = 0 # We assume our first pivot row is 0.
    for pivot_column in range(len(mat)): # We look to row reduce every column
        if checkZerosColumn(mat, pivot_row, pivot_column, mod_number) == False: # We first check to see if we have all zeros at or below "pivot_row".  If so, we just go to the next column, not the next row.
            reduceColumnSubtract(mat, pivot_row, pivot_column, mod_number) # If there is a nonzero entry, we use subtraction to reduce the column.
            if findInverse(mat[pivot_row][pivot_column], mod_number) != False: # "!= False" means that this is a true pivot position.
                normalizePivotRow(mat, pivot_row, pivot_column, mod_number) # This means that we can normalize the pivot row.
                clearPivotColumn(mat, pivot_row, pivot_column, mod_number) # We can use the resulting normalization to make every other entry in the column zero.
            pivot_row += 1 # Move on to the next row and next column.
      
def createFile(name, adj_graph, num_labels):
    """From the adjacency dictionary of an undirected graph, this function will create a text file with the following information:
(1) The string "name", which is the name of the graph, as well as the number of vertices.
(2) The weakly connected components of the "labeling digraph".
(3) The number of weakly connected components.
(4) The cardinality (or cardinalities) of the connected components.
(5) Whether or not there are any unwinnable labelings in the connected component containing the labeling with all zeros.
(6) Whether or not Vasily's Conjecture holds for the connected components (i.e. whether or not subtracting a fixed labeling from
all labelings in its connected component gives us the zero component).  Any components that are counterexamples to Vasily's
Conjecture are written to the file."""
    num_vertices = len(adj_graph) # This is the number of vertices in the undirected graph.
    labeling_list = possibleLabelings(num_labels, num_vertices) # This is the set of all possible vertex labelings.
    adj_digraph = LightsOutTrap.constLabelingDigraph(adj_graph, num_labels) # This is the "labeling digraph" of the graph.
    zero_labeling = labeling_list[0] # This will be our labeling with all zeros.
    component_info = constComponentList(adj_digraph, zero_labeling) # This generates the weakly connected components and the index of the component containing "zero_labeling".
    component_list = component_info[0] # This is the list of weakly connected components.
    components_size = componentCardinality(component_list) # This gives us the cardinalities of the weakly connected components.
    zero_component = component_list[component_info[1]] # This is the component containing the zero labeling.
    traps = findTrap(adj_digraph, zero_labeling, zero_component) # This is a list of all unwinnable labelings in the zero component.
    my_file = open('Graph' + str(name) + 'Labels' + str(num_labels), 'w') # The name of our file will be the name of the graph and the number of labels.
    my_file.write('Graph: ' + name + '\n') # Write in the name of the graph.
    my_file.write('Number of Labels: ' + str(num_labels) + '\n') # Write in the number of labels.
    for component in component_list:
        my_file.write(str(component) + '\n') # Write in the vertices of each weakly connected component, separated by a carriage return.
    my_file.write('Number of Components: ' + str(len(component_list)) + '\n')
    if isinstance(components_size, list) is True:
        my_file.write('Cardinalities of All Components: ' + '\n' + str(components_size)+ '\n') # Writes in all cardinalities of components if some are different.
    else:
        my_file.write('Cardinality of Each Component: ' + str(components_size) + '\n')
    if len(traps) == 0: # An empty list for "traps" means no unwinngable labelings.
        my_file.write('There are no unwinnable labelings in the zero component.' + '\n')
    else:
        my_file.write('Unwinnable Labelings in Zero Component: ' + str(traps) + '\n')
    counterexamples = list() # This is a list of counterexamples to Vasily's Conjecture.
    for component in component_list: # We need to check each component to see if the conjecture is true or false.
        for labeling in component: # We need to check each labeling to see whether or not they all work.
            match = componentMatch(labeling, component, zero_component, num_labels) # This checks for a match.
            if match is False:
                counterexamples.append(component) # If match is "false", "component" is included in the list of counterexamples.
                break # Once we find one counterexample in the component, there is no need to search for more.  Skip to the next component.
    if len(counterexamples) == 0:
        my_file.write('Vasily\'s Conjecture is True for this graph' + '\n')
    else:
        my_file.write('Vasily\'s Conjecture is False for this graph.  Here are the components that are counterexamples:' + '\n')
        for component in counterexamples:
            my_file.write(str(component) + '\n')
    my_file.close()

def constCyclicGroup(num_elts):
    """Constructs a cyclic group of order n."""
    result = zeroMatrix(num_elts)
    for x in range(num_elts):
        for y in range(num_elts):
            result[x][y] = (x + y) % num_elts
    return result

def constDirectProduct(cayley1, cayley2):
    """Constructs the direct product of the groups with Cayley tables cayley1 and
cayley2.  The ordered pair (m,n) is represented by the integer len(C2)*m + n.  Returns a
list whose components are the cardinality of the group and the Cayley matrix."""
    #c1 and c2 are meant to be cayley1 and cayley2 correct?
    num = len(cayley1) * len(cayley2)
    cayley = zeroMatrix(num)
    for x in range(len(cayley1)): # Compute (x,y)*(r,s) = (xr,ys)
        for y in range(len(cayley2)):
            for r in range(len(cayley1)):
                for s in range(len(cayley2)):
                    cayley[len(cayley2) * x + y][len(cayley2) * r + s] = len(cayley2) * cayley2[x][r] + cayley2[y][s]
    return [num, cayley]

def decodeDirectProduct(cayley1, cayley2, elt):
    """Converts the element "elt" of the direct product G1xG2, where G1 has
Cayley table cayley1 and G2 has Cayley table cayley, to an ordered pair."""
    y = elt % len(cayley2)
    x = int((elt - y) / len(cayley2))
    return [x,y]

def constWreathProduct(cayley1, cayley2):
    pass

def constSymmetric(num_letters):
    pass

def constAlternating(num_letters):
    pass

def constDihedral(num_elts):
    pass

def constCayley():
    """Allows manual construction of the Cayley table for a group (or other algebraic structure with a single
binary operation).  First, you input the number of elements in the group.  For each pair of group elements, you
input the result of multiplying them (in order)."""
    num_vert = int(input("Here is where you make your own adjacency dictionary.  How many vertices do you want? "))
    adj_graph = initializeAdjDict(num_vert)
    for vertex in adj_graph:
        adj_vertex = -2 # We are not done (so we don't want "adj_vertex" to be -1), but we don't have an adjacent vertex to "vertex" yet (so we don't want "adj_vertex" to be nonnegative).
        while adj_vertex != -1: # The event y = -1 indicates that we are done.
            adj_vertex = int(input("What would you like to be adjacent to vertex " + str(vertex) + " ? (Input '-1' if you are done with this vertex) "))
            # Allows input of vertex "adj_vertex" to "vertex".
            if adj_vertex != -1 and adj_vertex not in adj_graph[vertex]: # Constructs the edge entered above, but only if it hasn't been constructed already.
                constEdge(adj_graph, vertex, adj_vertex)
    return adj_graph
