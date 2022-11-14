#main running file to control everthing here
import logic.Graph as g

def main_run():
    graph = g.Graph(1)
    graph.addVertex("A", "B", 1)
    graph.addVertex("B", "A", 0)
    graph.addVertex("C", "A,B")

    graph.addVertex("A", "C", 1)

main_run()