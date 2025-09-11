from ..plano import Plano

class PlanoPDM(Plano):
    """
    Representa o plano de ação gerado pelo Processo de Decisão Markoviano (PDM).
    Este plano contém a utilidade associada aos estados e a política a ser seguida pelo agente.
    """
    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade  # Armazena a utilidade de cada estado
        self.__politica = politica  # Armazena a política, que mapeia estados para ações

    def obter_accao(self, estado):
        """
        Obtém a ação a ser tomada a partir de um estado específico, conforme a política definida.

        A ação é determinada pela política, que indica a melhor ação para um dado estado.
        """
        if self.__politica:
            return self.__politica.get(estado)  # Retorna a ação associada ao estado

    def mostrar(self, vista):
        """
        Exibe a utilidade e a política na interface gráfica.

        A utilidade de cada estado é mostrada no ambiente, assim como a ação a ser tomada
        em cada estado, de acordo com a política calculada.
        """
        if self.__politica:
            # Exibe a utilidade de cada estado
            for estado, valor in self.__utilidade.items():
                vista.mostrar_valor_posicao(estado.posicao, valor)  # Mostra o valor da utilidade no ambiente
            # Exibe a política, ou seja, a ação a ser tomada em cada estado
            for estado, accao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, accao.ang)  # Mostra a direção da ação no ambiente
