from modules.list_directioned_graph import *
from modules.list_graph import *
from algorithms.dfs import DepthFirstSearch

g = ListGraph(5)

g.addEdge(1,1)


dg = DirectionedListGraph(3)


dg.addEdge(1,2)
dg.addEdge(1,0)



dfs = DepthFirstSearch(dg)


et = dfs.getEdgesTypes(6)
hasCicle = dfs.hasCicle()
r = dfs.getTopologicalSorting()
for edge in et:
    print(f'{edge["origin"]}, {edge["destiny"]} = {edge["type"]}')