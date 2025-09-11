from math import dist
from pee.melhor_prim.heuristica import Heuristica

class HeurDist(Heuristica):
    """
    Implementa uma heurística baseada na distância euclidiana para o planejamento em espaços de estados.
    Esta heurística calcula a distância entre o estado atual e o estado final para estimar a proximidade do objetivo.
    """
    def __init__(self, estado_final):
        """
        Inicializa a heurística com o estado final.

        O estado final é utilizado para calcular a distância euclidiana em relação ao estado atual,
        indicando o quanto o estado atual está distante do objetivo.
        """
        self.__estado_final = estado_final  # Armazena o estado final para os cálculos subsequentes

    def h(self, estado):
        """
        Calcula a distância entre o estado atual e o estado final.

        O valor heurístico é baseado na distância euclidiana entre as posições do estado atual
        e do estado final, usando a função `dist` do módulo `math`.
        """
        return dist(estado.posicao, self.__estado_final.posicao)  # Retorna a distância entre os estados
