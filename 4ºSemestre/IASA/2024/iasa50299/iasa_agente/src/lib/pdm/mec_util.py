class MecUtil:

    def __init__(self, modelo, gama, delta_max):
        # Inicialização do MecUtil com o modelo, fator de desconto (gama) e valor máximo de delta permitido
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max
    
    def utilidade(self):
        """Calcula a utilidade para cada estado do modelo."""
        # Conjunto de estados (S) e conjunto de ações possíveis (A)
        S, A = self.__modelo.S, self.__modelo.A
        # Dicionário para armazenar a utilidade de cada estado (inicializado com 0)
        U = {s: 0.0 for s in S()}
        # Algoritmo de iteração de valor
        while True:
            # Cópia das utilidades anteriores para verificar a convergência
            Uant = U.copy()
            # Valor de delta para verificar a convergência
            delta = 0
            # Loop sobre todos os estados
            for s in S():
                # Cálculo da utilidade para cada ação possível no estado s
                U[s] = max([self.util_accao(s, a, Uant) for a in A(s)], default=0)
                # Atualização do valor de delta
                delta = max(delta, abs(U[s] - Uant[s]))
            # Verifica se a convergência foi alcançada
            if delta < self.__delta_max:
                break
        return U
    
    def util_accao(self, s, a, U):
        """Calcula o valor esperado de uma ação em um estado dado."""
        # Funções de transição (T), recompensa (R) e estados sucessores (suc)
        T, R, suc = self.__modelo.T, self.__modelo.R, self.__modelo.suc
        # Cálculo da utilidade esperada para a ação a no estado s
        return sum(T(s, a, sn) * (R(s, a, sn) + self.__gama * U[sn]) for sn in suc(s, a))