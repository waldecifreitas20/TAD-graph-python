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

    def getNumberNodes(self) -> int: len(self.nodes) 
    
    def getNumberEdges(self) -> int: len(self.edges)

    # Metodos abstratos
    def addEdge(self, fromNode, toNode): pass
    def removedge(self, fromNode, toNode): pass
    def hasEdge(self, fromNode, toNode): pass

    def nodeDegree(self, value) -> int: pass

    def printGraph(self) -> None: pass

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
