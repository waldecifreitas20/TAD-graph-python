from modules.graph import *

class ListGraph(Graph):

    def __init__(self, nodesNumber, isMatrix=False):
        self.isMatrix = isMatrix
        self.edges = []
        self.nodes = self._generateNodes(nodesNumber)
        self.nodesNumber = len(self.nodes)

    def _generateNodes(self, quantity):
        nodes = []
        for i in range(quantity):
            node = self.Node(i)
            node.id = i
            nodes.append(node)
            
        return nodes

    def addEdge(self, fromNode, toNode):
        pass

    def removeEdge(self, node):pass
    def removeEdge(self, fromNode, toNode):pass
    
   
