from collections import deque
from utils.colors import *

_MAX_VALUE_ = 9999999999999

class BreadthFirstSearch:

    def __init__(self, graph) -> None:
        self.graph = graph
        self.runtime = 0
        self.finalTime = []
        self.discoveryTime = []
        self.ancestor = []
        self.colors = []
      
        

    def _initVariables(self):
        numberNodes = self.graph.getNumberNodes()

        self.runtime = 0
        self.colors.clear()
        self.ancestor.clear()
        self.finalTime.clear()
        self.discoveryTime.clear()

        for i in range(numberNodes):
            self.colors.append(WHITE)
            self.ancestor.append(None)
            self.finalTime.append(_MAX_VALUE_)
            self.discoveryTime.append(_MAX_VALUE_)
            

    def bfs(self):
        self._initVariables()

        for node in range(self.graph.getNumberNodes()):
            if self.colors[node] == WHITE:
                self._bfsVisit(node)
                print('--------------------------')

    def _bfsVisit(self, node):
        self.runtime += 1
        self.discoveryTime = self.runtime
        self.colors[node] = GRAY

        adj = self.graph.getAdjacentsFrom(node)
        queue = deque(adj)

        while len(queue) > 0:
           pass


        self.runtime += 1
        self.finalTime = self.runtime
        self.colors[node] = BLACK



    



