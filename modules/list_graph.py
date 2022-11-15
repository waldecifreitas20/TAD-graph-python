if __name__ == '__main__':
    from graph import *
else:
    from modules.graph import *


class ListGraph(Graph):

    def __init__(self, numberNodes) -> None:
        super().__init__(numberNodes)

    def addEdge(self, fromNode, toNode):

        if(self.hasEdge(fromNode, toNode)):
            raise Exception('NAO EH POSSIVEL ADCIONAR UMA ARESTA EXISTENTE!')
        else:
            self.edges.append(self.Edge(fromNode, toNode))

    def removeEdge(self, node): pass
    def removeEdge(self, fromNode, toNode): pass

    # Override
    def hasEdge(self, fromNode, toNode):

        for edge in self.edges:
            if edge.fromNode == fromNode and edge.toNode:
                return True

        return False


