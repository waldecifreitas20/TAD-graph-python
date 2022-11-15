class UnexistingNodeException(Exception):
    def __init__(self):
        super().__init__('AMBOS OS VERTICES DEVEM FAZER PARTE DO GRAFO!')