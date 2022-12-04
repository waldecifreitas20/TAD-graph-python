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
        degree = 0
        if not self.hasNode(value):
            raise Exception('VERTICE NAO FAZ PARTE DO GRAFO')
        
        for i in range(self.length()):
            if self.edges[i][value] != 0:
                degree += 1
        return degree

    def getDegreeOut(self, value):
        degree = 0
        if not self.hasNode(value):
            raise Exception('VERTICE NAO FAZ PARTE DO GRAFO')

        for i in range(self.length()):
            if self.edges[value][i] != 0:
                degree += 1
        return degree
    
    def getTransposed(self):
        numberNodes = self.length()
        graph = DirectionedMatrixGraph(numberNodes)

        for fromNode in range(self.length()):
            for toNode in range(self.length()):
                if self.edges[fromNode][toNode] != 0:
                    graph.addEdge(toNode, fromNode)
            
        return graph
        