class Graph:

    def __init__(self, nodesNumber) -> None:
        self.nodes = self._generateNodes(nodesNumber)
        self.edges = []
        self._edgesLength = 0
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

    def getNumberEdges(self) -> int: return self._edgesLength

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
        if weight == 0:
            weight = 1
        self._edgesLength += 1
        self._addEdge(fromNode, toNode, weight)

    def removedge(self, fromNode, toNode):
        # CHECA SE OS VERTICES EXISTEM NO GRAFO
        if(not self.hasNode(fromNode) or not self.hasNode(toNode)):
            raise Exception('AMBOS OS VERTICES DEVEM FAZER PARTE DO GRAFO!')

        # CHECA SE A ARESTA JA EXISTE NO GRAFO
        if(not self.hasEdge(fromNode, toNode)):
            raise Exception(
                'NAO EH POSSIVEL REMOVER UMA ARESTA INEXISTENTE!')
        self._edgesLength -= 1
        self._removeEdge(fromNode, toNode)

    def getNodeDegree(self, value) -> int:
        if(not self.hasNode(value)):
            raise Exception(f'O VERTICE {value} NAO FAZ PARTE DO GRAFO!')
        return self._getNodeDegree(value)

#   @abstract
    def getAdjacentsFrom(self, value) -> tuple:
        raise Exception('Abstract method must be implemented')

    def getTransposed(self):
        raise Exception('Abstract method must be implemented')

    def printGraph(self) -> None: 
        raise Exception('Abstract method must be implemented')

    def _addEdge(self, fromNode, toNode, weight=1): 
        raise Exception('Abstract method must be implemented')

    def _removeEdge(self, fromNode, toNode): 
        raise Exception('Abstract method must be implemented')

    def hasEdge(self, fromNode, toNode) -> bool: 
        raise Exception('Abstract method must be implemented')

    def _getNodeDegree(self, value) -> int: 
        raise Exception('Abstract method must be implemented')

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
