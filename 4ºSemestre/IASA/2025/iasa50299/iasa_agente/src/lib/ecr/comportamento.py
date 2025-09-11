from abc import ABC, abstractmethod

class Comportamento(ABC):
    """
    Interface que define a funcionalidade geral de um comportamento.
    Um comportamento relaciona padrões de percepção com padrões de ação.
    """
    @abstractmethod
    def activar(self, percepcao):
        """
        Ativa o comportamento com base na percepção atual.
        
        :param percepcao: A percepção atual do ambiente.
        :return: A ação associada ao comportamento, se houver, ou None.
        """
        pass