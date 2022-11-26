from modules.list_graph import *


class DirectionedListGraph(ListGraph):

    def __init__(self, nodesNumber):
        super().__init__(nodesNumber)

#   @Override
    def _addEdge(self, fromNode, toNode, weight=1):
        self.edges.append(self.Edge(fromNode, toNode, weight))
