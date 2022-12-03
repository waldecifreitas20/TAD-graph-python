from utils.tools import sortEdgesByWeight
from collections import deque

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
        
        for _ in range(self.graph.getNumberNodes()):
            self.ancestor.append(None)
            self.nodesWeight.append(_MAX_INT_)
            self.visited.append(False)
        

    def getMinimalSpanningTree(self, initialNode=0):
        self._initVariables()

        self.nodesWeight[initialNode] = 0
        
        edges = self.graph.getEdgesOf(initialNode)
        heap = sortEdgesByWeight(edges)

        while len(heap) > 0:

            edge = heap.pop(0)
            
            if not self.visited[edge.toNode] and (edge.weight < self.nodesWeight[edge.toNode]):
                self.ancestor[edge.toNode] = edge.fromNode
                self.visited[edge.toNode] = True
                nextAdjacents = self.graph.getEdgesOf(edge.toNode)
                heap.extend(nextAdjacents)
                heap = sortEdgesByWeight(heap)
