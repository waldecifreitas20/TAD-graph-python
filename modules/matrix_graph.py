if __name__ == '__main__':
    from graph import *
else:
    from modules.graph import *

class MatrixGraph(Graph):

    def __init__(self, numberNodes):
        super().__init__(numberNodes)
        self.edges = self._initEdges(numberNodes)

    def _initEdges(self,numberNodes):
        edges = []

        for line in range(numberNodes):
            edges.append([])
            for column in range(numberNodes):
                edges[line].append(0)
        return edges


#   @Override
    def _addEdge(self, fromNode, toNode, weight=1):
        self.edges[fromNode][toNode] = weight
        self.edges[toNode][fromNode] = weight
        

    def _removeEdge(self, fromNode, toNode):
        self.edges[fromNode][toNode] = 0
        self.edges[toNode][fromNode] = 0
#   @Override
    def hasEdge(self, fromNode, toNode):
        edge1 = self.edges[fromNode][toNode] != 0
        edge2 = self.edges[toNode][fromNode] != 0
        return edge1 and edge2
    
#   @Override
    def _getNodeDegree(self, value):
        degree = 0
        for i in range(self.length()):
            if self.edges[value][i] != 0:
                degree += 1
        return degree
        
#   @Override
    def getAdjacentsFrom(self, value) -> list:
        adjacents = []
        for i in range(self.length()):
            if self.edges[value][i] != 0:
                adjacents.append(i)
        adjacents.sort()
        return adjacents
        
#   @Override
    def getEdgesOf(self, value) -> list:
        edges = []

        for i in range(self.length()):
            edgeWeight = self.edges[value][i]
            if edgeWeight > 0:
                edges.append(Graph.Edge(value, i, edgeWeight ))
        return edges
        
#   @Override
    def getEdge(self, fromNode, toNode):
        edgeWeight = self.edges[fromNode][toNode]
        if edgeWeight <= 0:
            raise Exception('Edges does not exist')
        
        return Graph.Edge(fromNode, toNode, edgeWeight)

#   @Override
    def printGraph(self):
        self._printNodeNameLine()
        for line in range(self.length()):
            node = self.nodes[line].value
            print(f'{node}| ', end='')
            for column in range(self.length()):
                edge = self.edges[line][column]
                print(f'{edge} ', end='')
            print()

    def _printNodeNameLine(self):
        print('   ', end='')
        for i in range(self.length()):
            print(f'{self.nodes[i].value} ', end='')
        print()
        for i in range(self.length()):
            print(f'---', end='')
        print()
        
