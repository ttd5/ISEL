from lib.pdm.modelo.modelo_pdm import ModeloPDM
from lib.plan.modelo.modelo_plan import ModeloPlan

class ModeloPDMPlan(ModeloPDM, ModeloPlan):
    """Combinação de um ModeloPDM e um ModeloPlan.

    Este modelo combina um ModeloPDM e um ModeloPlan para representar um ambiente onde o processo
    de decisão de Markov (PDM) é utilizado para planejamento. Ele herda de ambos ModeloPDM e ModeloPlan.

    """

    def __init__(self, modelo_plan, objectivos, rmax=1000.0):
        """Inicializa o ModeloPDMPlan.

        Args:
            modelo_plan: O modelo de planejamento.
            objectivos: Uma lista de estados que representam os objetivos.
            rmax: O valor máximo de recompensa (por padrão, 1000.0).
        """
        self.__modelo_plan = modelo_plan
        self.__objectivos = objectivos
        self.__rmax = rmax
        self.__transicoes = {}

        # Construir o dicionário de transições
        if self.obter_estados() and self.obter_operadores(): 
            for s in self.obter_estados():
                for a in self.obter_operadores():
                    sn = a.aplicar(s)
                    if sn is not None:
                        self.__transicoes[(s, a)] = sn

    # Métodos da interface ModeloPlan
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()
        
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
        
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()
    
    # Métodos da interface ModeloPDM
    def S(self):
        return self.obter_estados()
        
    def A(self, s):
        return self.obter_operadores()
        
    def T(self, s, a, sn):
        if sn and (sn == self.__transicoes[(s, a)]):
            return 1
        return 0
        
    def R(self, s, a, sn):
        r = 0
        if sn:
            r = -(a.custo(s, sn))
            if self.__objectivos and sn in self.__objectivos:
                r += self.__rmax
        return r
    
    def suc(self, s, a):
        sn = []
        if self.__transicoes.get((s, a)):
            sn.append(self.__transicoes.get((s, a)))
        return sn