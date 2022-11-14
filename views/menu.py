from os import (
    system as runCommand,
    name as operationalSystem
)

WINDOWS = 'nt'
THICK_BORDER = '========================================================'
THIN_BORDER = '--------------------------------------------------------'

def clearScreen(): 
    if operationalSystem == WINDOWS:
        runCommand('cls')
    else:
        runCommand('clear')

def renderMainMenu():
    print(THICK_BORDER)
    print('      MENU PRINCIPAL')
    print(THICK_BORDER)
    _renderMainMenuOptions()
    print(THICK_BORDER)

def _renderMainMenuOptions():
    print('1 - GERAR NOVO GRAFO')
    print('2 - ADICIONAR ARESTA')
    print('3 - REMOVER ARESTA')
    print('4 - CHECAR EXISTENCIA DE ARESTA')
    print('5 - MOSTRAR GRAFO')
    print('6 - VER QUANTIDADE DE ARESTAS E VERTICES')
    print('7 - CHECAR GRAU DE UM VERTICE')
    print('8 - EXECUTAR ALGORITMOS')
    print('0 - SAIR DO PROGRAMA')

def generateGraphMenu():
    print(THICK_BORDER)
    print('      SELECIONE A ACAO DESEJADA')
    print(THICK_BORDER)
    print('1 - GERAR GRAFO DIRECIONADO')
    print('2 - GERAR GRAFO NAO DIRECIONADO')
    print('3 - VOLTAR PARA O MENU PRINCIPAL')
    print(THICK_BORDER)

def addEdgeMenu():
    print(THICK_BORDER)
    print('INSIRA')
    print(THICK_BORDER)


def removeEdgeMenu():
    pass

def checkEdgeExistenceMenu():
    pass

def showGraphMenu():
    pass

def showEdgeAndNodesLengthMenu():
    pass

def checkNodeDegreeMenu():
    pass

def runAlgorithmsMenu():
    print(THICK_BORDER)
    print('OBS: OS ITENS COM "#" NAO SAO SELECIONAVEIS. APENAS')
    print('INDICAM O ALGORITMO UTILIZADO PARA REALIZAR A TAREFA')
    print(THICK_BORDER)
    print('# - BUSCA EM PROFUNDIDADE')
    print('    1 - CLASSIFICACAO DE ARESTAS')
    print('    2 - VERIFICACAO DE CICLO')
    print('    3 - ORDENACAO TOPOLOGICA')
    print('    4 - COMPONENTES FORTEMENTE CONECTADOS')
    print(THIN_BORDER)
    print('# - BUSCA EM LARGURA')
    print('    5 - CAMINHO CURTO ENTRE UM PAR DE VERTICES')
    print(THIN_BORDER)
    print('# - ALGORITMO PRIM')
    print('    6 - ARVORE GERADORA MINIMA')
    print(THIN_BORDER)
    print('# - ALGORITMO DIJKSTRA')
    print('    6 - CAMINHO MINIMO DE UM VERTICE PARA QUALQUER OUTRO')
    print(THICK_BORDER)
