from lib.pee.prof.procura_profundidade import ProcuraProfundidade

class ProcuraProfLim(ProcuraProfundidade):
    """Procura em Profundidade Limitada.

    Esta classe herda da procura em profundidade e adiciona um limite máximo de profundidade.

    Attributes:
        prof_max (int): O limite máximo de profundidade permitido.
    """

    def __init__(self, prof_max=100):
        """Inicializa a procura em profundidade limitada com um limite máximo de profundidade.

        Args:
            prof_max (int, optional): O limite máximo de profundidade permitido. O padrão é 100.
        """
        self.__prof_max = prof_max
        super().__init__()

    @property
    def prof_max(self):
        """Getter para o limite máximo de profundidade."""
        return self.__prof_max
    
    @prof_max.setter
    def prof_max(self, num):
        """Setter para o limite máximo de profundidade."""
        self.__prof_max = num

    def _expandir(self, problema, no):
        """Expande os nós sucessores até o limite máximo de profundidade.

        Args:
            problema: O problema a ser resolvido.
            no: O nó atual a ser expandido.

        Yields:
            Iterator: Um iterador sobre os nós sucessores.
        """
        # Verifica se a profundidade atual do nó é menor que o limite máximo
        if no.profundidade < self.prof_max:
            # Se for, expande os nós sucessores normalmente
            yield from super()._expandir(problema, no)