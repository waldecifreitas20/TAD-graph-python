from modules.list_directioned_graph import *
from modules.list_graph import *
from algorithms.dfs import DepthFirstSearch

g = ListGraph(5)

g.addEdge(1,1)


dg = DirectionedListGraph(3)


dg.addEdge(1,0)
dg.addEdge(1,2)



dfs = DepthFirstSearch(dg)


r = dfs.getTopologicalSorting(2)
print(r)
print(dfs.discoveryTime)
print(dfs.finalTime)
""" 
for edge in et:
    print(f'{edge["origin"]}, {edge["destiny"]} = {edge["type"]}') """