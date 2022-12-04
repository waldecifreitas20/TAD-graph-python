from collections import deque
from utils.tools import sortEdgesByWeight

_MAX_VALUE_ = 9999999999999

class BreadthFirstSearch:

    def __init__(self, graph) -> None:
        self.graph = graph
        self.runtime = 0
        self.discoveryTime = []
        self.ancestor = []
        self.visited = []
              

    def _initVariables(self):
        numberNodes = self.graph.length()

        self.runtime = 0
        self.visited.clear()
        self.ancestor.clear()
     
        self.discoveryTime.clear()

        for i in range(numberNodes):
            self.visited.append(False)
            self.ancestor.append(None)
            self.discoveryTime.append(-1)
            

    def bfs(self, initialNode=0):
        self._initVariables()

        queue = deque([initialNode])
        self.visited[initialNode] = True
        self.discoveryTime[initialNode] = 0
        while len(queue) > 0:
            self.runtime += 1
            node = queue.popleft()
            adjacents = self.graph.getAdjacentsFrom(node)

            edges = []
            for destinyNode in adjacents:
                edge = self.graph.getEdge(node, destinyNode)
                edges.append(edge)

            edges = sortEdgesByWeight(edges)
            for edge in edges:
                destinyNode = edge.toNode   
                if not self.visited[destinyNode]:
                    self.discoveryTime[destinyNode] = self.runtime
                    queue.append(destinyNode)
                    self.visited[destinyNode] = True
                    self.ancestor[destinyNode] = node

        
    def getPathBetween(self, origin, destiny):
        self.bfs(origin)
        path = []
        node = destiny

        while node != origin or node == -1:
            path.append(node)
            next = self.ancestor[node]
            node = next
        
        path.reverse()
        return path
     



    



