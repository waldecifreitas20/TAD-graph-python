if __name__ == '__main__':
    from graph import *
else:
    from modules.graph import *


class ListGraph(Graph):

    def __init__(self, numberNodes) -> None:
        super().__init__(numberNodes)
        self.edges = []

    def getEdge(self, fromNode, toNode):
        for edge in self.edges:
            if edge.fromNode == fromNode and edge.toNode == toNode:
                return edge
        raise Exception('Edges does not exist')


#   @Override


    def _addEdge(self, fromNode, toNode, weight=1):
        # ADCIONA A NOVA ARESTA
        self.edges.append(self.Edge(fromNode, toNode, weight))
        self.edges.append(self.Edge(toNode, fromNode, weight))

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

#   @Override
    def printGraph(self):
        for node in self.nodes:
            print(node.value, end=' ')
            for adjacent in self.getAdjacentsFrom(node.value):
                weight = self.getEdge(node.value, adjacent).weight
                print(f'-({weight})-> {adjacent}', end=f' ')
            print('-> null')
