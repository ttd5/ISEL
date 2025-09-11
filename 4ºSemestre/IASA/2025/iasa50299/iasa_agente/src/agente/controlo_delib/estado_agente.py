from lib.mod.estado import Estado

class EstadoAgente(Estado):
    """
    Define o estado de um agente dentro de um sistema de estados.
    Esta classe estende a classe Estado e usa a posição do agente como a principal representação do seu estado.
    """

    def __init__(self, posicao):
        """
        Cria uma instância de EstadoAgente com base na posição fornecida.

        A posição do agente é utilizada para representar seu estado no espaço de estados.
        """
        self.__posicao = posicao  # Armazena a posição do agente como o estado

    @property
    def posicao(self):
        """
        Retorna a posição atual do agente.

        Este método oferece acesso à posição do agente de maneira controlada, garantindo a integridade do estado.
        """
        return self.__posicao

    def id_valor(self):
        """
        Gera um identificador único para o estado do agente.

        A geração do identificador é feita com base no hash da posição do agente, garantindo que cada estado tenha um identificador único.
        """
        return hash(self.__posicao)  # Usa o hash da posição para identificar unicamente o estado
