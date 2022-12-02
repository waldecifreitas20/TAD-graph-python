from modules.list_directioned_graph import *
from modules.list_graph import *
from modules.matrix_graph import *
from modules.matrix_directioned_graph import *

from algorithms.bfs import BreadthFirstSearch

from collections import deque


g = ListGraph(5)

g.addEdge(1,1)


dg = DirectionedListGraph(6)

dg.addEdge(0,1,weight=2)
dg.addEdge(0,2,weight=3)
dg.addEdge(0,4,weight=1)

dg.addEdge(2,3,weight=2)
dg.addEdge(1,3,weight=3)
dg.addEdge(1,2,weight=3)

dg.addEdge(3,5,weight=2)
dg.addEdge(3,4,weight=3)


bfs = BreadthFirstSearch(dg)
bfs.bfs()

print(bfs.discoveryTime)
print(bfs.visited)
print(bfs.ancestor)

""" 
dfs = DepthFirstSearch(dg)


r = dfs.getStrengthComponents(0)
print(r)
print(dfs.finalTime)
et = dfs.getEdgesTypes()

for edge in et:
    print(f'{edge["origin"]}, {edge["destiny"]} = {edge["type"]}') """