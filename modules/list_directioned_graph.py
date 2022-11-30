from modules.list_graph import *


class DirectionedListGraph(ListGraph):

    def __init__(self, nodesNumber):
        super().__init__(nodesNumber)

#   @Override
    def _addEdge(self, fromNode, toNode, weight=1):
        self.edges.append(self.Edge(fromNode, toNode, weight))

    def getDegreeIn(self, value):
        degree = 0
        for edge in self.edges:
            if edge.toNode == value:
                degree += 1
        return degree

    def getDegreeOut(self, value):
        return len(self.getAdjacentsFrom(value))

    def _getNodeDegree(self, value):
        return self.getDegreeIn() + self.getDegreeOut()

    def getTransposed(self):
        graph = DirectionedListGraph(self.getNumberNodes())

        for edge in self.edges:
            fromNode = edge.toNode
            toNode = edge.fromNode
            graph.addEdge(fromNode, toNode)
            
        return graph