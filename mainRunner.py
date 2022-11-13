#main running file to control everthing here
'''This file is intended to run the program.
considered the controller of the program, list below commands to run'''


import GraphLightsOut
import LightsOutTrap
import MatrixReduction

#Code from GraphLightsOut
def GraphLightsOut_runner():
    labeling_list = list()
    labeling_dict = dict()
    adj_dict_digraph = dict()

    adj_dict = GraphLightsOut.constPathGraph(5)
    neighbor_mat = GraphLightsOut.dictionaryToMatrix(GraphLightsOut.constPathGraph(5))
    #matrixReduceModulo is not a method/function. 
    #reduced_mat = matrixReduceModulo(GraphLightsOut.dictionaryToMatrix(GraphLightsOut.constPathGraph(5)), 3)
    print(neighbor_mat)
    #print(reduced_mat)
    print(GraphLightsOut.decodeDirectProduct(GraphLightsOut.constCyclicGroup(2),GraphLightsOut.constCyclicGroup(3),4))

#Code from LightsOutTrap
def LightsOutTrap_runner():
    labeling_list = list()
    labeling_dict = dict()
    adj_dict_digraph = dict()

    adj_dict = LightsOutTrap.constPathGraph(5)
    neighbor_mat = GraphLightsOut.dictionaryToMatrix(LightsOutTrap.constPathGraph(5))
    #reduced_mat = GraphLightsOut.matrixReduceModulo(GraphLightsOut.dictionaryToMatrix(LightsOutTrap.constPathGraph(5)), 3)
    print(neighbor_mat)
    #print(reduced_mat)

#Code from MatrixReduction
def MatrixReduction_runner():
    adj_graph = {0:[1,5], 1:[0,2], 2:[1,3], 3:[2,4], 4:[3,5], 5:[4,0], 6:[7], 7:[6], 8:[9], 9:[8], 10:[11], 11:[10]}
    #adj_pendant = constPendant(adj_comp)
    #neighbor_mat = dictionaryToMatrix(constPathGraph(6))
    #neighbor_mat = dictionaryToMatrix(constDisjointPaths(15, [2,3,4]))
    #neighbor_mat = dictionaryToMatrix(constCompMultiGraph([2,3]))
    #neighbor_mat = dictionaryToMatrix(constCaterGraph([[1,2],[1,1,1]]))
    #neighbor_mat = dictionaryToMatrix(constTheta([2,3,4]))
    #neighbor_mat = dictionaryToMatrix(constRemoveMaximumMatching(4))
    #neighbor_mat = dictionaryToMatrix(constRemoveMaxMatchPlusOne(12))
    #adj_mat = dictionaryToAdjMatrix(adj_graph)
    my_graph = {1:[3,4,5], 2:[4,5], 3:[1,4,5], 4:[1,2,3], 5:[1,2,3]}
    neighbor_mat = MatrixReduction.dictionaryToMatrix(my_graph)
    #adj_dict = constCompMultiGraph([3,3])

    #subPathAdj(adj_dict, 0, 3)
    #subPathAdj(adj_dict, 4, 6)
    #subPathAdj(adj_dict, 7, 8)
    #print(adj_comp)
    #print(adj_pendant)
    #neighbor_mat = dictionaryToMatrix(adj_dict)
    MatrixReduction.printMatrix(neighbor_mat)
    MatrixReduction.reduceColumnModuloInt(neighbor_mat)
    MatrixReduction.printMatrix(neighbor_mat)

def main_run():
    GraphLightsOut_runner()
    LightsOutTrap_runner()
    MatrixReduction_runner()

main_run()