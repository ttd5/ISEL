from mod.estado import Estado

class EstadoAgente(Estado):
    """
    Representa o estado do agente no ambiente.

    Este estado contém a posição atual do agente no mundo.

    Attributes:
        posicao (tuple): A posição atual do agente no mundo, representada como um tuplo.
        id_valor (int): O valor de identificação único para este estado, gerado a partir da posição.
    """

    def __init__(self, posicao):
        """
        Inicializa o estado do agente com a posição fornecida.

        Args:
            posicao (tuple): A posição inicial do agente no mundo.
        """
        self.__posicao = posicao
        self.__id_valor = hash(self.__posicao)

    @property
    def posicao(self):
        """
        Retorna a posição atual do agente.

        Returns:
            tuple: A posição atual do agente no mundo.
        """
        return self.__posicao
    
    def id_valor(self):
        """
        Retorna o valor de identificação único para este estado.

        Returns:
            int: O valor de identificação único deste estado.
        """
        return self.__id_valor
