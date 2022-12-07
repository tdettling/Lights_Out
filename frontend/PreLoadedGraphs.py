from Graph import Graph


def createOptionOne():
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
    g.printGraph()
    return g


def createOptionTwo():
    g = Graph(2)
    temp_edge_dict = {"A": ['B'],
                      "B": ['C'],
                      "C": ['D', 'A'],
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

    return g

def createOptionThree():
    g = Graph(2)
    temp_edge_dict = {"A": ['B'],
                      "B": ['C'],
                      "C": ['D'],
                      "D": ['A']}
    temp_vertex_values_dict = {"A": 0,
                               "B": 1,
                               "C": 1,
                               "D": 1}
    g.addSetGraph(temp_edge_dict, temp_vertex_values_dict, 2)

    return g

def createOptionFour():
    g = Graph(2)
    temp_edge_dict = {"A": ['B', 'C'],
                      "B": ['A'],
                      "C": ['D'],
                      "D": []}
    temp_vertex_values_dict = {"A": 1,
                               "B": 1,
                               "C": 0,
                               "D": 1}
    g.addSetGraph(temp_edge_dict, temp_vertex_values_dict, 2)

    return g

def createOptionFive():
    g = Graph(2)
    temp_edge_dict = {"A": [],
                      "B": [],
                      "C": ['A', 'B'],
                      "D": ['C'],
                      "E": ['C'],
                      "F": ['C']}
    temp_vertex_values_dict = {"A": 0,
                               "B": 1,
                               "C": 1,
                               "D": 0,
                               "E": 1,
                               "F": 1}
    g.addSetGraph(temp_edge_dict, temp_vertex_values_dict, 2)

    return g

def createOptionSix():
    g = Graph(2)
    temp_edge_dict = {"A": ['D'],
                      "B": ['D'],
                      "C": ['D'],
                      "D": ['E'],
                      "E": ['D']}
    temp_vertex_values_dict = {"A": 0,
                               "B": 0,
                               "C": 1,
                               "D": 1,
                               "E": 0}
    g.addSetGraph(temp_edge_dict, temp_vertex_values_dict, 2)
  
    return g 

def createOptionSeven():
    g = Graph(2)
    temp_edge_dict = {"A": [],
                      "B": ['C'],
                      "C": ['A', 'E'],
                      "D": ['C'],
                      "E": []}
    temp_vertex_values_dict = {"A": 0,
                               "B": 0,
                               "C": 1,
                               "D": 1,
                               "E": 1}
    g.addSetGraph(temp_edge_dict, temp_vertex_values_dict, 2)

    return g

def createOptionEight():
    g = Graph(2)
    temp_edge_dict = {"A": ['B'],
                      "B": ['A', 'C'],
                      "C": ['B', 'E'],
                      "D": ['C', 'E'],
                      "E": ['D']}
    temp_vertex_values_dict = {"A": 1,
                               "B": 1,
                               "C": 1,
                               "D": 1,
                               "E": 1}
    g.addSetGraph(temp_edge_dict, temp_vertex_values_dict, 2)

    return g

def createOptionNine():
    g = Graph(2)
    temp_edge_dict = {"A": ['D'],
                      "B": [],
                      "C": ['B'],
                      "D": ['B', 'E'],
                      "E": ['A']}
    temp_vertex_values_dict = {"A": 1,
                               "B": 0,
                               "C": 0,
                               "D": 1,
                               "E": 1}
    g.addSetGraph(temp_edge_dict, temp_vertex_values_dict, 2)

    return g

def createOptionTen():
    g = Graph(2)
    temp_edge_dict = {"A": ['B', 'C', 'D'],
                      "B": [],
                      "C": [],
                      "D": ['E'],
                      "E": [],
                      "F": ['B', 'E']}
    temp_vertex_values_dict = {"A": 1,
                               "B": 0,
                               "C": 0,
                               "D": 1,
                               "E": 0,
                               "F": 1}
    g.addSetGraph(temp_edge_dict, temp_vertex_values_dict, 2)

    return g

def chooseOption(option_selected):
    match option_selected:
        case "option_one":
            print("something")
            selectedGraph = createOptionOne()
            return selectedGraph
        case "option_two":
            print("something 2")
            selectedGraph = createOptionTwo()
            return selectedGraph

        case "option_three":
            selectedGraph = createOptionThree()
            return selectedGraph
            print("something")

        case "option_four":
            print("something")
            selectedGraph = createOptionFour()
            return selectedGraph

        case "option_five":
            print("something")
            selectedGraph = createOptionFive()
            return selectedGraph

        case "option_six":
            print("something")
            selectedGraph = createOptionSix()
            return selectedGraph

        case "option_seven":
            print("something")
            selectedGraph = createOptionSeven()
            return selectedGraph

        case "option_eight":
            print("something")
            selectedGraph = createOptionEight()
            return selectedGraph

        case "option_nine":
            print("something")
            selectedGraph = createOptionNine()
            return selectedGraph

        case "option_ten":
            print("something")
            selectedGraph = createOptionTen()
            return selectedGraph

        case _:
            print("not an option")
            return
