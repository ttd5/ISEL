from abc import ABC, abstractmethod

class Plano(ABC):
    """Interface para os planos."""

    @abstractmethod
    def obter_accao(self, estado):
        """
        Obtém a próxima ação a ser executada no estado especificado.

        Args:
            estado: O estado atual do ambiente.

        Returns:
            Ação: A próxima ação a ser executada no estado especificado.
        """
        pass
    
    @abstractmethod
    def mostrar(self, vista):
        """
        Mostra uma representação do plano numa determinada visualização.

        Args:
            vista: A visualização onde o plano será mostrado.
        """
        pass