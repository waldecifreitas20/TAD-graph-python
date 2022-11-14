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
    print('0 - SAIR DO PROGRAMA')

def generateGraphMenu():
    print(_THICK_BORDER)
    print('      SELECIONE A ACAO DESEJADA')
    print(_THICK_BORDER)
    print('1 - GERAR GRAFO DIRECIONADO')
    print('2 - GERAR GRAFO NAO DIRECIONADO')
    print('0 - VOLTAR PARA O MENU PRINCIPAL')
    print(_THICK_BORDER)

def generateDirectionedGraphMenu():
    print(_THICK_BORDER)
    print('      SELECIONE A ACAO DESEJADA')
    print(_THICK_BORDER)
    print('1 - ')
    print('2 - GERAR GRAFO NAO DIRECIONADO')
    print('0 - VOLTAR PARA O MENU PRINCIPAL')
    print(_THICK_BORDER)


def addEdgeMenu(nodeSourceName = ''):
    print(_THICK_BORDER)
    print(f'INSIRA O VALOR DO NO {nodeSourceName.upper()}')
    print(_THICK_BORDER)


def removeEdgeMenu():
    print(_THICK_BORDER)
    print('0 - VOLTAR PARA O MENU PRINCIPAL')
    print(_THICK_BORDER)


def hasEdgeMenu():
    print(_THICK_BORDER)
    print('0 - VOLTAR PARA O MENU PRINCIPAL')
    print(_THICK_BORDER)


def showGraphMenu():
    print(_THICK_BORDER)
    print('0 - VOLTAR PARA O MENU PRINCIPAL')
    print(_THICK_BORDER)


def showEdgeAndNodesLengthMenu():
    print(_THICK_BORDER)
    print('0 - VOLTAR PARA O MENU PRINCIPAL')
    print(_THICK_BORDER)


def checkNodeDegreeMenu():
    print(_THICK_BORDER)
    print('0 - VOLTAR PARA O MENU PRINCIPAL')
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
    print('    6 - CAMINHO MINIMO DE UM VERTICE PARA QUALQUER OUTRO')
    print('0 - VOLTAR PARA O MENU PRINCIPAL')
    print(_THICK_BORDER)
