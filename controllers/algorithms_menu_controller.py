from views.algorithms_menu import *
from views.main_menu import clearScreen

from data import graph_data as appData


from algorithms.bfs import *
from algorithms.dfs import *
from algorithms.dijkstra import *
from algorithms.prim import *

def renderView(view): return view()

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


# DFS
def classifyEdgesController(view): 
    graph = appData.getGraph()
    dfs = DepthFirstSearch(graph)
    while True:
        clearScreen()
        renderView(view)
        try:
            initialNode = int(input('VERTICE INICIAL: '))
            edgesTypes = dfs.getEdgesTypes(initialNode)
            clearScreen()
            if len(edgesTypes) > 0:
                print(f'PARTIDO DO VERTICE {initialNode}, A CLASSIFICACAO DAS ARESTAS É ESTA:')
                for edge in edgesTypes:
                    print(f'{edge["origin"]}, {edge["destiny"]} = {edge["type"]}') 
            else:
                print('O GRAFO NAO POSSUI ARESTAS!')
        except:
            clearScreen()
            print('VERTICE INVALIDO!')    
        finally:
            keepOn = input('\nDESEJA REALIZAR UMA NOVA EXECUCAO? DIGITE "1" PARA "SIM"\nR: ')
            if keepOn != '1':
                clearScreen()
                return
def hasCicleController(view): 
    graph = appData.getGraph()
    renderView(view)
    input()
    
def topologicalSortingController(view): 
    graph = appData.getGraph()
    renderView(view)
    input()

def strongerComponentsController(view): 
    graph = appData.getGraph()
    renderView(view)
    input()

# BFS
def shortestPathController(view): 
    graph = appData.getGraph()
    renderView(view)

# PRIM
def minimalSpanningTreeController(view): 
    graph = appData.getGraph()
    renderView(view)


# DIJKSTRA
def shortestPathToAllController(view): 
    graph = appData.getGraph()
    renderView(view)
