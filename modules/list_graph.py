if __name__ == '__main__':
    from graph import *
else:
    from modules.graph import *


class ListGraph(Graph):

    def __init__(self, numberNodes) -> None:
        super().__init__(numberNodes)

#   @Override
    def addEdge(self, fromNode, toNode):
        # CHECA SE OS VERTICES EXISTEM NO GRAFO
        if(not self.hasNode(fromNode) or not self.hasNode(toNode)):
            raise Exception('AMBOS OS VERTICES DEVEM FAZER PARTE DO GRAFO!')

        # CHECA SE A ARESTA JA EXISTE NO GRAFO
        if(self.hasEdge(fromNode, toNode)):
            raise Exception(
                'NAO EH POSSIVEL ADCIONAR UMA ARESTA JA EXISTENTE!')
        
        origin = self.getNode(fromNode)
        destiny = self.getNode(toNode)

        # ADCIONA A NOVA ARESTA
        self.edges.append(self.Edge(origin, destiny))
        self.edges.append(self.Edge(destiny, origin))

#   @Override
    def removeEdge(self, node): pass

#   @Override
    def removeEdge(self, fromNode, toNode): pass

#   @Override
    def hasEdge(self, fromNode, toNode):
        for edge in self.edges:
            if edge.fromNode.value == fromNode and edge.toNode.value == toNode:
                return True
        return False

#   @Override
    def printGraph(self):
        for node in self.nodes:
            print(node.value, end=' -> ')
            for adjacent in self.getAdjacentsFrom(node.value):
                print(adjacent,end= ' -> ')
            print('null')

g = ListGraph(5)
g.addEdge('1','4')
g.addEdge('1','2')
g.addEdge('1','3')
g.addEdge('0','2')
g.addEdge('2','2')
g.printGraph()
