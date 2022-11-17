from data import graph_data as appData
from modules.list_graph import *
from modules.list_directioned_graph import *
from modules.matrix_graph import *
from modules.matrix_directioned_graph import *
from utils.checkers import isValidMenuOption
from utils.menu_options import *
from views.menu import clearScreen


def renderView(view): return view()


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
        renderView(view)
        menuOption = input('SELECIONE UMA OPCAO: ')
        clearScreen()

        if (menuOption == '0'):
            break

        if (isValidMenuOption(menuOption, GENERATE_GRAPH_MENU_OPTIONS)):
            while True:
                try:
                    numberNodes = int(
                        input('DIGITE O NUMERO DE VERTICES DO GRAFO: '))
                    
                    # VERIFICA QUAL TIPO DE GRAFO GERAR
                    if (menuOption == '1'):
                        graph = DirectionedMatrixGraph(numberNodes)
                    elif (menuOption == '2'):
                        graph = DirectionedListGraph(numberNodes)
                    elif (menuOption == '3'):
                        graph = MatrixGraph(numberNodes)
                    elif (menuOption == '4'):
                        graph = ListGraph(numberNodes)

                    appData.saveGraph(graph)
                    clearScreen()
                    return
                except:
                    clearScreen()
                    print('DIGITE UMA OPCAO VALIDA')
        else:
            print('DIGITE UMA OPCAO VALIDA')

def addEdgeController(view):
    graph = appData.getGraph()
    if graph == None:
        print('O GRAFO ESTA VAZIO. SELECIONE A PRIMEIRA OPCAO E GERE UM GRAFO')
    else:
        while True:
            renderView(view)
            try:
                fromNode = int(input('VERTICE ORIGEM: '))
                toNode = int(input('VERTICE DESTINO: '))
                edgeWeight = int(input('PESO DA ARESTA: '))
                if(edgeWeight == '0'):
                    edgeWeight = '1'
                graph.addEdge(fromNode, toNode, edgeWeight)
                appData.saveGraph(graph)
                print('ARESTA ADICIONADA COM SUCESSO!')
            except Exception as error:
                clearScreen()
                print(error)
            finally:
                keepOn = input('DESEJA ADCIONAR MAIS ARESTAS? (1 - SIM)\nR: ')
                clearScreen()
                if(keepOn != '1'):
                    break

def removeEdgeController(view): pass
def hasEdgeController(view): pass

def showGraphController(view): 
    graph = appData.getGraph()
    graph.printGraph()
    input('\nAPERTE ENTER PARA CONTINAR')
    clearScreen()

def showEdgeAndNodesController(view): pass
def checkNodeDegreeController(view): pass
def runAlgorithmsController(view): pass
