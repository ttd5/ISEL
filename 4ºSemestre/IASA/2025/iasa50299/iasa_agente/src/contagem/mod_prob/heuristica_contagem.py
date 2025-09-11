from lib.pee.melhor_prim.heuristica import Heuristica

class HeuristicaContagem(Heuristica):
    def __init__(self, meta):
        self.__meta = meta

    def h(self, estado):
        return abs(self.__meta - estado.valor)