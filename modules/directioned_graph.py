from modules.graph import Graph


class DirectionedGraph(Graph):

    def __init__(self, nodesNumber, isMatrix=False):
        super().__init__(nodesNumber, isMatrix)
