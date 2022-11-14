from data import graph_data as appData
from modules.graph import *
from utils.checkers import isValidMenuOption
from utils.menu_options import *
from views.menu import clearScreen


def runView(view): return view()

def getViewController(menuOption, views):
    if (menuOption == '1'):
        return (
            views.generateGraphMenu,
            generateGraphController,
        )

    if (menuOption == '2'):
        return (
            views.addEdgeMenu,
            addEdgeController,
        )

    if (menuOption == '3'):
        return (
            views.removeEdgeMenu,
            removeEdgeController
        )

    if (menuOption == '4'):
        return (
            views.hasEdgeMenu,
            hasEdgeController
        )

    if (menuOption == '5'):
        return (
            views.showGraphMenu,
            showGraphController
        )

    if (menuOption == '6'):
        return (
            views.showEdgeAndNodesLengthMenu,
            showEdgeAndNodesController
        )

    if (menuOption == '7'):
        return (
            views.checkNodeDegreeMenu,
            checkNodeDegreeController
        )

    if (menuOption == '8'):
        return (
            views.runAlgorithmsMenu,
            runAlgorithmsController
        )

def generateGraphController(view):
    MENU_OPTION = -1

    while MENU_OPTION != 0:
        runView(view)
        MENU_OPTION = input('SELECIONE UMA OPCAO: ')
        clearScreen()

        if(MENU_OPTION == '0'):
            break

        if (isValidMenuOption(MENU_OPTION, GENERATE_GRAPH_MENU_OPTIONS)):
                while True:
                    try:
                        numberNodes = int(input('DIGITE O NUMERO DE VERTICES DO GRAFO: ')) 
                        if(MENU_OPTION == '1'):
                            graph = Graph(numberNodes)
                        else:
                            graph = Graph(numberNodes)
                        appData.saveGraph(graph)
                        break                        
                    except:
                        clearScreen()
                        print('DIGITE UMA OPCAO VALIDA')
                  

def addEdgeController(view): pass
def removeEdgeController(view): pass
def hasEdgeController(view): pass
def showGraphController(view): pass
def showEdgeAndNodesController(view): pass
def checkNodeDegreeController(view): pass
def runAlgorithmsController(view): pass
