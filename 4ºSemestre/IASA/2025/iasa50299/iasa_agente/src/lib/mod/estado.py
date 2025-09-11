"""
Estado
@author: Tatiana Damaya
"""

from abc import ABC, abstractmethod

class Estado(ABC):

    @abstractmethod
    def id_valor(self):
        """
        Método abstrato que deve ser implementado pelas subclasses.
        Deve retornar um valor único que identifica o estado.

        @return: Identificação única do estado.
        """
        pass

    def __hash__(self):
        """
        Retorna um valor de hash único para a instância, baseado no método id_valor.
        Isso permite que instâncias de Estado sejam usadas em coleções como conjuntos (set) e dicionários (dict).
        
        @return: Valor de hash único da instância.
        """
        return self.id_valor()
    
    def __eq__(self, other):
        """
        Compara dois estados para verificar se são iguais, com base em seus identificadores únicos.

        @param other: Outro objeto para comparar.
        @return: True se forem estados iguais, False caso contrário.
        """
        if isinstance(other, Estado):
            return self.__hash__() == other.__hash__()
        return False