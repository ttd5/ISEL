from lib.pee.melhor_prim.aval.avaliador_sof import AvaliadorSof
from lib.pee.melhor_prim.procura_informada import ProcuraInformada

class ProcuraSofrega(ProcuraInformada):
    """Classe que representa a Procura Sofrega, uma subclasse de ProcuraInformada."""

    def __init__(self):
        """Inicializa a Procura Sofrega com um avaliador sofrega."""
        super().__init__(AvaliadorSof())  # Inicializa a classe pai com um avaliador sofrega