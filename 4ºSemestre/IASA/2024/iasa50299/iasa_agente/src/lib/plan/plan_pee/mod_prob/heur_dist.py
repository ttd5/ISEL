from lib.pee.melhor_prim.heuristica import Heuristica
import math

class HeurDist(Heuristica):
    """Implementação da heurística de distância euclidiana."""

    def __init__(self, estado_final):
        """Inicializa a heurística com o estado final."""
        self.__estado_final = estado_final

    def h(self, estado):
        """Calcula a distância euclidiana entre o estado atual e o estado final."""
        return math.dist(self.__estado_final.posicao, estado.posicao)
