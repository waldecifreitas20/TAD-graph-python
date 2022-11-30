from os import name as _operationalSystem
from os import system as _runCommand

_WINDOWS = 'nt'
_THICK_BORDER = '========================================================'
_THIN_BORDER = '--------------------------------------------------------'


def clearScreen():
    if _operationalSystem == _WINDOWS:
        _runCommand('cls')
    else:
        _runCommand('clear')


def renderMainMenu():
    print(_THICK_BORDER)
    print('      MENU PRINCIPAL')
    print(_THICK_BORDER)
    _renderMainMenuOptions()
    print(_THICK_BORDER)


def _renderMainMenuOptions():
    print('1 - GERAR NOVO GRAFO')
    print('2 - ADICIONAR ARESTA')
    print('3 - REMOVER ARESTA')
    print('4 - CHECAR EXISTENCIA DE ARESTA')
    print('5 - MOSTRAR GRAFO')
    print('6 - VER QUANTIDADE DE ARESTAS E VERTICES')
    print('7 - CHECAR GRAU DE UM VERTICE')
    print('8 - EXECUTAR ALGORITMOS')
    print('9 - LISTA DE ADJACENCIAS')
    print('0 - SAIR DO PROGRAMA')


def generateGraphMenu():
    print(_THICK_BORDER)
    print('      SELECIONE A ACAO DESEJADA')
    print(_THICK_BORDER)
    print('1 - GERAR GRAFO DIRECIONADO (MATRIZ)')
    print('2 - GERAR GRAFO DIRECIONADO (LISTA DE ADJACENCIAS)')
    print('3 - GERAR GRAFO NAO DIRECIONADO (MATRIZ)')
    print('4 - GERAR GRAFO NAO DIRECIONADO (LISTA DE ADJACENCIAS)')
    print('0 - VOLTAR PARA O MENU PRINCIPAL')
    print(_THICK_BORDER)


def _edgesOperationsMenu():
    print(_THICK_BORDER)
    print('INSIRA OS VERTICES DA ARESTA')
    print(_THIN_BORDER)
    print('OBS: OS VERTICES DEVEM SER NUMERICOS')
    print(_THICK_BORDER)


def addEdgeMenu():
    _edgesOperationsMenu()


def removeEdgeMenu():
    _edgesOperationsMenu()


def hasEdgeMenu():
    _edgesOperationsMenu()


def showGraphMenu():
    print(_THICK_BORDER)
    print('0 - VOLTAR PARA O MENU PRINCIPAL')
    print(_THICK_BORDER)


def showEdgeAndNodesLengthMenu(): 
    print(_THICK_BORDER)
    print('INFORMACOES')
    print(_THICK_BORDER)



def checkNodeDegreeMenu():
    print(_THICK_BORDER)
    print('INSIRA O VALOR DO VERTICE')
    print(_THICK_BORDER)


def runAlgorithmsMenu():
    print(_THICK_BORDER)
    print('OBS: OS ITENS COM "#" NAO SAO SELECIONAVEIS. APENAS')
    print('INDICAM O ALGORITMO UTILIZADO PARA REALIZAR A TAREFA')
    print(_THICK_BORDER)
    print('# - BUSCA EM PROFUNDIDADE')
    print('    1 - CLASSIFICACAO DE ARESTAS')
    print('    2 - VERIFICACAO DE CICLO')
    print('    3 - ORDENACAO TOPOLOGICA')
    print('    4 - COMPONENTES FORTEMENTE CONECTADOS')
    print(_THIN_BORDER)
    print('# - BUSCA EM LARGURA')
    print('    5 - CAMINHO CURTO ENTRE UM PAR DE VERTICES')
    print(_THIN_BORDER)
    print('# - ALGORITMO PRIM')
    print('    6 - ARVORE GERADORA MINIMA')
    print(_THIN_BORDER)
    print('# - ALGORITMO DIJKSTRA')
    print('    7 - CAMINHO MINIMO DE UM VERTICE PARA QUALQUER OUTRO')
    print('0 - VOLTAR PARA O MENU PRINCIPAL')
    print(_THICK_BORDER)


def showAdjacentsMenu():
    print(_THICK_BORDER)
    print('INSIRA O VALOR DO VERTICE')
    print(_THICK_BORDER)