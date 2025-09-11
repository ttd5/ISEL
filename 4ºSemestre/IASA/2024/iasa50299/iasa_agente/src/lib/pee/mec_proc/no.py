from typing import Any
from functools import total_ordering

"""
• Nó
– Elemento constituinte da árvore de procura, mantendo informação de:
• Estado, a que corresponde o nó
• Operador, que gerou o estado a que corresponde o nó (pode não existir)
• Antecessor, nó antecessor na árvore de procura (pode não existir)
• Profundidade do nó, na árvore de procura
• Custo do percurso até ao nó
– Comparável com outros nós em termos de custo
"""

@total_ordering
class No:
    """
    • Estado
    • Operador (que gerou o estado)
    • Antecessor
    • Profundidade (do nó)
    • Custo (da raiz até ao nó)
    """
    def __init__(self, estado, operador=None, antecessor=None):
        """Inicializa um nó com o estado, operador e antecessor especificados."""
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        
        if antecessor:
            self.__profundidade = antecessor.profundidade + 1
            self.__custo = antecessor.custo + operador.custo(antecessor.estado, estado) 
        else:
            self.__profundidade = 0
            self.__custo = 0
        
    @property
    def estado(self):
        """Retorna o estado associado ao nó."""
        return self.__estado
    
    @property
    def operador(self):
        """Retorna o operador que gerou o estado associado ao nó."""
        return self.__operador
        
    @property
    def custo(self):
        """Retorna o custo do percurso até o nó."""
        return self.__custo
    
    @property
    def profundidade(self):
        """Retorna a profundidade do nó na árvore de procura."""
        return self.__profundidade
    
    @property
    def antecessor(self):
        """Retorna o nó antecessor na árvore de procura."""
        return self.__antecessor
    
    def __lt__(self, no):
        """Define a ordem de comparação entre nós com base em seus custos."""
        return self.__custo < no.custo