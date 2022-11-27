from modules.graph import *
from utils.checkers import (isDirectionedGraph, indexOf)
from utils.colors import *
from utils.edges_types import *

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


edgesTypes = []
treeNodes = []


def dfs(graph)
    global colors
    _initVariables(graph)
    nodes = graph.getNumberNodes()
    for i in range(nodes):
        if colors[i] == WHITE:
            _dfsVisit(i)


def _dfsVisit(index):
    global colors, discoveryTime, finalTime, ancestor, runtime, graph, edgesTypes, treeNodes

    runtime += 1
    colors[index] = GRAY
    treeNodes.append(index)
    discoveryTime[index] = runtime

    adjacents = graph.getAdjacentsFrom(index)
    adjacents.sort(reverse=True)

    if len(adjacents) != 0:
        destinyNode = adjacents.pop()

        while destinyNode != None:
            if colors[destinyNode] == WHITE:
                edgesTypes.append([index, destinyNode, TREE])
                ancestor[destinyNode] = index
                _classifyEdgesVisit(destinyNode)
            else:
                # VERIFICA SE É UMA ARESTA DE RETORNO
                if indexOf(destinyNode, ancestor) != -1:
                    edgesTypes.append([index, destinyNode, RETURN])

                # VERIFICA SE É UMA ARESTA DE AVANÇO
                if isDirectionedGraph(graph):
                    if ancestor[destinyNode] == None and :
                        edgesTypes.append([index, destinyNode, NEXT])
                    else:
                        edgesTypes.append([index, destinyNode, CROSSING])

            try:
                destinyNode = adjacents.pop()
            except:
                destinyNode = None

    colors[index] = BLACK
    runtime += 1
    finalTime[index] = runtime


def classifyEdges(graph=Graph):
    global colors
    _initVariables(graph)
    nodes = graph.getNumberNodes()
    for i in range(nodes):
        if colors[i] == WHITE:
            _classifyEdgesVisit(i)


def _classifyEdgesVisit(index):
    global colors, discoveryTime, finalTime, ancestor, runtime, graph, edgesTypes, treeNodes

    runtime += 1
    colors[index] = GRAY
    treeNodes.append(index)
    discoveryTime[index] = runtime

    adjacents = graph.getAdjacentsFrom(index)
    adjacents.sort(reverse=True)

    if len(adjacents) != 0:
        destinyNode = adjacents.pop()

        while destinyNode != None:
            if colors[destinyNode] == WHITE:
                edgesTypes.append([index, destinyNode, TREE])
                ancestor[destinyNode] = index
                _classifyEdgesVisit(destinyNode)
            else:
                # VERIFICA SE É UMA ARESTA DE RETORNO
                if indexOf(destinyNode, ancestor) != -1:
                    edgesTypes.append([index, destinyNode, RETURN])

                # VERIFICA SE É UMA ARESTA DE AVANÇO
                if isDirectionedGraph(graph):
                    if ancestor[destinyNode] == None and :
                        edgesTypes.append([index, destinyNode, NEXT])
                    else:
                        edgesTypes.append([index, destinyNode, CROSSING])

            try:
                destinyNode = adjacents.pop()
            except:
                destinyNode = None

    colors[index] = BLACK
    runtime += 1
    finalTime[index] = runtime
