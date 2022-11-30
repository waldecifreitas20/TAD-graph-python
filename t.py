import algorithms.dfs as DFS
import algorithms.bfs as bfs
import algorithms.dijkstra as dijkstra
import algorithms.prim as prim

from modules.list_directioned_graph import *
from modules.matrix_directioned_graph import *
from modules.list_graph import *
from modules.matrix_graph import *

g = DirectionedListGraph(6)
g.addEdge(0,1)
g.addEdge(0,4)
g.addEdge(1,2)
""" 
g.addEdge(1,4)

g.addEdge(2,3)

g.addEdge(3,1)

g.addEdge(4,3)

g.addEdge(5,0)
g.addEdge(5,4)
 """


DFS.classifyEdges(g)


print(DFS.finalTime)
