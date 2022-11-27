from views.algorithms_menu import *

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


def classifyEdgesController(view): pass
def hasCicleController(view): pass
def topologicalSortingController(view): pass
def strongerComponentsController(view): pass


def shortestPathController(view): pass


def minimalSpanningTreeController(view): pass


def shortestPathToAllController(view): pass
