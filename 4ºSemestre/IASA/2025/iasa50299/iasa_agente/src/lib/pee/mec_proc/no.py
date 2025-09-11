"""
Nó
@author: Tatiana Damaya

Descrição:
Classe que representa um nó na árvore de procura, onde cada nó mantém informações sobre:
- O estado que ele representa.
- O operador que gerou o estado (se houver).
- O nó antecessor, que leva ao nó atual na árvore de procura (se houver).
- A profundidade do nó na árvore.
- O custo do caminho até o nó a partir da raiz.

Essa classe também define como os nós podem ser comparados entre si, com base no custo total do caminho até o nó.
"""

class No:
    """
    Classe que representa um nó na árvore de procura.
    Cada nó mantém o estado atual, o operador que gerou o estado, o antecessor,
    a profundidade na árvore e o custo do caminho até o nó.
    """

    nos_criados = 0
    nos_eliminados = 0
    nos_max_memoria = 0
    
    def __init__(self, estado, operador=None, antecessor=None, custo=0.0):
        """
        Inicializa um nó com o estado, operador, antecessor e custo especificados.

        @param estado: O estado que o nó representa.
        @param operador: O operador que gerou o estado (pode ser None).
        @param antecessor: O nó antecessor, ou seja, o nó que levou ao nó atual (pode ser None).
        @param custo: O custo acumulado até o nó (por padrão, 0.0).
        
        Se o nó possui um antecessor, o custo será calculado com base no custo do antecessor
        mais o custo da transição gerada pelo operador.
        Caso contrário, o nó é a raiz da árvore e o custo e profundidade são definidos como 0.
        """
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo
        self.__prioridade = None

        if (operador is None and antecessor is None):
            self.__profundidade = 0
            No.nos_criados = 0
            No.nos_eliminados = 0
        else:
           self.__profundidade = antecessor.profundidade + 1
          
        No.nos_criados += 1 #incrementa o número de nós criados
        nos_max = No.nos_criados - No.nos_eliminados
        if nos_max < No.nos_max_memoria:
            No.nos_max_memoria = nos_max

        
    @property
    def estado(self):
        """
        Retorna o estado associado ao nó.
        
        @return: O estado do nó.
        """
        return self.__estado
    
    @property
    def operador(self):
        """
        Retorna o operador que gerou o estado associado ao nó.
        
        @return: O operador que gerou o estado do nó.
        """
        return self.__operador
        
    @property
    def custo(self):
        """
        Retorna o custo do percurso até o nó.
        
        O custo é calculado como a soma dos custos do antecessor e a transição
        do operador aplicado.
        
        @return: O custo do nó.
        """
        return self.__custo
    
    @property
    def profundidade(self):
        """
        Retorna a profundidade do nó na árvore de busca.
        
        A profundidade é a distância do nó até a raiz da árvore.
        
        @return: A profundidade do nó.
        """
        return self.__profundidade
    
    @property
    def antecessor(self):
        """
        Retorna o nó antecessor, ou seja, o nó que levou ao nó atual.
        
        @return: O nó antecessor.
        """
        return self.__antecessor
    
    @property
    def prioridade(self):
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, valor):
        self.__prioridade = valor
        
    def __lt__(self, no):
        return self.prioridade < no.prioridade
    
    def __del__(self):
        No.nos_eliminados += 1