from lib.pee.melhor_prim.aval.avaliador_aa import AvaliadorAA
from lib.pee.melhor_prim.procura_informada import ProcuraInformada

class ProcuraAA(ProcuraInformada):
    """
    Este algoritmo utiliza uma função de avaliação que combina o custo acumulado até o nó atual com uma heurística que estima o custo do nó atual ao objetivo.
    """

    def __init__(self):
        """Inicializa a procura AA com um avaliador específico (AvaliadorAA)."""
        super().__init__(AvaliadorAA())
