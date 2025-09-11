from abc import ABC, abstractmethod, abstractproperty
from lib.pee.mec_proc.no import No 
from lib.pee.mec_proc.solucao import Solucao 

class MecanismoProcura(ABC):
    """
    Mecanismo genérico de procura para explorar um espaço de estados até encontrar uma solução.
    """
    def __init__(self, fronteira):  
        self._fronteira = fronteira

    def _iniciar_memoria(self):
        """Inicializa a memória do mecanismo de procura."""
        return self._fronteira.iniciar()
    
    @abstractmethod
    def _memorizar(self, no):
        """Método abstrato para memorizar um nó explorado."""
        pass

    def procurar(self, problema):
        """Executa a procura no espaço de estados para encontrar uma solução."""
        self._iniciar_memoria()
        initial_node = No(problema.estado_inicial)
        self._fronteira.inserir(initial_node)
        while not self._fronteira.vazia:
            current_node = self._fronteira.remover()
            if problema.objectivo(current_node.estado):
                return Solucao(current_node)
            else:
                for no_suc in self._expandir(problema, current_node):
                    self._memorizar(no_suc)

    def _expandir(self, problema, no):
        """Expande um nó gerando seus nós sucessores."""
        for operador in problema.operadores:
            estado_suc = operador.aplicar(no.estado)
            if estado_suc:
                yield No(estado_suc, operador, no)