if __name__ == '__main__':
    from matrix_graph import *
else:
    from modules.matrix_graph import *


class DirectionedMatrixGraph(MatrixGraph):

    def __init__(self, nodesNumber):
        super().__init__(nodesNumber)
        self.edges = self._initEdges(nodesNumber)

#   @Override
    def _addEdge(self, fromNode, toNode, weight=1):
        self.edges[fromNode][toNode] = weight

    def _removeEdge(self, fromNode, toNode):
        self.edges[fromNode][toNode] = 0

    def _initEdges(self,numberNodes):
        edges = []

        for line in range(numberNodes):
            edges.append([])
            for column in range(numberNodes):
                edges[line].append(0)
        return edges

    def hasEdge(self, fromNode, toNode):
        return  self.edges[fromNode][toNode] != 0
   
    def getDegreeIn(self, value):
        pass

    def getDegreeOut(self, value):
        pass
        