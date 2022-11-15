if __name__ == '__main__':
    from matrix_graph import *
else:
    from modules.matrix_graph import *



class DirectionedMatrixGraph(MatrixGraph):

    def __init__(self, nodesNumber):
        super().__init__(nodesNumber)