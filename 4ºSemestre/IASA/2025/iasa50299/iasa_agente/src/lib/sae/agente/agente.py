"""
Agente de simulação
@author: Luís Morgado
"""

from abc import ABC, abstractmethod

from .transdutor import Transdutor

#_______________________________________________________________________________

class Agente(ABC):
    """
    Agente base para simulação
    """
    def __init__(self):
        self.__transdutor = Transdutor()
        """Transdutor sensorial"""
        self.__vista = None
        """Vista do modelo interno"""

    @property
    def transdutor(self):
        return self.__transdutor

    @property
    def vista(self):
        return self.__vista
    
    @vista.setter
    def vista(self, nova_vista):
        self.__vista = nova_vista

    def _actuar(self, accao):
        self.__transdutor.actuar(accao)

    def _percepcionar(self):
        return self.__transdutor.percepcionar()
    
    @abstractmethod
    def executar(self):
        """
        Executar passo de processamento
        """