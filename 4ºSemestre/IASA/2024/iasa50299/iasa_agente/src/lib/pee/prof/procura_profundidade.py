from lib.pee.mec_proc.fronteira.fronteira_lifo import FronteiraLIFO
from lib.pee.mec_proc.mecanismo_procura import MecanismoProcura

class ProcuraProfundidade(MecanismoProcura):
    """Procura em Profundidade.

    Esta classe implementa o algoritmo de procura em profundidade, onde os nós são explorados em profundidade,
    ou seja, até que não haja mais nós a serem explorados num determinado ramo da árvore de busca.

    Attributes:
        Nenhum.
    """

    def __init__(self):
        """Inicializa a busca em profundidade usando a fronteira LIFO."""
        super().__init__(FronteiraLIFO())

    def _memorizar(self, no):
        """Memoriza um nó na fronteira."""
        self._fronteira.inserir(no)