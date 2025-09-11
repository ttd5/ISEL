from pdm.mec_util import MecUtil

class PDM:

    def __init__(self, modelo, gama, delta_max):
        # Inicialização do PDM com o modelo, fator de desconto (gama) e valor máximo de delta permitido
        self.__modelo = modelo
        self.gama = gama
        self.delta_max = delta_max
        # Inicialização do mecanismo de utilidade (MecUtil)
        self.__mec_util = MecUtil(self.__modelo, self.gama, self.delta_max)

    def politica(self, U):
        """Calcula a política de ação para cada estado possível."""
        # Conjunto de estados (S) e conjunto de ações possíveis (A)
        S, A = self.__modelo.S, self.__modelo.A
        pol = {}
        # Iteração sobre todos os estados
        for s in S():
            # Verifica se existem ações possíveis para o estado atual
            if A(s):
                # Escolhe a ação que maximiza a utilidade esperada usando o MecUtil
                pol[s] = max(A(s), key=lambda a: self.__mec_util.util_accao(s, a, U))
        return pol
        
    def resolver(self):
        """Resolve o problema de decisão de Markov parcialmente observável."""
        # Calcula a utilidade para cada estado usando o MecUtil
        U = self.__mec_util.utilidade()
        # Calcula a política de ação usando as utilidades calculadas
        pol = self.politica(U)
        return U, pol