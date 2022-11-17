from modules.list_graph import *


class DirectionedListGraph(ListGraph):

    def __init__(self, nodesNumber):
        super().__init__(nodesNumber)

    def addEdge(self, fromNode, toNode, weight=1):
        super().addEdge(fromNode, toNode, weight)