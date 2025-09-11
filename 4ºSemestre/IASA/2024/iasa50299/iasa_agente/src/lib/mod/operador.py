from abc import ABC, abstractmethod

class Operador(ABC):
    """Define a estrutura básica de um operador no sistema."""

    @abstractmethod
    def aplicar(self, estado):
        """Aplica o operador a um estado para gerar um novo estado.

        Args:
            estado: O estado ao qual o operador será aplicado.

        Returns:
            O novo estado resultante após a aplicação do operador.
        """
        pass
    
    @abstractmethod
    def custo(self, estado, estado_suc):
        """Define o custo de transição de um estado para outro estado.

        Args:
            estado: O estado inicial.
            estado_suc: O estado sucessor após a aplicação do operador.

        Returns:
            O custo de transição do estado inicial para o estado sucessor.
        """
        pass