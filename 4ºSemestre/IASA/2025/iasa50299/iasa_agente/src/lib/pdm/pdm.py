from pdm.mec_util import MecUtil

class PDM:
    """
    Implementação de um Processo de Decisão Markoviano (PDM).
    O objetivo é calcular as utilidades dos estados e encontrar a política ótima utilizando um mecanismo de utilidade.
    """

    def __init__(self, modelo, gama, delta_max):
        """
        Configura o Processo de Decisão Markoviano.

        Inicializa o modelo do mundo, o mecanismo de utilidade e define os parâmetros de cálculo da utilidade.
        O fator de desconto e o limite de variação são usados para controlar o processo de cálculo de convergência.
        """
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)
    
    def politica(self, U):
        """
        Determina a política ótima com base na utilidade calculada para cada estado.

        Para cada estado, identifica a ação que oferece a maior utilidade, com base nos valores fornecidos.
        Essa ação é considerada a melhor escolha para o agente naquele estado.
        """
        A = self.__modelo.A
        S = self.__modelo.S
        politica = {}

        for s in S():
            if A(s):
                melhor_acao = max(A(s), key=lambda a: self.__mec_util.util_accao(s, a, U))
                politica[s] = melhor_acao

        return politica
    
    def resolver(self):
        """
        Resolve o processo de decisão Markoviano.

        Calcula as utilidades para os estados e determina a política ótima correspondente com base nas utilidades calculadas.
        Retorna tanto as utilidades quanto a política final.
        """
        U = self.__mec_util.utilidade()
        politica = self.politica(U)
        return U, politica
