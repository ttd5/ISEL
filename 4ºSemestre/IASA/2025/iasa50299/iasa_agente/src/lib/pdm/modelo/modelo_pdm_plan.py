from modelo_pdm import ModeloPDM
from plan.modelo.modelo_plan import ModeloPlan

class ModeloPDMPlan(ModeloPDM, ModeloPlan):
    
    def __init__(self, modelo_plan, objectivos, rmax=1000):
        self.__modelo_plan = modelo_plan  # Armazena o modelo de planejamento
        self.__rmax = rmax  # Define o valor máximo de recompensa
        self.__objectivos = objectivos  # Define os objetivos do agente
        
        # Gera as transições de estado possíveis
        self.__transicoes = {}
        
        # Para cada estado e cada ação, calcula os estados sucessores
        for s in self.obter_estados():
            for a in self.obter_operadores():
                sn = a.aplicar(s)  # Aplica a ação ao estado para obter o estado sucessor
                if sn:
                    self.__transicoes[(s, a)] = sn  # Armazena as transições no dicionário
                
        
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()  # Obtém o estado atual do modelo de planejamento
    
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()  # Obtém todos os estados do modelo de planejamento
    
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()  # Obtém todos os operadores do modelo de planejamento
    
    def S(self):
        return self.obter_estados()  # Retorna os estados do PDM
    
    def A(self, s):
        # Retorna as ações possíveis, exceto para estados que são objetivos
        return self.obter_operadores() if s not in self.__objectivos else []
    
    def T(self, s, a, sn):
        # Em um ambiente determinístico, a transição ocorre se a chave (s, a) estiver no dicionário
        return 1 if self.__transicoes.get((s, a)) is not None else 0  # Retorna 1 se a transição existir, caso contrário 0
    
    def R(self, s, a, sn):
        # Retorna a recompensa máxima se o estado sucessor for um objetivo, caso contrário retorna 0
        return self.__rmax if sn in self.__objectivos else 0
    
    def suc(self, s, a):
        sn = self.__transicoes.get((s, a))  # Obtém o estado sucessor para a transição
        # Retorna o estado sucessor como uma lista, ou uma lista vazia se não houver sucessor
        return [sn] if sn is not None else []
