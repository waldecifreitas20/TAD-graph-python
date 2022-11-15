from modules.graph import *

class MatrixGraph(Graph):

    def __init__(self, numberNodes):
        super().__init__(numberNodes)
        self.edges = self._initEdges(numberNodes)

    def _initEdges(numberNodes):
        edges = []

        for line in range(numberNodes):
            edges.append([])
            for column in range(numberNodes):
                edges[line][column] = 0

#   @Override
    def addEdge(self, fromNode, toNode):
        # TODO
        pass