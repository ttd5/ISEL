from lib.mod.problema import Problema 

class ProblemaPlan(Problema):
    """Implementação de um problema específico para planeamento."""

    def __init__(self, modelo_plan, estado_final):
        """
        Inicializa o problema com o modelo de planeamento e o estado final.

        Args:
            modelo_plan (ModeloPlan): O modelo de planeamento.
            estado_final (Estado): O estado final desejado.
        """
        self.__modelo_plan = modelo_plan  # Armazena o modelo de planeamento
        self.__estado_final = estado_final  # Armazena o estado final
        super().__init__(self.__modelo_plan.obter_estado(), self.__modelo_plan.obter_operadores())

    def objectivo(self, estado):
        """
        Verifica se o estado atual corresponde ao estado final desejado.

        Args:
            estado (Estado): O estado atual a ser verificado.

        Returns:
            bool: True se o estado atual for igual ao estado final, False caso contrário.
        """
        return estado.posicao == self.__estado_final.posicao 