from modules.list_directioned_graph import *
from modules.list_graph import *
from algorithms.dfs import DepthFirstSearch

g = ListGraph(5)

g.addEdge(1,1)


dg = DirectionedListGraph(10)

dg.addEdge(0,1)
dg.addEdge(0,5)
dg.addEdge(0,3)
dg.addEdge(0,2)

dg.addEdge(1,2)

dg.addEdge(2,3)
dg.addEdge(2,4)

dg.addEdge(4,6)

dg.addEdge(5,4)
dg.addEdge(5,6)

dg.addEdge(6,7)
dg.addEdge(6,8)

dg.addEdge(7,8)

dg.addEdge(9,6)


dfs = DepthFirstSearch(dg)


r = dfs.getTopologicalSorting(0)
print(r)

""" 
for edge in et:
    print(f'{edge["origin"]}, {edge["destiny"]} = {edge["type"]}') """