import unittest
from Graph import Graph
import PreLoadedGraphs

global testGraphs
testGraphs = [PreLoadedGraphs.createOptionOne(), PreLoadedGraphs.createOptionTwo(), \
              PreLoadedGraphs.createOptionThree(), PreLoadedGraphs.createOptionFour(), \
              PreLoadedGraphs.createOptionFive(), PreLoadedGraphs.createOptionSix(), \
              PreLoadedGraphs.createOptionSeven(), PreLoadedGraphs.createOptionEight(), 
              PreLoadedGraphs.createOptionNine(), PreLoadedGraphs.createOptionTen()]

class TestGraph(unittest.TestCase):

    def test_geenral(self):
        g = Graph(2)
        g.addVertex("D", 'A', 0)
        print("test a graph: ")
        g.printGraph()
        self.assertTrue(g.containsVertexInEdgeConnectionDict('D'))

        g.addConnectionForeExsistingNode("A", 'C')
        self.assertTrue(g.containsConnection("D", 'A'))

    def test_initialize_starter_graph(self):
        global testGraphs
        for graph in testGraphs:
            self.assertTrue(graph.containsVertexInEdgeConnectionDict('A'))
            self.assertTrue(graph.containsVertexInEdgeConnectionDict('B'))
            self.assertTrue(graph.containsVertexInEdgeConnectionDict('C'))

            self.assertTrue(graph.containsVertexInValues('A'))
            self.assertTrue(graph.containsVertexInValues('B'))
            self.assertTrue(graph.containsVertexInValues('C'))

    def test_connectingGraph(self):
        g = Graph(2)
        temp_edge_dict = {"A": ['B'],
                        "B": ['C'],
                        "C": ['D'],
                        "D": ['E'],
                        "E": ['F'],
                        "F": []}    
        temp_vertex_values_dict = {"A": 1,
                                "B": 1,
                                "C": 1,
                                "D": 1,
                                "E": 1,
                                "F": 1}
        g.addSetGraph(temp_edge_dict, temp_vertex_values_dict, 2)
        print("test b graph: ")
        g.printGraph()
        self.assertTrue(g.containsConnection("B", 'C'))



if __name__ == '__main__':
    unittest.main()
