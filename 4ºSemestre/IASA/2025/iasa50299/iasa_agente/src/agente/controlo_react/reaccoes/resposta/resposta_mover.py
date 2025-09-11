from lib.sae.agente.accao import Accao
from lib.ecr.resposta import Resposta


class RespostaMover(Resposta):
    """
    Resposta para mover-se numa direção

    Esta classe representa uma resposta para mover-se numa direção específica no ambiente.

    Attributes:
        _accao (Accao): A ação a ser realizada, representada pela direção de movimento.
    """
    
    def __init__(self, direccao):
        """
        Inicializa a resposta para mover-se na direção especificada.

        Args:
            direccao (Direccao): A direção para mover-se.
        """
        # Chama o construtor da classe base com a ação criada
        super().__init__(Accao(direccao, 1))

