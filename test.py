from modules.matrix_directioned_graph import *
from modules.matrix_graph import *
from algorithms.dfs import DepthFirstSearch

g = MatrixGraph(5)

dfs = DepthFirstSearch(g)

print(dfs.colors)