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

def constWheelGraph(num_vertices):
    """Constructs and returns  the adjacency dictionary for a wheel graph with "num_vertices" vertices."""
    adj_graph = LightsOutTrap.constCycleGraph(num_vertices - 1) # First construct a cycle
    adj_graph[num_vertices - 1] = []
    for vertex in range(num_vertices - 1): # For each vertex in the cycle, construct an edge between that vertex and the center vertex.
        LightsOutTrap.constEdge(adj_graph, num_vertices - 1, vertex)
    return adj_graph

def constRemoveMaximumMatching(num_vertices):
    """Constructs adjacency dictionary for a graph obtained from the complete graph on "num_vertices" vertices by removing a
maximum perfect matching."""
    adj_graph = LightsOutTrap.initializeAdjDict(num_vertices) # Initializes adjacency dictionary with the proper number of vertices.
    for x in range(0,num_vertices): # Look at all pairs of vertices in the graph.
        for y in range(x,num_vertices):
            if ((x % 2 == 1) or (x+1 != y)) and (x != y): # Constructs an edge between each even vertex and each vertex that is not its successor.
                LightsOutTrap.constEdge(adj_graph, x, y)
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
        adj_dict = LightsOutTrap.initializeAdjDict(num_vertices)
        LightsOutTrap.constEdge(adj_dict, 0, 1)
        LightsOutTrap.constEdge(adj_dict, 1, 2)
        LightsOutTrap.constEdge(adj_dict, 0, 2) # These are for the 3-cycle.
        if num_vertices > 4:
            for x in range(3,num_vertices-2):
                if (x % 2) == 1:
                    LightsOutTrap.constEdge(adj_dict, x, x+1)
        return adj_dict

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
    labeling_list = LightsOutTrap.possibleLabelings(num_labels, len(adj_graph))  # Constructs a list of all possible labels.  These are the vertices of the digraph.
    adj_digraph = dict() # Initialize the adjacency dictionary for the "labeling digraph".
    for labeling in labeling_list:  # Take each labeling separately.
        adj_digraph[labeling] = list()  # Initialize the dictionary entry of "labeling" by making each value the empty list.
        for vertex, label in enumerate(labeling):  # This loop toggles every nonzero button and puts it in the value list.  Note that "vertex" represents
            # the toggled vertex, and "label" represents the label of the vertex.
            new_labeling = incrementLabelZn(adj_graph, labeling, num_labels, vertex)  # This is the labeling resulting from toggling "vertex".
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
    labeling_list = LightsOutTrap.possibleLabelings(num_labels, len(adj_graph))  # Constructs a list of all possible labels.  These are the vertices of the digraph.
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

def printMatrix(mat):
    """Prints a matrix so that it looks like a matrix, with columns and rows printed in a natural way.  Puts an extra blank row at the end in case
you want to print more than one matrix."""
    for row in range(len(mat)):
        print(mat[row])
    print("")

def dictionaryToMatrix(adj_dict):
    """Converts the adjacency dictionary for either a directed or undirected graph "adj_dict" to a neighborhood matrix.  The output is
the two-dimensional array "neighbor_mat"."""
    neighbor_mat = LightsOutTrap.zeroMatrix(len(adj_dict))
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
      

def constCyclicGroup(num_elts):
    """Constructs a cyclic group of order n."""
    result = LightsOutTrap.zeroMatrix(num_elts)
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
    cayley = LightsOutTrap.zeroMatrix(num)
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


def constCayley():
    """Allows manual construction of the Cayley table for a group (or other algebraic structure with a single
binary operation).  First, you input the number of elements in the group.  For each pair of group elements, you
input the result of multiplying them (in order)."""
    num_vert = int(input("Here is where you make your own adjacency dictionary.  How many vertices do you want? "))
    adj_graph = LightsOutTrap.initializeAdjDict(num_vert)
    for vertex in adj_graph:
        adj_vertex = -2 # We are not done (so we don't want "adj_vertex" to be -1), but we don't have an adjacent vertex to "vertex" yet (so we don't want "adj_vertex" to be nonnegative).
        while adj_vertex != -1: # The event y = -1 indicates that we are done.
            adj_vertex = int(input("What would you like to be adjacent to vertex " + str(vertex) + " ? (Input '-1' if you are done with this vertex) "))
            # Allows input of vertex "adj_vertex" to "vertex".
            if adj_vertex != -1 and adj_vertex not in adj_graph[vertex]: # Constructs the edge entered above, but only if it hasn't been constructed already.
                LightsOutTrap.constEdge(adj_graph, vertex, adj_vertex)
    return adj_graph
