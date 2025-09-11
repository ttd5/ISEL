from lib.pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

class AvaliadorAA(AvaliadorHeur):
    """Classe que herda de AvaliadorHeur e implementa o método de prioridade para o algoritmo A*."""
    def prioridade(self, no):
        """
        Calcula a prioridade de um nó para o algoritmo A*.

        A prioridade é a soma do custo acumulado até o nó com a estimativa do custo
        do nó até o objetivo (heurística).
        
        Args:
            no: O nó cuja prioridade está sendo calculada.
        
        Returns:
            A prioridade do nó para o algoritmo A*.
        """
        return no.custo + self._heuristica.h(no.estado)