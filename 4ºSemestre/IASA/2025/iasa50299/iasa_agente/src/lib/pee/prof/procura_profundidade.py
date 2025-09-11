from lib.pee.mec_proc.mecanismo_procura import MecanismoProcura
from lib.pee.prof.fronteira_lifo import FronteiraLIFO


class ProcuraProfundidade(MecanismoProcura):
    """
    Implementa um mecanismo de busca em profundidade utilizando uma fronteira LIFO.
    """

    def __init__(self):
        super().__init__(FronteiraLIFO())  # Inicializa com a fronteira LIFO
        self.__nos_mem_mex = 0  # Inicializa o contador de nós máximos na memória

    def _actualizar_contagem_nos(self):
        """
        Atualiza o contador de nós na memória, registrando o número máximo de nós na fronteira.
        """
        num_nos_mem = self._fronteira.dimensao  # Obtém o número de nós atuais na fronteira
        if num_nos_mem > self.__nos_mem_mex:
            self.__nos_mem_mex = num_nos_mem  # Atualiza o máximo se necessário

    def _memorizar(self, no):
        """
        Memorização do nó no processo de busca e atualização do contador de nós na memória.
        """
        super()._memorizar(no)  # Memorização padrão
        self._actualizar_contagem_nos()  # Atualiza a contagem de nós

    @property
    def nos_memoria(self):
        """
        Retorna o número máximo de nós memorizados durante a execução da busca.
        """
        return self.__nos_mem_mex