''''Groups are represented by integers starting at zero.  The group structure is
stored in a Cayley table (matrix).'''
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
