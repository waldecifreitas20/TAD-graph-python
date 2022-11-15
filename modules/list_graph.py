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

        # ADCIONA A NOVA ARESTA
        self.edges.append(self.Edge(fromNode, toNode))

#   @Override
    def removeEdge(self, node): pass
#   @Override
    def removeEdge(self, fromNode, toNode): pass
#   @Override
    def hasEdge(self, fromNode, toNode):
        for edge in self.edges:
            if edge.fromNode == fromNode and edge.toNode == toNode:
                return True
        return False
