from modules.list_directioned_graph import *
from modules.list_graph import *
from modules.matrix_graph import *
from modules.matrix_directioned_graph import *
from algorithms.dfs import DepthFirstSearch

g = ListGraph(5)

g.addEdge(1,1)


dg = DirectionedListGraph(9)

dg.addEdge(1,2)
dg.addEdge(2,7)
dg.addEdge(7,1)
dg.addEdge(7,3)
dg.addEdge(3,1)

dg.addEdge(3,4)
dg.addEdge(7,8)
dg.addEdge(2,5)


dg.addEdge(5,8)
dg.addEdge(8,4)
dg.addEdge(4,6)
dg.addEdge(6,5)




dfs = DepthFirstSearch(dg)


r = dfs.getStrengthComponents(0)
print(r)
print(dfs.finalTime)
""" et = dfs.getEdgesTypes()

for edge in et:
    print(f'{edge["origin"]}, {edge["destiny"]} = {edge["type"]}') """