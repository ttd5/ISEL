from controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from controlo_react.reaccoes.explorar.explorar import Explorar
from controlo_react.reaccoes.explorar.explorar_mem import ExplorarMem
from lib.ecr.hierarquia import Hierarquia

class RecolherAlvos(Hierarquia):
    """
    Comportamento para Recolher Alvos

    Esta classe representa um comportamento composto que agrega um conjunto de sub-comportamentos.
    Estes sub-comportamentos correspondem a sub-objetivos necessários para alcançar o objetivo principal de recolher alvos. 
    Os sub-comportamentos incluem AproximarAlvo, EvitarObst e Explorar.

    Attributes:
        comportamentos (list): Uma lista de sub-comportamentos que contribuem para o objetivo de recolher alvos.
    """
    def __init__(self):
        """
        Inicializa o comportamento para recolher alvos.

        Args:
            comportamentos (list): Uma lista de sub-comportamentos.
        """
        # Chama o construtor da classe base para inicializar a hierarquia com os sub-comportamentos fornecidos
        super().__init__([ AproximarAlvo(), EvitarObst(), ExplorarMem(), Explorar(0.7)])
