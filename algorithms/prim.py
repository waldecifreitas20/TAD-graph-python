from utils.tools import sortIndexesOfMaxValue

_MAX_INT_ = 999999999999

class Prim:

    def __init__(self, graph) -> None:
        self.graph = graph
        self.ancestor = []
        self.edgesWeight = []
        self.nodes = []

    def _initVariables(self):
        self.ancestor.clear()
        self.edgesWeight.clear()
        
        for _ in range(self.graph.getNumberNodes()):
            self.ancestor.append(None)
            self.edgesWeight.append(_MAX_INT_)
        

    def getMinimalSpanningTree(self, initialNode):
        self._initVariables()
        edges = self.graph.edges
        heap = 0

        print(heap)
