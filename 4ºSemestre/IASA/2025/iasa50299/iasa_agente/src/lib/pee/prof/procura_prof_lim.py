from lib.pee.prof.procura_profundidade import ProcuraProfundidade


class ProcuraProfLim(ProcuraProfundidade):
    """
    Implementa uma busca em profundidade com limite de profundidade especificado.
    """

    def __init__(self, prof_max=10):
        super().__init__()  # Inicializa a classe base
        self.__prof_max = prof_max  # Define o limite de profundidade máximo
    
    def procurar(self, problema, prof_max=10):
        """
        Executa a busca em profundidade limitada.

        Define o limite de profundidade para a busca, garantindo que a profundidade do nó não ultrapasse o limite especificado.
        """
        self._prof_max = prof_max
        return super().procurar(problema)
    
    def _expandir(self, problema, no):
        """
        Expande o nó, mas respeitando o limite de profundidade.

        Se a profundidade do nó ultrapassar o limite, a expansão é evitada.
        """
        return super()._expandir(problema, no) if no.profundidade < self._prof_max else []
