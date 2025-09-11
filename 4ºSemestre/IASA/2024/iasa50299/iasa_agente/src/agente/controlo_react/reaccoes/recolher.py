from lib.ecr.hierarquia import Hierarquia

class Recolher(Hierarquia):
    """
    Comportamento para Recolher Alvos

    Esta classe representa um comportamento composto que agrega um conjunto de sub-comportamentos.
    Estes sub-comportamentos correspondem a sub-objetivos necessários para alcançar o objetivo principal de recolher alvos. 
    Os sub-comportamentos incluem AproximarAlvo, EvitarObst e Explorar.

    Attributes:
        comportamentos (list): Uma lista de sub-comportamentos que contribuem para o objetivo de recolher alvos.
    """
    def __init__(self, comportamentos):
        """
        Inicializa o comportamento para recolher alvos.

        Args:
            comportamentos (list): Uma lista de sub-comportamentos.
        """
        # Chama o construtor da classe base para inicializar a hierarquia com os sub-comportamentos fornecidos
        super().__init__(comportamentos)
