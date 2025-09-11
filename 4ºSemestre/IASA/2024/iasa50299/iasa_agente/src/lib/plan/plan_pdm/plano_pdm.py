from lib.plan.plano import Plano

class PlanoPDM(Plano):
    """Representa um plano de ação gerado pelo processo de decisão de Markov (PDM).

    PlanoPDM armazena a utilidade associada a cada estado e a política de ação que define a ação ótima a ser tomada em cada estado.

    Attributes:
        utilidade (dict): Um dicionário que mapeia cada estado à sua utilidade.
        politica (dict): Um dicionário que mapeia cada estado à sua política de ação.
    """

    def __init__(self, utilidade, politica):
        """Inicializa o PlanoPDM com a utilidade e a política de ação."""
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado):
        """Obtém a ação associada a um estado na política de ação."""
        if estado and estado in self.__politica:
            return self.__politica[estado]
        
    def mostrar(self, vista):
        """Mostra o plano de ação numa visualização."""
        if self.__politica:
            # Mostra a utilidade associada a cada estado
            for estado, valor in self.__utilidade.items():
                vista.mostrar_valor_posicao(estado.posicao, valor)
            
            # Mostra o vetor de ação associado a cada estado na política de ação
            for estado, accao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, accao.ang)