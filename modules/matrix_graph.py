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
    def addEdge(self, fromNode, toNode):
         # CHECA SE OS VERTICES EXISTEM NO GRAFO
        if(not self.hasNode(fromNode) or not self.hasNode(toNode)):
            raise Exception('AMBOS OS VERTICES DEVEM FAZER PARTE DO GRAFO!')

        # CHECA SE A ARESTA JA EXISTE NO GRAFO
        if(self.hasEdge(fromNode, toNode)):
            raise Exception(
                'NAO EH POSSIVEL ADCIONAR UMA ARESTA JA EXISTENTE!')

        origin = self.getNodeId(fromNode)
        destiny = self.getNodeId(toNode)

        self.edges[origin][destiny] = 1
        self.edges[destiny][origin] = 1
        

#   @Override
    def hasEdge(self, fromNode, toNode):
        origin = self.getNodeId(fromNode)
        destiny = self.getNodeId(toNode)

        edge1 = self.edges[origin][destiny] == 1
        edge2 = self.edges[destiny][origin] == 1
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
        
