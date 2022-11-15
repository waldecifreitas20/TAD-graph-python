class Graph:

    def __init__(self, nodesNumber) -> None:
        self.nodes = self._generateNodes(nodesNumber)
        self.edges = []
        self.nodesNumber = len(self.nodes)

    def _generateNodes(self, quantity) -> None:
        nodes = []
        for i in range(quantity):
            node = self.Node(i)
            node.id = i
            nodes.append(node)
            
        return nodes
    

    def hasNode(self, value) -> bool:
        for node in self.nodes:
            if node.value == value:
                return True

        return False

    def getNumberNodes(self) -> int: return len(self.nodes) 
    
    def getNumberEdges(self) -> int: return len(self.edges)

#   @abstract
    def addEdge(self, fromNode, toNode): raise Exception('Abstract method must be implemented')
    def removedge(self, fromNode, toNode): raise Exception('Abstract method must be implemented')
    def hasEdge(self, fromNode, toNode): raise Exception('Abstract method must be implemented')

    def nodeDegree(self, value) -> int: raise Exception('Abstract method must be implemented')

    def printGraph(self) -> None: raise Exception('Abstract method must be implemented')

    def printNodes(self) -> None:
        print('[', end='') 
        for node in self.nodes:
            print(f'{node.value}, ', end='')
        print('\\0]') 

    class Node:
        id = int
        degree = int
        def __init__(self, value, id=-1, degree=0):
            self.value = value
            self.id = id
            self.degree = degree

    class Edge:

        def __init__(self, fromNode, toNode, weight=1):
            self.toNode = toNode
            self.fromNode = fromNode
            self.weight = weight
