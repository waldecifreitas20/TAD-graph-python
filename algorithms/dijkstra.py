from utils.tools import sortIndexesOfMaxValue

_MAX_INT_ = 99999999999999

class Dijkstra:

    def __init__(self, graph) -> None:
        self.graph = graph
        self.ancestor = []
        self.nodesWeight = []
        self.knowns = []
        self.visited = []
        
    def _initVariables(self):
        self.ancestor.clear()
        self.nodesWeight.clear()
        self.visited.clear()

        for _ in range(self.graph.length()):
            self.visited.append(False)
            self.ancestor.append(None)
            self.nodesWeight.append(_MAX_INT_)

    def dijkstra(self, initialNode=0):
        self._initVariables()
        self.nodesWeight[initialNode] = 0

        """      edges = []
        for node in range(self.graph.length()):
            adjacents = self.graph.getEdgesOf(node)
            edges.extend(adjacents) """
     
        for _ in range(self.graph.length()):
            node = self._getIndexOfMinWeight()
            print(node)
            self.visited[node] = True
            edges = self.graph.getEdgesOf(node)
            for edge in edges:
                origin = edge.fromNode
                destiny = edge.toNode
                weight = edge.weight

                if self.nodesWeight[origin] + weight < self.nodesWeight[destiny]:
                    self.ancestor[destiny] = origin
                    self.nodesWeight[destiny] = self.nodesWeight[origin] + weight


    def _getIndexOfMinWeight(self): 
        nodes = self.nodesWeight.copy()
        minimals = []
        for i in range(len(nodes) ):       
            if not self.visited[i]:
                minimals.append(i)
        
        minimal = minimals[0]
        for index in minimals:
            if self.nodesWeight[index] < self.nodesWeight[minimal]:
                minimal = index
        return minimal

    def getShortestPath(self, origin, destiny):
        self.dijkstra(origin)
        path = []
        node = destiny
        while node != origin and self.ancestor[node] is not None:
            path.append(node)
            node = self.ancestor[node]
        path.append(origin)
        path.reverse()
        return path