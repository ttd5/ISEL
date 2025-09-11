"""
Fronteira
@author: Tatiana Damaya
"""

from abc import ABC, abstractmethod

class Fronteira(ABC):
    """
    Classe abstrata que representa uma fronteira de exploração para armazenar e 
    gerenciar nós explorados em algoritmos de busca.

    A forma como os nós são inseridos depende do tipo específico de busca.
    """

    def __init__(self):
        """
        Inicializa a fronteira chamando o método iniciar().
        """
        self.iniciar()

    def iniciar(self):
        """
        Reinicializa a fronteira, removendo todos os nós armazenados.
        """
        self._nos = []
    
    @property
    def vazia(self):
        """
        Verifica se a fronteira está vazia.

        @return: True se não houver nós na fronteira, False caso contrário.
        """
        return len(self._nos) == 0
    
    @property
    def dimensao(self):
        """
        Retorna o número de nós atualmente armazenados na fronteira.

        @return: Quantidade de nós na fronteira.
        """
        return len(self._nos)
    
    @abstractmethod
    def inserir(self, no):
        """
        Insere um nó na fronteira de forma ordenada.

        O critério de ordenação depende do tipo de busca (por exemplo, BFS, DFS, A*).
        Esse método deve ser implementado pelas subclasses.

        @param no: O nó a ser inserido na fronteira.
        """
        pass

    def remover(self):
        """
        Remove e retorna o primeiro nó da fronteira de exploração.

        @return: O nó que foi removido da fronteira.
        """
        if not self.vazia:
            return self._nos.pop(0)
        else:
            return None