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
    return adj_complement

def constPendant(adj_graph):
    """Given the graph with adjacency dictionary "adj_graph", it givse as output the adjacency dictionary for the pendant graph
associated with the graph.  In other words, it takes the graph and adds a pendant vertex to each existing vertex."""
    import copy
    adj_pendant = copy.deepcopy(adj_graph) # Initialize adjacency dictionary
    for vertex in adj_graph:
        adj_pendant[vertex].append(vertex+len(adj_graph))
        adj_pendant[vertex+len(adj_graph)]=[vertex]
    return adj_pendant

def combineComponents(graph_list):
    """Constructs a graph whose connected components are the graphs in the list "graph_list"."""
    current_graph = graph_list[0] # Set the current graph equal to the first graph in the list of connected components.
    for k in range(1,len(graph_list)): # Look through all the remaining connected components.
        interim_graph = dict() # Initialize the graph we use to adjust the vertices and add in the new graph.
        current_component = graph_list[k] # Set current_component equal to the connected component currently being worked with.
        for vertex in current_graph: # Take each vertex in the current graph with the purpose of increasing each vertex to make room for the vertices in the current component.
            new_vertex = vertex + len(current_component) # "new_vertex" is the new name for the vertex "vertex".
            interim_graph[new_vertex] = list()
            for adjacent_vertex in current_graph[vertex]: # Look at each vertex adjacent to "vertex".  We want to increase them, too.
                new_adjacent_vertex = adjacent_vertex + len(current_component) # We increase adjacent vertices to match their new identity.
                interim_graph[new_vertex].append(new_adjacent_vertex) # Change old vertices into new vertices.
        interim_graph.update(current_component) # Include the current component in the interim graph, and make this the current graph.
        current_graph = interim_graph
    return current_graph

def constCompleteGraph(num_vertices):
    """Constructs and returns the adjacency dictionary for a complete graph with "num_vertices" vertices."""
    adj_graph = initializeAdjDict(num_vertices) # Initialize the adjacency dictionary.
    for vertex in adj_graph:
        for other_vertex in adj_graph:
            if vertex != other_vertex:
                adj_graph[vertex].append(other_vertex)
    return adj_graph

def constPathGraph(num_vertices):
    """Constructs and returns the adjacency dictionary for a path graph with "num_vertices" vertices."""
    adj_graph = initializeAdjDict(num_vertices) # Initialize the adjacency dictionary.
    subPathAdj(adj_graph, 0, num_vertices - 1) # Construct a path with edges between adjacent vertices, starting at "0" and ending at "num_vertices-1".
    return adj_graph

def constDisjointPaths(num_vertices, path_list):
    """Constructs and returns the adjacency dictionary for a graph with num_vertices
whose edges form vertex-disjoint paths whose lengths given by the list "path_list"."""
    adj_dict = initializeAdjDict(num_vertices)
    current_vertex = 0 
    for length in path_list:
        subPathAdj(adj_dict, current_vertex, current_vertex + length)
        current_vertex += length + 1
    return adj_dict

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

def constWinSpider(half_num_vertices):
    legs = []
    legs.append(1) # First leg has length 1
    for leg in range(0,half_num_vertices-1):
        legs.append(2)
    return constCaterGraph([legs])

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

def dictionaryToAdjMatrix(adj_dict):
    """Converts the adjacency dictionary for either a directed or undirected graph "adj_dict" to a neighborhood matrix.  The output is
the two-dimensional array "neighbor_mat"."""
    neighbor_mat = zeroMatrix(len(adj_dict))
    for i in range(len(adj_dict)): # The remaining 1's correspond to edges or arcs in the graph.
        for j in adj_dict[i]:
            neighbor_mat[i][j] = 1
    return neighbor_mat

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

def checkZerosColumnInt(mat, pivot_row, pivot_column):
    """This function checks to see if every entry in column "pivot_column" that is at or below row "pivot_row" is zero.  This helps
us see if there is any point to doing any row operations on this column."""
    all_zero = True # We begin by assuming that all entries in column "pivot_column" at or below row "pivot_row" are zero.
    for row in range(pivot_row,len(mat)):
        if mat[row][pivot_column] != 0: # Give all_zero the value "False" if you find a nonzero value.
            all_zero = False
            break
    return all_zero # This is true if all entries in column "pivot_column" at or below row "pivot_row" are zero and false otherwise.

def reduceColumnSubtract(mat, pivot_row, pivot_column, mod_number):
    """This function takes a matrix and row reduces a given column at and below row "pivot_row" to its row reduced form.
The matrix is "mat".  The column to be reduced is "pivot_column".  The computations are done modulo "mod_number".A row switch is done so that the
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

def reduceColumnSubtractInt(mat, pivot_row, pivot_column):
    """This function takes a matrix and row reduces a given column at and below row "pivot_row" to its row reduced form in a label-neutral
way.  The matrix is "mat".  The column to be reduced is "pivot_column".  The computations are done modulo "mod_number".  A row switch is done
so that the pivot position is row "pivot_row" and column "pivot_column"."""
    num_nonzero_column = 2 # The exit condition is when there is at most one nonzero entry in the column.  We're not ready to exit yet.
    for row in range(pivot_row,len(mat)): # Look at each row at or below the pivot row.
        if mat[row][pivot_column] < 0: # Look for leading entries that are negative.
            for column in range(len(mat)): # Multiply each entry in the row by -1 to have a positive leading entry.
                mat[row][column] = -1 * mat[row][column]
    while num_nonzero_column >= 2: # If we haven't satisfied the exit condition for this column.
        for row in range(pivot_row,len(mat)): # Look at all non-zero rows at or below the pivot row.  These will be our potential pivots.
            for non_pivot_row in range(pivot_row,len(mat)): # Look at all other non-zero rows at or below the pivot row.
                if row != non_pivot_row and mat[row][pivot_column] != 0 and mat[row][pivot_column] <= mat[non_pivot_row][pivot_column]: # Only subtract if they are different rows, the pivot entry is non-zero, and the pivot entry is smaller than the non-pivot entry.
                    for k in range(len(mat)): # Subtract the pivot row from the non-pivot row, where "k" is the column.
                        mat[non_pivot_row][k] = mat[non_pivot_row][k] - mat[row][k] # Subtract pivot row from non-pivot row modulo "mod_number".
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

def reduceColumnModuloInt(mat):
    """This function takes the matrix "mat" and puts it in reduced echelon form, with all arithmetic done modulo "mod_number"."""
    pivot_row = 0 # We assume our first pivot row is 0.
    for pivot_column in range(len(mat)): # We look to row reduce every column
        if checkZerosColumnInt(mat, pivot_row, pivot_column) == False: # We first check to see if we have all zeros at or below "pivot_row".  If so, we just go to the next column, not the next row.
            reduceColumnSubtractInt(mat, pivot_row, pivot_column) # If there is a nonzero entry, we use subtraction to reduce the column.
            pivot_row += 1 # Move on to the next row and next column.

