from utils.colors import *
from utils.checkers import isDirectionedGraph


_MAX_VALUE_ = 999999999


class DepthFirstSearch:

    def __init__(self, graph) -> None:
        self.graph = graph
        self.colors = []
        self.ancestor = []
        self.discoveryTime = []
        self.finalTime = []
        self.edgeTypes = []
        self.topologicalSorting = []

    def _initVariables(self):
        self.runtime = 0
        self.colors.clear()
        self.finalTime.clear()
        self.discoveryTime.clear()
        self.edgeTypes.clear()
        self.ancestor.clear()
        self.topologicalSorting.clear()

        for _ in range(self.graph.getNumberNodes()):
            self.colors.append(WHITE)
            self.finalTime.append(_MAX_VALUE_)
            self.discoveryTime.append(_MAX_VALUE_)
            self.ancestor.append(None)

    def getEdgesTypes(self, initialNode=0) -> list:
        self._initVariables()

        if self.colors[initialNode] == WHITE:
            self._classifyEdgesDFS(initialNode)

        for node in range(self.graph.getNumberNodes()):
            if self.colors[node] == WHITE:
                self._classifyEdgesDFS(node)
        return self.edgeTypes

    def _classifyEdgesDFS(self, node):        
        self.runtime += 1
        self.colors[node] = GRAY
        self.discoveryTime[node] = self.runtime

        adjacents = self.graph.getAdjacentsFrom(node)
        adjacents.sort(reverse=True)

        if len(adjacents) != 0:
            while True:
                try:
                    destinyNode = adjacents.pop()
                    if self.colors[destinyNode] == WHITE:
                        self.edgeTypes.append({
                            'origin': node,
                            'destiny': destinyNode,
                            'type': self.EdgeType.TREE
                        })
                        self.ancestor[destinyNode] = node
                        self._classifyEdgesDFS(destinyNode)
                    else:
                        isBackEdge = not isDirectionedGraph(
                            self.graph) or self.colors[destinyNode] == GRAY
                        if isBackEdge:
                            self.edgeTypes.append({
                                'origin': node,
                                'destiny': destinyNode,
                                'type': self.EdgeType.BACK})

                        elif self.colors[destinyNode] == BLACK:

                            isForwardEdge = self.discoveryTime[destinyNode] > self.discoveryTime[node]
                            if isForwardEdge:
                                self.edgeTypes.append({
                                    'origin': node,
                                    'destiny': destinyNode,
                                    'type': self.EdgeType.FORWARD})
                            else:
                                self.edgeTypes.append({
                                    'origin': node,
                                    'destiny': destinyNode,
                                    'type': self.EdgeType.CROSS})
                except:
                    break

        self.runtime += 1
        self.finalTime[node] = self.runtime
        self.colors[node] = BLACK

    def hasCicle(self, initialNode=0):
        edgesType = self.getEdgesTypes(initialNode)
        cicles = list(filter(lambda edge: edge['type'] == self.EdgeType.BACK, edgesType))
      
        return len(cicles) > 0

    def getTopologicalSorting(self, initialNode=0):
        if self.hasCicle():
            raise Exception('Graph must have no cicle')
        
        self._initVariables()

        if self.colors[initialNode] == WHITE:
            self._getTopologicalSortingDFS(initialNode)

        for node in range(self.graph.getNumberNodes()):
            if self.colors[node] == WHITE:
                self._getTopologicalSortingDFS(node)
        
        self.topologicalSorting.reverse()
        return self.topologicalSorting

    def _getTopologicalSortingDFS(self, node):        
        self.runtime += 1
        self.colors[node] = GRAY
        self.discoveryTime[node] = self.runtime

        adjacents = self.graph.getAdjacentsFrom(node)
        adjacents.sort(reverse=True)
        
        while len(adjacents) != 0:
            destinyNode = adjacents.pop()
            if self.colors[destinyNode] == WHITE:
                self.ancestor[destinyNode] = node
                self._getTopologicalSortingDFS(destinyNode)

        self.runtime += 1
        self.finalTime[node] = self.runtime
        self.colors[node] = BLACK
        self.topologicalSorting.append(node)



    class EdgeType:
        TREE = '_TREE_'
        BACK = '_BACK_'
        CROSS = '_CROSS_'
        FORWARD = '_FORWARD_'
