from modules.list_graph import Graph


class DirectionedListGraph(Graph):

    def __init__(self, nodesNumber, isMatrix=False):
        super().__init__(nodesNumber, isMatrix)
