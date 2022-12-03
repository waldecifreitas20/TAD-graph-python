from modules.list_directioned_graph import *
from modules.list_graph import *
from modules.matrix_graph import *
from modules.matrix_directioned_graph import *

from algorithms.prim import Prim

from collections import deque


g = ListGraph(5)

g.addEdge(1,1)


dg = MatrixGraph(6)

dg.addEdge(0,1,weight=6)
dg.addEdge(0,2,weight=1)
dg.addEdge(0,3,weight=5)

dg.addEdge(1,4,weight=5)
dg.addEdge(3,5,weight=4)


dg.addEdge(2,1,weight=2)
dg.addEdge(2,3,weight=2)
dg.addEdge(2,4,weight=6)
dg.addEdge(2,5,weight=4)

dg.addEdge(4,5,weight=3)

""" 
 """

prim = Prim(dg)

tree = prim.getMinimalSpanningTree()
tree.printGraph()


""" 
bfs = BreadthFirstSearch(dg)
bfs.bfs()
path = bfs.getPathBetween(0,6)


print(path) """

""" 
dfs = DepthFirstSearch(dg)


r = dfs.getStrengthComponents(0)
print(r)
print(dfs.finalTime)
et = dfs.getEdgesTypes()

for edge in et:
    print(f'{edge["origin"]}, {edge["destiny"]} = {edge["type"]}') """