import unittest
from Graph import Graph
import PreLoadedGraphs

class TestGraph(unittest.TestCase):

    def test_geenral(self):
        g = Graph(2)
        self.assertTrue(g.addVertex("D", 'A', 0))
        #print("test a graph: ")
        #g.printGraph()
        self.assertTrue(g.containsVertexInEdgeConnectionDict("D"))

        g.addConnectionForeExsistingNode("A", 'C')
        self.assertTrue(g.containsConnection("D", 'A'))

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
        


if __name__ == '__main__':
    unittest.main()
