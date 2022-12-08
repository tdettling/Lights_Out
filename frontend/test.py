import unittest

import PreLoadedGraphs
from Graph import Graph


class TestGraph(unittest.TestCase):

    """
    Tests the general fucntionality of the Graph.py file.
    Includes checking both false and true vertices, and adding vertices.
    """
    def test_general(self):
        g = Graph(2)
        #self.assertFalse(g.addVertex("D", 'A', 0))
        #print("test a graph: ")
        #g.printGraph()
        self.assertFalse(g.containsVertexInValues('D'))
        self.assertFalse(g.containsVertexInValues('A'))
        self.assertFalse(g.containsVertexInEdgeConnectionDict('D'))
        self.assertFalse(g.containsVertexInEdgeConnectionDict('A'))
        g.addVertex('D')
        g.addVertex('A')

        self.assertTrue(g.containsVertexInValues('D'))
        self.assertTrue(g.containsVertexInValues('A'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('D'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('A'))

        g.addVertex('A', 'C')
        self.assertTrue(g.addConnectionForeExsistingNode("A", 'C'))
        self.assertTrue(g.containsConnection('A', 'C'))
        self.assertFalse(g.containsConnection("D", 'A'))

    """
    Tests creating your own graph. 
    Includes checking both false and true vertices, adding vertices, and changing connections.
    """
    def test_create_graph(self):
        g = Graph(2)
        g.addVertex('A')
        g.addVertex('C')
        g.addVertex('P')

        self.assertTrue(g.containsVertexInValues('A'))
        self.assertTrue(g.containsVertexInValues('C'))
        self.assertTrue(g.containsVertexInValues('P'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('A'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('C'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('P'))

        g.addConnectionForeExsistingNode('A', 'C')

        g.removeVertex('P')

        self.assertFalse(g.containsVertexInValues('P'))
        self.assertFalse(g.containsVertexInEdgeConnectionDict('P'))

        g.editVertexValue('A', 4)
        self.assertEqual(0, g.vertex_values['A'])

        g.editVertexValue('A', 3)
        self.assertEqual(1, g.vertex_values['A'])

        g.addVertex('P')
        g.addConnectionForeExsistingNode('P', 'C')

        g.changeConnection('A', 'C', 'P')
        self.assertTrue(g.containsConnection('A', 'P'))
        self.assertFalse(g.containsConnection('A', 'C'))


    """
    Tests replacing an instantiated graph with a new one and the transition of connections. 
    Includes checking the values of a graph, and checking connections.
    """

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
        #print("test b graph: ")
        #g.printGraph()
        self.assertTrue(g.containsConnection("B", 'C'))

    """
    Tests basic functionality of checking for a winner and toggeling a vertex. 
    Includes checking for a winner, and toggeling a vertex.
    """
    def test_togglePresetONE(self):
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

        g.toggleVertex("B")
        self.assertEqual(g.vertex_values["B"],0, "Vertex B should be 0")
        self.assertEqual(g.vertex_values["C"],0, "Vertex C should be 0")

        g.toggleVertex("C")
        self.assertEqual(g.vertex_values["C"],1, "Vertex C should be 1")
        self.assertEqual(g.vertex_values["D"],0, "Vertex D should be 0")

        self.assertFalse(g.checkWinner())


    """
    Tests preset one. 
    Includes checking for a winner, toggeling a vertex, and checking connections.
    """
    def test_winPresetONE(self):
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

        self.assertEqual(g.vertex_values["A"],1, "Initializing:  Vertex A should be 1")
        self.assertEqual(g.vertex_values["B"],1, "Initializing:  Vertex B should be 1")
        self.assertEqual(g.vertex_values["C"],1, "Initializing:  Vertex C should be 1")
        self.assertEqual(g.vertex_values["D"],1, "Initializing:  Vertex D should be 1")
        self.assertEqual(g.vertex_values["E"],1, "Initializing:  Vertex E should be 1")
        self.assertEqual(g.vertex_values["F"],1, "Initializing:  Vertex F should be 1")


        g.toggleVertex("A")
        self.assertEqual(g.vertex_values["A"],0, "TOGGLING A: Vertex A should be 0")
        self.assertEqual(g.vertex_values["B"],0, "TOGGLING A: Vertex B should be 0")
        self.assertEqual(g.vertex_values["C"],1, "TOGGLING A: Vertex C should be 1")
        self.assertEqual(g.vertex_values["D"],1, "TOGGLING A: Vertex D should be 1")
        self.assertEqual(g.vertex_values["E"],1, "TOGGLING A: Vertex E should be 1")
        self.assertEqual(g.vertex_values["F"],1, "TOGGLING A: Vertex F should be 1")
        self.assertFalse(g.checkWinner())

        g.toggleVertex("C")
        self.assertEqual(g.vertex_values["A"],0, "TOGGLING C: Vertex A should be 0")
        self.assertEqual(g.vertex_values["B"],0, "TOGGLING C: Vertex B should be 0")
        self.assertEqual(g.vertex_values["C"],0, "TOGGLING C: Vertex C should be 0")
        self.assertEqual(g.vertex_values["D"],0, "TOGGLING C: Vertex D should be 0")
        self.assertEqual(g.vertex_values["E"],1, "TOGGLING C: Vertex E should be 1")
        self.assertEqual(g.vertex_values["F"],1, "TOGGLING C: Vertex F should be 1")
        self.assertFalse(g.checkWinner())

        g.toggleVertex("E")
        self.assertEqual(g.vertex_values["A"],0, "TOGGLING E: Vertex A should be 0")
        self.assertEqual(g.vertex_values["B"],0, "TOGGLING E: Vertex B should be 0")
        self.assertEqual(g.vertex_values["C"],0, "TOGGLING E: Vertex C should be 0")
        self.assertEqual(g.vertex_values["D"],0, "TOGGLING E: Vertex D should be 0")
        self.assertEqual(g.vertex_values["E"],0, "TOGGLING E: Vertex E should be 0")
        self.assertEqual(g.vertex_values["F"],0, "TOGGLING E: Vertex F should be 0")
        self.assertTrue(g.checkWinner())


    """
    Tests invalid connections, planarity, and ready to play. 
    Includes reseting and intializing the graph, planarity, ready to play, and checking connections.
    """
    def test_invalid_connections(self):
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
        g.resetGraph()
        self.assertFalse(g.readyToPlay())

        self.assertEqual({}, g.edge_dict, "Graph should be empty")
        self.assertEqual({}, g.vertex_values, "Graph should be empty")

        g.addSetGraph(temp_edge_dict, temp_vertex_values_dict, 2)

        self.assertTrue(g.isPlanar(), "Graph is Planar")
        self.assertTrue(g.readyToPlay())
        self.assertFalse(g.checkWinner())

        self.assertTrue(g.containsVertexInValues('A'))
        self.assertTrue(g.containsVertexInValues('B'))
        self.assertTrue(g.containsVertexInValues('C'))
        self.assertTrue(g.containsVertexInValues('D'))
        self.assertTrue(g.containsVertexInValues('E'))
        self.assertTrue(g.containsVertexInValues('F'))

        self.assertTrue(g.containsVertexInEdgeConnectionDict('A'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('B'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('C'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('D'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('E'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('F'))

        self.assertFalse(g.containsConnection("A", 'A'))
        self.assertFalse(g.containsConnection("A", 'C'))
        self.assertFalse(g.containsConnection("A", 'D'))
        self.assertFalse(g.containsConnection("A", 'E'))
        self.assertFalse(g.containsConnection("A", 'F'))

        self.assertFalse(g.containsConnection("B", 'B'))
        self.assertFalse(g.containsConnection("B", 'A'))
        self.assertFalse(g.containsConnection("B", 'D'))
        self.assertFalse(g.containsConnection("B", 'E'))
        self.assertFalse(g.containsConnection("B", 'F'))

        self.assertFalse(g.containsConnection("C", 'A'))
        self.assertFalse(g.containsConnection("C", 'B'))
        self.assertFalse(g.containsConnection("C", 'C'))
        self.assertFalse(g.containsConnection("C", 'E'))
        self.assertFalse(g.containsConnection("C", 'F'))

        self.assertFalse(g.containsConnection("D", 'D'))
        self.assertFalse(g.containsConnection("D", 'A'))
        self.assertFalse(g.containsConnection("D", 'B'))
        self.assertFalse(g.containsConnection("D", 'C'))
        self.assertFalse(g.containsConnection("D", 'F'))

        self.assertFalse(g.containsConnection("E", 'E'))
        self.assertFalse(g.containsConnection("E", 'A'))
        self.assertFalse(g.containsConnection("E", 'B'))
        self.assertFalse(g.containsConnection("E", 'C'))
        self.assertFalse(g.containsConnection("E", 'D'))
       
        self.assertFalse(g.containsConnection("F", 'A'))
        self.assertFalse(g.containsConnection("F", 'B'))
        self.assertFalse(g.containsConnection("F", 'C'))
        self.assertFalse(g.containsConnection("F", 'D'))
        self.assertFalse(g.containsConnection("F", 'E'))
        self.assertFalse(g.containsConnection("F", 'F'))
        

    """
    Tests preset two. 
    Includes reseting and intializing the graph, planarity, 
    ready to play, getting the adjacent verticies, and checking connections.
    """
    def test_PresetGraphTWO(self):
        g = PreLoadedGraphs.createOptionTwo()

        temp_edge_dict = g.edge_dict
        temp_vertex_values_dict = g.vertex_values
        modulus = 2

        g.resetGraph()
        self.assertFalse(g.readyToPlay())

        self.assertEqual({}, g.edge_dict, "Graph should be empty")
        self.assertEqual({}, g.vertex_values, "Graph should be empty")

        g.addSetGraph(temp_edge_dict, temp_vertex_values_dict, modulus)

        self.assertTrue(g.isPlanar(), "Graph is Planar")
        self.assertTrue(g.readyToPlay())
        self.assertFalse(g.checkWinner())

        self.assertTrue(g.containsVertexInValues('A'))
        self.assertTrue(g.containsVertexInValues('B'))
        self.assertTrue(g.containsVertexInValues('C'))
        self.assertTrue(g.containsVertexInValues('D'))
        self.assertTrue(g.containsVertexInValues('E'))
        self.assertTrue(g.containsVertexInValues('F'))

        self.assertTrue(g.containsVertexInEdgeConnectionDict('A'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('B'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('C'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('D'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('E'))
        self.assertTrue(g.containsVertexInEdgeConnectionDict('F'))

        self.assertFalse(g.containsConnection("A", 'A'))
        self.assertFalse(g.containsConnection("A", 'C'))
        self.assertFalse(g.containsConnection("A", 'D'))
        self.assertFalse(g.containsConnection("A", 'E'))
        self.assertFalse(g.containsConnection("A", 'F'))

        self.assertFalse(g.containsConnection("B", 'B'))
        self.assertFalse(g.containsConnection("B", 'A'))
        self.assertFalse(g.containsConnection("B", 'D'))
        self.assertFalse(g.containsConnection("B", 'E'))
        self.assertFalse(g.containsConnection("B", 'F'))

        
        self.assertFalse(g.containsConnection("C", 'B'))
        self.assertFalse(g.containsConnection("C", 'C'))
        self.assertFalse(g.containsConnection("C", 'E'))
        self.assertFalse(g.containsConnection("C", 'F'))

        self.assertFalse(g.containsConnection("D", 'D'))
        self.assertFalse(g.containsConnection("D", 'A'))
        self.assertFalse(g.containsConnection("D", 'B'))
        self.assertFalse(g.containsConnection("D", 'C'))
        self.assertFalse(g.containsConnection("D", 'F'))

        self.assertFalse(g.containsConnection("E", 'E'))
        self.assertFalse(g.containsConnection("E", 'A'))
        self.assertFalse(g.containsConnection("E", 'B'))
        self.assertFalse(g.containsConnection("E", 'C'))
        self.assertFalse(g.containsConnection("E", 'D'))
       
        self.assertFalse(g.containsConnection("F", 'A'))
        self.assertFalse(g.containsConnection("F", 'B'))
        self.assertFalse(g.containsConnection("F", 'C'))
        self.assertFalse(g.containsConnection("F", 'D'))
        self.assertFalse(g.containsConnection("F", 'E'))
        self.assertFalse(g.containsConnection("F", 'F'))
    
        self.assertTrue(g.containsConnection('A', 'B'))  
        self.assertTrue(g.containsConnection('B', 'C'))  
        self.assertTrue(g.containsConnection("C", 'A'))
        self.assertTrue(g.containsConnection('C', 'D')) 
        self.assertTrue(g.containsConnection('D', 'E')) 
        self.assertTrue(g.containsConnection('E', 'F')) 


        self.assertEqual(['B'], g.getListOfAdjacentVerticies('A'), "A should be adjacent to B")
        self.assertEqual(['C'], g.getListOfAdjacentVerticies('B'), "B should be adjacent to C")
        #self.assertEqual(['D', 'A'], g.getListOfAdjacentVerticies('C'), "C should be adjacent to A and D")
        self.assertEqual(['E'], g.getListOfAdjacentVerticies('D'), "D should be adjacent to E")
        self.assertEqual(['F'], g.getListOfAdjacentVerticies('E'), "E should be adjacent to F")

        g.toggleVertex("A")
        self.assertEqual(g.vertex_values["A"],0, "TOGGLING A: Vertex A should be 0")
        self.assertEqual(g.vertex_values["B"],0, "TOGGLING A: Vertex B should be 0")
        self.assertEqual(g.vertex_values["C"],1, "TOGGLING A: Vertex C should be 1")
        self.assertEqual(g.vertex_values["D"],1, "TOGGLING A: Vertex D should be 1")
        self.assertEqual(g.vertex_values["E"],1, "TOGGLING A: Vertex E should be 1")
        self.assertEqual(g.vertex_values["F"],1, "TOGGLING A: Vertex F should be 1")
        self.assertFalse(g.checkWinner())

        g.toggleVertex("C")
        self.assertEqual(g.vertex_values["A"],1, "TOGGLING C: Vertex A should be 1")
        self.assertEqual(g.vertex_values["B"],0, "TOGGLING C: Vertex B should be 0")
        self.assertEqual(g.vertex_values["C"],0, "TOGGLING C: Vertex C should be 0")
        self.assertEqual(g.vertex_values["D"],0, "TOGGLING C: Vertex D should be 0")
        self.assertEqual(g.vertex_values["E"],1, "TOGGLING C: Vertex E should be 1")
        self.assertEqual(g.vertex_values["F"],1, "TOGGLING C: Vertex F should be 1")
        self.assertFalse(g.checkWinner())

        g.toggleVertex("E")
        self.assertEqual(g.vertex_values["A"],1, "TOGGLING E: Vertex A should be 0")
        self.assertEqual(g.vertex_values["B"],0, "TOGGLING E: Vertex B should be 0")
        self.assertEqual(g.vertex_values["C"],0, "TOGGLING E: Vertex C should be 0")
        self.assertEqual(g.vertex_values["D"],0, "TOGGLING E: Vertex D should be 0")
        self.assertEqual(g.vertex_values["E"],0, "TOGGLING E: Vertex E should be 0")
        self.assertEqual(g.vertex_values["F"],0, "TOGGLING E: Vertex F should be 0")




if __name__ == '__main__':
    unittest.main()
