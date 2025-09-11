from mod.problema import Problema

class ProblemaPlan(Problema):
    """
    Representa um problema de planejamento no contexto do método de Procura em Espaços de Estados (PEE).
    Esta classe define o estado inicial, os operadores e o estado objetivo para a resolução do problema.
    """

    def __init__(self, modelo_plan, estado_final):
        """
        Inicializa uma instância de ProblemaPlan, definindo o modelo de planejamento e o estado final desejado.

        O modelo de planejamento fornece o estado inicial e os operadores aplicáveis, enquanto o estado final é guardado
        para ser utilizado na verificação do objetivo a ser alcançado.
        """
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())  # Chama o construtor da superclasse
        self.__estado_final = estado_final  # Armazena o estado final

    def objectivo(self, estado):
        """
        Verifica se o estado atual é o estado final, ou seja, se o objetivo foi alcançado.

        Compara o estado atual com o estado final. Se forem iguais, o objetivo foi atingido.
        """
        return estado == self.__estado_final  # Verifica se o estado corresponde ao estado final
