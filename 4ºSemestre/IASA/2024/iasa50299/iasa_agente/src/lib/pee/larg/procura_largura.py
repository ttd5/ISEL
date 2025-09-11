from lib.pee.mec_proc.fronteira.fronteira_fifo import FronteiraFIFO
from lib.pee.mec_proc.procura_grafo import ProcuraGrafo

class ProcuraLargura(ProcuraGrafo):
    def __init__(self):
        # Chama o construtor da classe pai para inicializar a busca em grafo
        super().__init__(FronteiraFIFO())  # Inicializa a fronteira com uma estrutura de dados FIFO