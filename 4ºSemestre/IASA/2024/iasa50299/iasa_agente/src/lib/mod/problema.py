from abc import ABC, abstractmethod

class Problema(ABC):
    """
    Classe abstrata que define a estrutura básica de um problema no sistema.

    Attributes:
        estado_inicial: O estado inicial do problema.
        operadores: Uma lista de operadores disponíveis para o problema.
    """

    def __init__(self, estado_inicial, operadores):
        """Inicializa o problema com um estado inicial e uma lista de operadores."""
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores

    @property
    def estado_inicial(self):
        """Getter para o estado inicial do problema."""
        return self.__estado_inicial
    
    @property
    def operadores(self):
        """Getter para a lista de operadores do problema."""
        return self.__operadores

    @abstractmethod
    def objectivo(self, estado):
        """Função abstrata para verificar se um estado atinge o objetivo do problema."""
        pass