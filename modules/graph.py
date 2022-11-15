class Graph:

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

    def addEdge(self, fromNode, toNode): pass
    def removedge(self, fromNode, toNode): pass

    def hasNode(self, value):
        for node in self.nodes:
            if node.value == value:
                return True

        return True

    def hasEdge(self, fromNode, toNode): pass


    class Node:
        id = int

        def __init__(self, value):
            self.value = value

    class Edge:

        def __init__(self, fromNode, toNode):
            self.toNode = toNode
            self.fromNode = fromNode

g = Graph(10)
print(g.hasNode(0))