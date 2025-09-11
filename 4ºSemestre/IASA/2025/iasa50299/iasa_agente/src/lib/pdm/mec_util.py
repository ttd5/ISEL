class MecUtil:
    """
    Implementa o mecanismo de cálculo da utilidade para um Processo de Decisão Markoviano (PDM).
    O objetivo é calcular as utilidades dos estados com base nas transições e recompensas.
    """

    def __init__(self, modelo, gama, delta_max):
        """
        Inicializa o mecanismo de utilidade.

        O modelo PDM contém a definição dos estados, ações, transições e recompensas. O fator de desconto é usado 
        para ajustar a utilidade das ações, e o delta máximo define o limite para a convergência do cálculo.
        """
        self.__modelo = modelo  # Armazena o modelo PDM
        self.__gama = gama  # Define o fator de desconto
        self.__delta_max = delta_max  # Estabelece o limite máximo de variação para a convergência

    def utilidade(self):
        """
        Calcula a utilidade de todos os estados.

        A utilidade é determinada por meio de um processo iterativo, onde, em cada ciclo, as utilidades dos estados
        são atualizadas até que a diferença entre as iterações sucessivas seja suficientemente pequena para considerar
        que o processo convergiu.
        """
        S = self.__modelo.S  # Obtém os estados disponíveis no modelo
        A = self.__modelo.A  # Obtém as ações disponíveis para cada estado
        U = {s: 0.0 for s in S()}  # Inicializa as utilidades dos estados com 0.0
        
        while True:
            Uant = U.copy()  # Faz uma cópia das utilidades da iteração anterior
            delta = 0  # Variável que armazenará a maior variação entre iterações

            for s in S():
                # Para cada estado, calcula a utilidade máxima com base nas ações possíveis
                U[s] = max([self.util_accao(s, a, Uant) for a in A(s)], default=0)
                delta = max(delta, abs(U[s] - Uant[s]))  # Calcula a variação entre a utilidade atual e a anterior

            if delta <= self.__delta_max:  # Se a variação for menor que o limite, o processo convergiu
                break

        return U  # Retorna as utilidades finais dos estados

    def util_accao(self, s, a, U):
        """
        Calcula a utilidade de realizar uma ação em um determinado estado.

        A utilidade da ação é calculada com base nas transições para os estados sucessores, considerando a recompensa
        e o fator de desconto. A utilidade é a soma ponderada das utilidades dos sucessores, ajustadas pelas probabilidades
        de transição e o valor das recompensas.
        """
        T = self.__modelo.T  # Função de transição que retorna a probabilidade de ir de um estado para outro
        R = self.__modelo.R  # Função de recompensa associada a uma transição de estado
        gama = self.__gama  # Fator de desconto
        suc = self.__modelo.suc  # Função que retorna os estados sucessores após uma ação

        # Calcula a utilidade da ação somando as utilidades dos estados sucessores
        return sum(T(s, a, sn) * (R(s, a, sn) + gama * U[sn]) for sn in suc(s, a))
