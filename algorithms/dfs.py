from utils.colors import *

_MAX_VALUE_ = 999999999

class DepthFirstSearch:

    def __init__(self, graph) -> None:
        self.graph = graph
        self.colors = []
        self.dicoveryTime = []
        self.finalTime = []
        self.runtime = 0
        self._initVariables()

    def _initVariables(self):
        for _ in range(self.graph.getNumberNodes()):
            self.colors.append(WHITE)
            self.dicoveryTime.append(_MAX_VALUE_)
            self.finalTime.append(_MAX_VALUE_)
    
