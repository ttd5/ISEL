from pee.larg.fronteira_fifo import FronteiraFIFO
from pee.larg.procura_grafo import ProcuraGrafo

class ProcuraLargura(ProcuraGrafo):

    def __init__(self):
        super().__init__(FronteiraFIFO())