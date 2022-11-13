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
import logic.GraphLightsOut as GraphLightsOut 

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
#FIXME 
def constCompleteGraph(num_vertices):
    """Constructs and returns the adjacency dictionary for a complete graph with "num_vertices" vertices."""
    adj_graph = initializeAdjDict(num_vertices) # Initialize the adjacency dictionary.
    for vertex in adj_graph:
        for other_vertex in adj_graph:
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

def parityLabelDigraph(adj_digraph):
    """The input "adj_digraph" is the adjacency dictionary for a Lights Out labeling digraph, which means all keys are vertex
labelings and all values are lists of vertex labelings.  This function creates a dictionary whose keys are the labelings and
whose values are "0" if the labeling is even and "1" if the labeling is not even."""
    parity_dict = dict() # Start with an empty parity dictionary.
    for labeling in adj_digraph: # Look through each labeling in the dictionary.
        parity_dict[labeling] = 0 # Start by assuming the labeling is even
        for label in labeling: # Look through each label in the labeling for odd labels.
            if label % 2 == 1: # If we find an odd label,
                parity_dict[labeling] = 1 # we change the parity dictionary to 1.
                break # Once we find an odd label, it is pointless to continue.
    return parity_dict

def findEvenDetours(adj_digraph, even_vertex1, even_vertex2):
    """Given two vertices "even_vertex1" and "even_vertex2" in the digraph, the function finds, if possible, an undirected path
beween "even_vertex1" and "even_vertex2" consisting of even vertices."""
    pass
      
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
    #is this supposed to be constLabelingDiagraphGroupZn()?
    adj_digraph = constLabelingDigraphGroupZn(adj_graph, num_labels) # This is the "labeling digraph" of the graph.
    zero_labeling = labeling_list[0] # This will be our labeling with all zeros.
    component_info = constComponentList(adj_digraph, zero_labeling) # This generates the weakly connected components and the index of the component containing "zero_labeling".
    component_list = component_info[0] # This is the list of weakly connected components.
    components_size = componentCardinality(component_list) # This gives us the cardinalities of the weakly connected components.
    zero_component = component_list[component_info[1]] # This is the component containing the zero labeling.
    traps = GraphLightsOut.findTrap(adj_digraph, zero_labeling, zero_component) # This is a list of all unwinnable labelings in the zero component.
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
            match = GraphLightsOut.componentMatch(labeling, component, zero_component, num_labels) # This checks for a match.
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

