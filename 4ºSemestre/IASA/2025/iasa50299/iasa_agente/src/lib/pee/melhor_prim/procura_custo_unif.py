from lib.pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from lib.pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif

class ProcuraCustoUnif(ProcuraMelhorPrim):
    """Classe que representa o algoritmo de Procura de Custo Uniforme.

    Este algoritmo expande sempre o nó com o menor custo acumulado até o momento, garantindo que sempre seja encontrado o caminho mais barato para o objetivo.
    """

    def __init__(self):
        """Inicializa a Procura de Custo Uniforme com um avaliador específico (AvaliadorCustoUnif)."""
        super().__init__(AvaliadorCustoUnif())