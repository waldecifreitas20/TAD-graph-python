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

    def getNode(self, value):
         for node in self.nodes:
            if node.value == value:
                return node

    def getNodeId(self, value):
         for node in self.nodes:
            if node.value == value:
                return node.id
    def getNumberNodes(self) -> int: return len(self.nodes) 
    
    def getNumberEdges(self) -> int: return len(self.edges)

    def getAdjacentsFrom(self,value):
        adjacents = []
        for edge in self.edges:
            if edge.fromNode == value:
                adjacents.append(edge.toNode)
        adjacents.sort()
        return adjacents
    

    def printNodes(self) -> None:
        print('[', end='') 
        for node in self.nodes:
            print(f'{node.value}, ', end='')
        print('\\0]')
 
    def addEdge(self, fromNode, toNode, weight=1): 
        # CHECA SE OS VERTICES EXISTEM NO GRAFO
        if(not self.hasNode(fromNode) or not self.hasNode(toNode)):
            raise Exception('AMBOS OS VERTICES DEVEM FAZER PARTE DO GRAFO!')

        # CHECA SE A ARESTA JA EXISTE NO GRAFO
        if(self.hasEdge(fromNode, toNode)):
            raise Exception(
                'NAO EH POSSIVEL ADCIONAR UMA ARESTA JA EXISTENTE!')

        self._addEdge(fromNode, toNode, weight)
#   @abstract
    def printGraph(self) -> None: raise Exception('Abstract method must be implemented')
    def _addEdge(self, fromNode, toNode, weight=1): raise Exception('Abstract method must be implemented')
    def removedge(self, fromNode, toNode): raise Exception('Abstract method must be implemented')
    def hasEdge(self, fromNode, toNode): raise Exception('Abstract method must be implemented')
    def nodeDegree(self, value) -> int: raise Exception('Abstract method must be implemented')

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
