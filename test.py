from modules.list_directioned_graph import *
from modules.list_graph import *
from modules.matrix_graph import *
from modules.matrix_directioned_graph import *

from algorithms.bfs import BreadthFirstSearch

from collections import deque


g = ListGraph(5)

g.addEdge(1,1)


dg = DirectionedListGraph(4)

dg.addEdge(0,1)
dg.addEdge(0,2)
dg.addEdge(1,2)
dg.addEdge(2,3)
dg.addEdge(3,3)
dg.addEdge(2,0)


bfs = BreadthFirstSearch(dg)

bfs.bfs()

""" 
dfs = DepthFirstSearch(dg)


r = dfs.getStrengthComponents(0)
print(r)
print(dfs.finalTime)
et = dfs.getEdgesTypes()

for edge in et:
    print(f'{edge["origin"]}, {edge["destiny"]} = {edge["type"]}') """