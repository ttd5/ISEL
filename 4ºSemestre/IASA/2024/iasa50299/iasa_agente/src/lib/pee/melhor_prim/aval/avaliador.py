from abc import ABC, abstractmethod

class Avaliador(ABC):
    """Classe abstrata que define um avaliador para determinar a prioridade dos nós em algoritmos de busca."""

    @abstractmethod
    def prioridade(self, no):
        """Método abstrato para calcular a prioridade de um nó.
        
        Args:
            no: O nó para o qual a prioridade deve ser calculada.
        
        Returns:
            A prioridade do nó.
        """
        pass