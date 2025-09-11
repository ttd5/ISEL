from lib.pee.melhor_prim.aval.avaliador import Avaliador

class AvaliadorHeur(Avaliador):
    """Classe que herda de Avaliador e permite definir uma heurística."""

    def definir_heuristica(self, heuristica):
        """
        Método para definir a heurística a ser usada.
        
        Args:
            heuristica: A heurística a ser definida para estimar o custo do caminho até o objetivo.
        """
        self._heuristica = heuristica