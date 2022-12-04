from utils.tools import sortEdgesByWeight
from modules.list_directioned_graph import DirectionedListGraph

_MAX_INT_ = 999999999999

class Prim:

    def __init__(self, graph) -> None:
        self.graph = graph
        self.ancestor = []
        self.nodesWeight = []
        self.visited = []

    def _initVariables(self):
        self.ancestor.clear()
        self.nodesWeight.clear()
        self.visited.clear()
        
        for _ in range(self.graph.length()):
            self.ancestor.append(None)
            self.nodesWeight.append(_MAX_INT_)
            self.visited.append(False)
        

    def _prim(self, initialNode=0):
        self._initVariables()

        self.nodesWeight[initialNode] = 0

        edges = self.graph.getEdgesOf(initialNode)
        heap = sortEdgesByWeight(edges)

        while len(heap) > 0:

            edge = heap.pop(0)
            
            if not self.visited[edge.toNode] and (edge.weight < self.nodesWeight[edge.toNode]):
                self.ancestor[edge.toNode] = edge.fromNode
                self.visited[edge.toNode] = True
                self.nodesWeight[edge.toNode] = edge.weight

                nextAdjacents = self.graph.getEdgesOf(edge.toNode)
                heap.extend(nextAdjacents)
                heap = sortEdgesByWeight(heap)

    def getMinimalSpanningTree(self, initialNode=0):
        self._prim(initialNode)
        minimalTree = DirectionedListGraph(len(self.graph.nodes))
    
        for destinyNode in range(1, minimalTree.length()):
            originNode = self.ancestor[destinyNode]
            weight = self.nodesWeight[originNode]
            minimalTree.addEdge(originNode, destinyNode, weight)

        return minimalTree
