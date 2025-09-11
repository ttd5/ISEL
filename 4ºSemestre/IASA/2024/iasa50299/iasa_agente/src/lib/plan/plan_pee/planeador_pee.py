from lib.plan.planeador import Planeador
from lib.pee.melhor_prim.procura_aa import ProcuraAA
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.plano_pee import PlanoPEE
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_sofrega import ProcuraSofrega

class PlaneadorPEE(Planeador):
    """Um planeador para o paradigma PEE (Procura em Espaço de Estados)."""

    def __init__(self, procura):
        """
        Inicializa o planeador com um tipo de procura específico.

        Args:
            procura (int): O tipo de procura a ser utilizado.
        """
        self.__tipo = procura  # Armazena o tipo de procura

        # Seleciona o mecanismo de procura com base no tipo especificado
        if procura == 1:
            self.__mec_pee = ProcuraAA()  # Utiliza a procura AA
        elif procura == 2:
            self.__mec_pee = ProcuraCustoUnif()  # Utiliza a procura de Custo Uniforme
        elif procura == 3:
            self.__mec_pee = ProcuraSofrega()  # Utiliza a procura Gulosa

    def planear(self, modelo_plan, objectivos):
        """
        Planeja a solução com base no modelo de planeamento e nos objetivos.

        Args:
            modelo_plan (ModeloPlan): O modelo de planeamento.
            objectivos (list): Uma lista de objetivos a serem alcançados.

        Returns:
            PlanoPEE: O plano de ação resultante da procura.
        """
        solucao = None

        # Realiza a procura com ou sem heurística, dependendo do tipo de procura
        if self.__tipo == 1 or self.__tipo == 3:
            solucao = self.__mec_pee.procurar(ProblemaPlan(modelo_plan, objectivos[0]), HeurDist(objectivos[0]))
        else:
            solucao = self.__mec_pee.procurar(ProblemaPlan(modelo_plan, objectivos[0]))

        # Retorna o plano resultado
        return PlanoPEE(solucao)