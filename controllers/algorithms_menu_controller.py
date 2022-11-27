from views.algorithms_menu import *
from data import graph_data as appData
from algorithms import *

def renderView(view): return view(view)

def getAlgorithmViewController(option):
    if option == 1:
        return (
            classifyEdgesMenu, classifyEdgesController
        )
    if option == 2:
        return (
            hasCicleMenu, hasCicleController
        )
    if option == 3:
        return (
            topologicalSortingMenu, topologicalSortingController
        )
    if option == 4:
        return (
            strongerComponentsMenu, strongerComponentsController
        )
    if option == 5:
        return (
            shortestPathMenu, shortestPathController
        )
    if option == 6:
        return (
            minimalSpanningTreeMenu, minimalSpanningTreeController
        )
    if option == 7:
        return (
            shortestPathToAllMenu, shortestPathToAllController
        )


def classifyEdgesController(view): 
    graph = appData.getGraph()
def hasCicleController(view): 
    graph = appData.getGraph()
    
def topologicalSortingController(view): 
    graph = appData.getGraph()
def strongerComponentsController(view): 
    graph = appData.getGraph()


def shortestPathController(view): 
    graph = appData.getGraph()


def minimalSpanningTreeController(view): 
    graph = appData.getGraph()


def shortestPathToAllController(view): 
    graph = appData.getGraph()
