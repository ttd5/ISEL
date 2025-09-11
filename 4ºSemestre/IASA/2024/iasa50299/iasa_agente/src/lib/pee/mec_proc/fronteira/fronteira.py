from abc import ABC, abstractmethod

class Fronteira(ABC):
    """
    Fronteira de exploração para memorizar e gerir nós explorados
    """
    def __init__(self):
        self.iniciar()
    
    @property
    def vazia(self):
        """Indica se a fronteira está vazia"""
        return len(self._nos)==0
    
    def iniciar(self):
        """Iniciar fronteira elimina todos os nós da fronteira"""
        self._nos = []
    
    @abstractmethod
    def inserir(self,no):
        """Insere nó na fronteira de exploração de forma ordenada, concretização depende do tipo de procura"""
        pass

    def remover(self):
        """Remove nó inicial da fronteira de exploração"""
        return self._nos.pop(0)