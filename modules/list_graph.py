if __name__ == '__main__':
    from graph import *
else:
    from modules.graph import *


class ListGraph(Graph):

    def __init__(self, numberNodes) -> None:
        super().__init__(numberNodes)

    def addEdge(self, fromNode, toNode):
        if(not self.hasNode(fromNode) or not self.hasNode(toNode)):
            raise Exception('AMBOS OS VERTICES DEVEM FAZER PARTE DO GRAFO!')

        if(self.hasEdge(fromNode, toNode)):
            raise Exception('NAO EH POSSIVEL ADCIONAR UMA ARESTA JA EXISTENTE!')
        
        self.edges.append(self.Edge(fromNode, toNode))

    def removeEdge(self, node): pass
    def removeEdge(self, fromNode, toNode): pass

    # Override
    def hasEdge(self, fromNode, toNode):

        for edge in self.edges:
            if edge.fromNode == fromNode and edge.toNode == toNode:
                return True

        return False


g = ListGraph(5)
g.addEdge(1,2)
try:
  g.addEdge(10,4)
  
except Exception as error:
    print(error)