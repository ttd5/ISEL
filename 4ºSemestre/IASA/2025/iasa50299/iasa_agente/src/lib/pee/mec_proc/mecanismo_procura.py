from abc import ABC, abstractmethod
from lib.pee.mec_proc.no import No
from lib.pee.mec_proc.solucao import Solucao 

class MecanismoProcura(ABC):
    """
    Classe genérica para implementar mecanismos de procura no espaço de estados, 
    com o objetivo de encontrar uma solução para o problema.
    """
    def __init__(self, fronteira):  
        self._fronteira = fronteira  # Define a fronteira que será usada para armazenar os nós
        self.__nos_processados = 0  # Inicializa o contador de nós processados

    def _iniciar_memoria(self):
        """Reinicia a memória do mecanismo de procura, preparando a fronteira."""
        return self._fronteira.iniciar()
    
    @abstractmethod
    def _memorizar(self, no):
        """Memoriza um nó após ser explorado, inserindo-o na fronteira."""
        self._fronteira.inserir(no)

    def procurar(self, problema):
        """Executa a procura no espaço de estados até encontrar uma solução."""
        self._iniciar_memoria()  # Inicia a memória do mecanismo de procura
        no = No(problema.estado_inicial)  # Cria um nó a partir do estado inicial do problema
        self._memorizar(no)  # Memoriza o nó inicial
        while not self._fronteira.vazia:  # Enquanto houver nós para explorar na fronteira,
            no = self._fronteira.remover()  # Remove o primeiro nó da fronteira
            self.__nos_processados += 1  # Conta o nó como processado
            if problema.objetivo(no.estado):  # Verifica se o estado do nó é uma solução
                return Solucao(no)  # Retorna a solução encontrada, que termina no nó
            for no_sucessor in self._expandir(problema, no):  # Expande o nó e processa seus sucessores
                self._memorizar(no_sucessor)  # Memoriza os nós sucessores
        return None  # Retorna None caso não encontre uma solução

    def expandir(self, problema, no):
        """
        Expande o nó gerando seus sucessores, de acordo com os operadores disponíveis no problema.
        """
        sucessores = []  # Cria uma lista vazia para armazenar os sucessores
        estado = no.estado  # Obtém o estado atual do nó
        for operador in problema.operadores:  # Para cada operador do problema,
            estado_suc = operador.aplicar(estado)  # Aplica o operador para gerar um estado sucessor
            if estado_suc is not None:  # Se o estado sucessor for válido,
                custo = no.custo + operador.custo(estado, estado_suc)  # Calcula o custo do sucessor
                no_successor = No(estado_suc, operador, no, custo)  # Cria o nó sucessor
                sucessores.append(no_successor)  # Adiciona o nó sucessor à lista
        return sucessores  # Retorna a lista de sucessores gerados
        
    @property
    def fronteira(self):
        return self._fronteira  # Retorna a fronteira utilizada pelo mecanismo de procura
    
    @property
    def nos_processados(self):
        return self.__nos_processados  # Retorna o número de nós processados até o momento
    
    @property
    @abstractmethod
    def nos_memoria(self):
        """Define como a memória de nós será gerida pelas subclasses."""
        return No.nos_max_memoria
