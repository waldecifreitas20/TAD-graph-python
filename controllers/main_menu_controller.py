from data import graph_data as appData
from modules.list_graph import *
from modules.list_directioned_graph import *
from modules.matrix_graph import *
from modules.matrix_directioned_graph import *
from utils.checkers import *
from utils.menu_options import *
from views.menu import *
from controllers.algorithms_menu_controller import *

def renderView(view): return view()


def getMenuViewController(menuOption):
    if (menuOption == '1'):
        return (
            generateGraphMenu,
            generateGraphMenuController,
        )

    if (menuOption == '2'):
        return (
            addEdgeMenu,
            addEdgeMenuController,
        )

    if (menuOption == '3'):
        return (
            removeEdgeMenu,
            removeEdgeMenuController
        )

    if (menuOption == '4'):
        return (
            hasEdgeMenu,
            hasEdgeMenuController
        )

    if (menuOption == '5'):
        return (
            showGraphMenu,
            showGraphMenuController
        )

    if (menuOption == '6'):
        return (
            showEdgeAndNodesLengthMenu,
            showEdgeAndNodesMenuController
        )

    if (menuOption == '7'):
        return (
            checkNodeDegreeMenu,
            checkNodeDegreeMenuController
        )

    if (menuOption == '8'):
        return (
            runAlgorithmsMenu,
            runAlgorithmsMenuController
        )
    if (menuOption == '9'):
        return (
            showAdjacentsMenu,
            showAdjacentsMenuController
        )


def generateGraphMenuController(view):
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


def addEdgeMenuController(view):
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


def removeEdgeMenuController(view):
    graph = appData.getGraph()
    if graph == None:
        print('O GRAFO ESTA VAZIO. SELECIONE A PRIMEIRA OPCAO E GERE UM GRAFO')
    else:
        while True:
            renderView(view)
            try:
                fromNode = int(input('VERTICE ORIGEM: '))
                toNode = int(input('VERTICE DESTINO: '))
                graph.removedge(fromNode, toNode)
                appData.saveGraph(graph)
                print('ARESTA REMOVIDA COM SUCESSO')
            except Exception as error:
                clearScreen()
                print(error)
            finally:
                keepOn = input('DESEJA REMOVAR MAIS ARESTAS? (1 - SIM)\nR: ')
                clearScreen()
                if(keepOn != '1'):
                    break


def hasEdgeMenuController(view):
    graph = appData.getGraph()
    while True:
        renderView(view)
        try:
            fromNode = int(input('VERTICE ORIGEM: '))
            toNode = int(input('VERTICE DESTINO: '))
            clearScreen()
            if graph.hasEdge(fromNode, toNode):
                print(f'A ARESTA {fromNode} -> {toNode} EXISTE NO GRAFO!')
            else:
                print(f'A ARESTA {fromNode} -> {toNode} NAO EXISTE NO GRAFO!')
        except Exception as error:
            clearScreen()
            print(error)
            print(f'A ARESTA {fromNode} -> {toNode} NAO EXISTE NO GRAFO!')
        finally:
            keepOn = input('DESEJA REALIZAR UMA NOVA CONSULTA? (1 - SIM)\nR: ')
            clearScreen()
            if(keepOn != '1'):
                break


def showGraphMenuController(view):
    graph = appData.getGraph()
    graph.printGraph()
    input('\nAPERTE ENTER PARA CONTINAR')
    clearScreen()


def showEdgeAndNodesMenuController(view):
    graph = appData.getGraph()
    clearScreen()
    renderView(view)
    print('O GRAFO ATUAL CONTEM: ')
    print(F'{graph.getNumberNodes()} VERTICES E {graph.getNumberEdges()} ARESTAS')
    input('\nAPERTE ENTER PARA CONTINUAR...')


def checkNodeDegreeMenuController(view):
    graph = appData.getGraph()
    while True:
        renderView(view)
        try:
            nodeValue = int(input('VERTICE: '))
            clearScreen()
            if isDirectionedGraph(graph):
                degreeIn = graph.getDegreeIn(nodeValue)
                degreeOut = graph.getDegreeOut(nodeValue)
                print(f'GRAU DE ENTRADA DO VERTICE {nodeValue}: {degreeIn}')
                print(f'GRAU DE SAIDA DO VERTICE {nodeValue}: {degreeOut}')
            else:
                nodeDegree = graph.getNodeDegree(nodeValue)
                print(f'GRAU DO VERTICE {nodeValue}: {nodeDegree}')
        except Exception as error:
            clearScreen()
            print(error)
        finally:
            keepOn = input('DESEJA REALIZAR UMA NOVA CONSULTA? (1 - SIM)\nR: ')
            clearScreen()
            if(keepOn != '1'):
                break


def showAdjacentsMenuController(view):
    graph = appData.getGraph()
    while True:
        renderView(view)
        try:
            nodeValue = int(input('VERTICE: '))
            adjacents = graph.getAdjacentsFrom(nodeValue)
            print(f'LISTA DE ADJACENCIAS: {adjacents}')
        except Exception as error:
            print(error)
        finally:
            keepOn = input('DESEJA REALIZAR UMA NOVA CONSULTA? (1 - SIM)\nR: ')
            clearScreen()
            if(keepOn != '1'):
                break


def runAlgorithmsMenuController(view): 
  pass
