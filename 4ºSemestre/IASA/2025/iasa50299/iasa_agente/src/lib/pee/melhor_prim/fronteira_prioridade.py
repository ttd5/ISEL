from pee.mec_proc.fronteira import Fronteira
from heapq import heappush, heappop

class FronteiraPrioridade(Fronteira):
    """
    Classe que implementa uma fronteira com prioridade para algoritmos de procura.
    Herda da classe Fronteira e recorre a uma 'heap' (fila de prioridade) para ordenar os nós de acordo com a sua prioridade.
    """

    def __init__(self, avaliador):
        """
        Inicializa uma nova instância de FronteiraPrioridade.

        Parâmetros:
        avaliador: O avaliador utilizado para calcular a prioridade dos nós.

        Descrição:
        Este construtor invoca o construtor da classe-mãe Fronteira e inicializa o atributo __avaliador com o objecto fornecido.
        """

        super().__init__()
        self.__avaliador = avaliador

    def inserir(self, no):
        """
        Insere um nó na fronteira de exploração com base na prioridade atribuída pelo avaliador.

        Parâmetros:
        no: O nó a inserir na fronteira.

        Descrição:
        Este método calcula a prioridade do nó através do avaliador e insere o nó na 'heap',
        assegurando a ordenação por prioridade. A 'heap' garante que o nó com menor prioridade seja extraído primeiro.
        """
        no.prioridade = self.__avaliador.prioridade(no)
        heappush(self._nos, (self._nos, no))

    def remover(self):

        """
        Remove e retorna o nó com menor prioridade presente na fronteira de exploração.

        Retorna:
        O nó com menor prioridade.

        Descrição:
        Este método retira da 'heap' o nó com menor prioridade e devolve-o,
        garantindo que a ordem de exploração respeite as prioridades definidas.
        """

        (_, no) = heappop(self._nos)
        return no
    
    