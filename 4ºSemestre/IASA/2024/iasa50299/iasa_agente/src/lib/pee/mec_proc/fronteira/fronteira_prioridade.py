from heapq import heappush, heappop
from lib.pee.mec_proc.fronteira.fronteira import Fronteira

class FronteiraPrioridade(Fronteira):
    """Fronteira de prioridade para procura de custo uniforme.

    Esta fronteira mantém os nós numa fila de prioridade com base em uma função de avaliação.
    Os nós com menor avaliação (ou prioridade) são retirados primeiro.
    """
    def __init__(self, avaliador):
        """Inicializa a fronteira de prioridade com o avaliador específico."""
        super().__init__()
        self.__avaliador = avaliador
        
    def inserir(self, no):
        """Insere um nó na fronteira com base na avaliação fornecida pelo avaliador."""
        prioridade = self.__avaliador.prioridade(no)
        heappush(self._nos, (prioridade, no))  # Insere o nó com sua prioridade na fila de prioridade

    def remover(self):
        """Remove e retorna o nó com a menor prioridade."""
        _, no = heappop(self._nos)  # Remove e retorna o nó com a menor prioridade da fila de prioridade
        return no