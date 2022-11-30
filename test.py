from modules.list_directioned_graph import *
from modules.list_graph import *
from algorithms.dfs import DepthFirstSearch

g = ListGraph(5)

g.addEdge(1,1)


dg = DirectionedListGraph(7)


dg.addEdge(1,2)
dg.addEdge(1,5)

dg.addEdge(2,5)
dg.addEdge(2,3)

dg.addEdge(3,6)

dg.addEdge(6,2)

dg.addEdge(5,6)

dg.addEdge(4,5)
dg.addEdge(4,1)

dfs = DepthFirstSearch(dg)


et = dfs.getEdgesTypes()
hasCicle = dfs.hasCicle()

print(hasCicle)