"""
Operador
@author: Tatiana Damaya
"""

from abc import ABC, abstractmethod

class Operador(ABC):
    """
    Classe abstrata que define a interface para um operador em um problema de busca.

    Um operador representa uma ação que pode ser aplicada a um estado para gerar um novo estado.
    Cada operador deve definir um método para aplicação e outro para calcular o custo da transição.
    """

    @abstractmethod
    def aplicar(self, estado):
        """
        Aplica o operador a um estado e retorna o estado resultante.

        @param estado: O estado atual onde o operador será aplicado.
        @return: O novo estado resultante da aplicação do operador.
        """
        pass

    @abstractmethod
    def custo(self, estado, estado_suc):
        """
        Retorna o custo da transição de um estado para outro ao aplicar o operador.

        @param estado: O estado atual antes da aplicação do operador.
        @param estado_suc: O estado sucessor resultante da aplicação do operador.
        @return: Um valor numérico representando o custo da transição entre os estados.
        """
        pass
