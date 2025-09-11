from lib.pee.melhor_prim.aval.avaliador import Avaliador

class AvaliadorHeur(Avaliador):
    """Classe que herda de Avaliador e permite definir uma heurística."""

    @property
    def heuristica(self):
        return self._heuristica

    def __init__(self):
        self._heuristica = None

    @heuristica.setter
    def heuristica(self, heuristica):
        self._heuristica = heuristica