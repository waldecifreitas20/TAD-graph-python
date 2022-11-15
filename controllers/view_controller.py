from data import graph_data as appData
from modules.directioned_graph import *
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
    menuOption = -1

    while menuOption != 0:
        runView(view)
        menuOption = input('SELECIONE UMA OPCAO: ')
        clearScreen()

        if (menuOption == '0'):
            break

        if (isValidMenuOption(menuOption, GENERATE_GRAPH_MENU_OPTIONS)):
            while True:
                try:
                    numberNodes = int(input('DIGITE O NUMERO DE VERTICES DO GRAFO: '))
                    
                    if (menuOption == '1'):
                        graph = DirectionedGraph(numberNodes, isMatrix=True)
                    elif (menuOption == '2'):
                        graph = DirectionedGraph(numberNodes)
                    elif (menuOption == '3'):
                        graph = Graph(numberNodes, isMatrix=True)
                    elif (menuOption == '4'):
                        graph = Graph(numberNodes)

                    appData.saveGraph(graph)
                    clearScreen()
                    return
                except:
                    clearScreen()
                    print('DIGITE UMA OPCAO VALIDA')
        else:
            print('DIGITE UMA OPCAO VALIDA')

def addEdgeController(view):
    graph = Graph
    while True:
        runView(view)
        fromNode = input('VERTICE ORIGEM: ')
        toNode = input('VERTICE DESTINO: ')
                
        try:
            graph = appData.getGraph()
            graph.addNode(fromNode, toNode)
        except Exception as error:
            clearScreen()
            print(error)
        finally:
            keepOn = input('DESEJA ADCIONAR MAIS ARESTAS? (1 - SIM)\nR: ')
            clearScreen()
            if(keepOn != '1'):
                break

    appData.saveGraph(graph)

def removeEdgeController(view): pass
def hasEdgeController(view): pass
def showGraphController(view): pass
def showEdgeAndNodesController(view): pass
def checkNodeDegreeController(view): pass
def runAlgorithmsController(view): pass
