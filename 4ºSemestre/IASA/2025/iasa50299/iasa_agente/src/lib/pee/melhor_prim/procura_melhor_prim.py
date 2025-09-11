from lib.pee.larg.procura_grafo import ProcuraGrafo
from lib.pee.melhor_prim.fronteira_prioridade import FronteiraPrioridade


class ProcuraMelhorPrim(ProcuraGrafo):
    """Classe que representa a Procura de Melhor Primeiro, uma subclasse de ProcuraGrafo.

    Esta classe é utilizada para realizar procuras de melhor primeiro.
    """

    def __init__(self, avaliador):
        """Inicializa a Procura de Melhor Primeiro com uma fronteira de prioridade.

        Args:
            avaliador: O avaliador a ser usado para calcular a prioridade dos nós.
        """
        super().__init__(FronteiraPrioridade(avaliador))  # Inicializa a classe pai com uma fronteira de prioridade
        self._avaliador = avaliador  # Armazena o avaliador para uso posterior

    def _manter(self, no):
        """Método para decidir se um nó deve ser mantido na busca.

        Este método verifica se o nó deve ser mantido na busca com base na sua prioridade e nos nós explorados anteriormente.
        """
        return super()._manter(no) or no.custo < self._explorados.get(no.estado).custo  # Decide se o nó deve ser mantido na busca
    
    @property
    def nos_memoria(self):
        # Devolve o número de nós que estão atualmente na fronteira
        return self._fronteira.dimensao