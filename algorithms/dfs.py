from modules.graph import *
from utils.colors import *


colors = []
discoveryTime = []
finalTime = []
ancestor = []
runtime = 0
graph = Graph


def _initVariables(_graph):
    global colors, discoveryTime, finalTime, anchestor, runtime, graph
    runtime = 0
    graph = _graph
    for _ in range(_graph.getNumberNodes()):
        colors.append(WHITE)
        discoveryTime.append(0)
        finalTime.append(0)
        ancestor.append(None)



def classifyEdges(graph=Graph):
    global colors
    _initVariables(graph)
    nodes = graph.getNumberNodes()
    for i in range(nodes):
        if colors[i] == WHITE:
            _classifyEdgesVisit(i)


def _classifyEdgesVisit(index):
    global colors, discoveryTime, finalTime, ancestor, runtime, graph

    runtime += 1
    colors[index] = GRAY
    discoveryTime[index] = runtime

    adjacents = graph.getAdjacentsFrom(index)
    adjacents.sort(reverse=True)
    if len(adjacents) != 0:
        destinyNode = adjacents.pop()
        
        while destinyNode != None:
            if colors[destinyNode] == WHITE:
                ancestor[destinyNode] = index
                _classifyEdgesVisit(destinyNode)
            try:
                destinyNode = adjacents.pop()
            except:
                destinyNode = None

    colors[index] = BLACK
    runtime += 1
    finalTime[index]= runtime
