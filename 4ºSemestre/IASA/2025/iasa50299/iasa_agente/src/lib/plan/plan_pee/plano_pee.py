from plan.plano import Plano

class PlanoPEE(Plano):
    """
    Representa um plano de ação gerado pelo planeador PEE (Procura em Espaços de Estados).
    Este plano armazena a sequência de passos (ações) necessárias para alcançar o objetivo.
    """

    def __init__(self, solucao):
        """
        Inicializa um novo plano de ação a partir de uma solução encontrada.

        A solução fornecida é uma lista de passos (ações) que formam o caminho até o objetivo.
        O construtor armazena esses passos para uso posterior no planejamento.
        """
        self.__passos = [passo for passo in solucao]  # Armazena a sequência de passos no plano

    def obter_accao(self, estado):
        """
        Obtém a ação associada a um estado específico.

        O método verifica se o estado fornecido está presente na lista de passos do plano.
        Se encontrado, retorna a ação associada a esse estado.
        Caso contrário, retorna None.
        """
        if self.__passos:
            passo = self.__passos.pop(0)  # Remove o primeiro passo da lista
            if passo.estado == estado:  # Verifica se o estado corresponde ao passo atual
                return passo.operador  # Retorna a ação associada ao estado

    @property
    def dimensao(self):
        """Retorna a quantidade de passos no plano."""
        return len(self.__passos)  # O número de passos é a dimensão do plano

    def mostrar(self, vista):
        """
        Exibe graficamente a sequência de passos do plano.

        O método utiliza a vista para mostrar cada estado e a ação associada, ajudando a visualizar
        o progresso do plano na resolução do problema.
        """
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)  # Exibe a direção da ação no ambiente