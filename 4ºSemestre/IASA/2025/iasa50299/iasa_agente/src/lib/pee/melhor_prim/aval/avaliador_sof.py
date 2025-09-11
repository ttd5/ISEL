from lib.pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

class AvaliadorSof(AvaliadorHeur):
    """Classe que herda de AvaliadorHeur e implementa a heurística para o algoritmo de procura de A*."""

    def prioridade(self, no):
        """
        Calcula a prioridade de um nó para o algoritmo de procura A*.

        A prioridade é determinada pela heurística, que estima o custo do nó até o objetivo.
        """
        return self._heuristica.h(no.estado)