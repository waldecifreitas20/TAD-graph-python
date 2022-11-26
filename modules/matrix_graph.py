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
    

    def printGraph(self):
        self._printNodeNameLine()
        for line in range(self.getNumberNodes()):
            node = self.nodes[line].value
            print(f'{node}| ', end='')
            for column in range(self.getNumberNodes()):
                edge = self.edges[line][column]
                print(f'{edge} ', end='')
            print()

    def _printNodeNameLine(self):
        print('   ', end='')
        for i in range(self.getNumberNodes()):
            print(f'{self.nodes[i].value} ', end='')
        print()
        for i in range(self.getNumberNodes()):
            print(f'---', end='')
        print()
        
