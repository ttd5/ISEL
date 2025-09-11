from lib.pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim):
    """Classe que representa a Procura Informada, uma subclasse de ProcuraMelhorPrim.

    Esta classe é usada para realizar procuras informadas, também conhecidas como procuras heurísticas.
    """

    def procurar(self, problema, heuristica):
        """Método para iniciar a busca informada.

        Este método define a heurística a ser utilizada e chama o método de procura da classe pai.
        """
        #self._heuristica = heuristica  # Define a heurística a ser utilizada
        self._avaliador.heuristica = heuristica  # Define a heurística no avaliador
        return super().procurar(problema)  # Chama o método de busca da classe pa