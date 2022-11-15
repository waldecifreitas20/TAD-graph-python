from modules.list_graph import *

_graph = Graph


def saveGraph(graph=Graph):
    global _graph
    _graph = graph


def getGraph() -> Graph:
    global _graph
    return _graph
