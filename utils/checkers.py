from modules.list_directioned_graph import DirectionedListGraph
from modules.matrix_directioned_graph import DirectionedMatrixGraph


def isValidMenuOption(choice, options):
    return options.__contains__(choice)


def isDirectionedGraph(graph):
    isDirectionedList = isinstance(graph, DirectionedListGraph)
    isDirectionedMatrix = isinstance(graph, DirectionedMatrixGraph)
    
    return isDirectionedList or isDirectionedMatrix

def indexOf(match, list):
    try:
        return list.index(match)
    except:
        return -1