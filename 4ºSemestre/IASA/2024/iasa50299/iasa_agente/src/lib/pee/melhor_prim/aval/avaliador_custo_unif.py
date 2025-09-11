from lib.pee.melhor_prim.aval.avaliador import Avaliador

class AvaliadorCustoUnif(Avaliador):
    """Classe que herda de Avaliador e implementa o método de prioridade para a Procura de Custo Uniforme."""
    def prioridade(self, no):
        """
        Calcula a prioridade de um nó para a Procura de Custo Uniforme.
        
        Como f(n) = g(n), a prioridade é simplesmente o custo acumulado até o nó.
        
        Args:
            no: O nó cuja prioridade está sendo calculada.
        
        Returns:
            O custo acumulado até o nó, que é a prioridade para a Procura de Custo Uniforme.
        """
        return no.custo