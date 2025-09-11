from abc import ABC, abstractmethod

class Heuristica(ABC):
    """Classe abstrata que define uma heurística para algoritmos de procura informada."""

    @abstractmethod
    def h(self, estado):
        """Método abstrato para calcular o valor heurístico de um estado.

        Args:
            estado: O estado para o qual a heurística deve ser calculada.

        Returns:
            O valor heurístico do estado.
        """
        pass