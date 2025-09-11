"""
Problema
@author: Tatiana Damaya
"""

from abc import ABC, abstractmethod

class Problema(ABC):
    """
    Classe abstrata que representa um problema genérico num espaço de estados.

    Um problema é definido por:
    - Um estado inicial.
    - Um conjunto de operadores (ações possíveis).
    - Um critério de objetivo, que deve ser implementado pelas subclasses.
    """

    def __init__(self, estado_inicial, operadores):
        """
        Inicializa um problema com um estado inicial e uma lista de operadores.

        @param estado_inicial: O estado inicial do problema.
        @param operadores: Uma lista de operadores (ações) aplicáveis aos estados.
        """
        self.__estado_inicial = estado_inicial
        assert(len(operadores) >= 1) #garante que a lista operadores tem pelo menos 1 valor
        self.__operadores = operadores

    @property
    def estado_inicial(self):
        """
        Retorna o estado inicial do problema.

        @return: Estado inicial.
        """
        return self.__estado_inicial

    @property
    def operadores(self):
        """
        Retorna a lista de operadores disponíveis no problema.

        @return: Lista de operadores.
        """
        return self.__operadores
    
    @abstractmethod
    def objectivo(self, estado):
        """
        Verifica se um determinado estado satisfaz a condição de objetivo do problema.

        Esse método deve ser implementado pelas subclasses para definir um critério de solução.

        @param estado: O estado a ser verificado.
        @return: True se o estado for um estado objetivo, False caso contrário.
        """
        pass