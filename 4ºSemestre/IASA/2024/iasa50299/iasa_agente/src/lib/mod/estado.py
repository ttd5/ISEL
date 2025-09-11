from abc import ABC, abstractmethod

class Estado(ABC):
    """Define a estrutura básica de um estado no sistema."""

    @abstractmethod
    def id_valor(self):
        """Método abstrato para obter o valor de identificação único do estado."""
        pass

    def __hash__(self):
        """Calcula o hash do estado com base no seu valor de identificação único."""
        return self.id_valor()

    def __eq__(self, other):
        """Verifica se dois estados são iguais com base no seu valor de identificação único."""
        return self.__hash__() == other.__hash__()