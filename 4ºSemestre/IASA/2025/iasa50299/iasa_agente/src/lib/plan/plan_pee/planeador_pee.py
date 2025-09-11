from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPEE
from plan.planeador import Planeador
from pee.melhor_prim.procura_informada import ProcuraInformada
from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA

class PlaneadorPEE(Planeador):
    """
    Implementa um planeador automático baseado no método PEE (Procura em Espaços de Estados).
    Utiliza diferentes métodos de procura heurística para gerar planos de ação a partir dos objetivos fornecidos.
    """

    def __init__(self):
        """
        Inicializa o planeador, configurando o mecanismo de procura.

        O mecanismo de procura é inicialmente configurado com ProcuraAA, mas pode ser alterado dependendo da necessidade.
        """
        # Configura o mecanismo de procura, inicialmente como ProcuraAA
        self.__mec_pee = ProcuraAA()

    def planear(self, modelo_plan, objectivos):
        """
        Gera um plano de ação baseado nos objetivos fornecidos, utilizando o modelo de planejamento.

        O plano é criado ao resolver o problema de planejamento com o mecanismo de procura configurado.
        Se a solução for encontrada, um plano de ação é gerado e retornado.
        Caso contrário, retorna None.
        """
        # Define o estado final como o primeiro objetivo fornecido
        estado_final = objectivos[0]
        
        # Cria um problema de planejamento com o modelo fornecido e o estado final desejado
        problema = ProblemaPlan(modelo_plan, estado_final)
        
        # Cria uma heurística baseada na distância até o estado final
        heuristica = HeurDist(estado_final)
        
        # Usa o mecanismo de procura para encontrar a solução
        solucao = self.__mec_pee.procurar(problema, heuristica)
        
        # Se uma solução for encontrada, cria e retorna o plano de ação
        if solucao is None:
            return None  # Caso não haja solução, pode-se retornar None ou tratar de outra forma
        
        # Cria o plano a partir da solução encontrada
        plano = PlanoPEE(solucao)
        return plano