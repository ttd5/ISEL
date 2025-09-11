from lib.plan.plan_pdm.plano_pdm import PlanoPDM
from lib.pdm.pdm import PDM
from lib.plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from lib.plan.planeador import Planeador

class PlaneadorPDM(Planeador):
    """Classe responsável por planear usando PDM (Processo de Decisão de Markov).

    PlaneadorPDM utiliza um modelo de planeamento para criar um ModeloPDMPlan, que é então usado para resolver um PDM e gerar um plano de ação.

    Attributes:
        gama (float): O fator de desconto para PDM (por padrão, 0.85).
        delta_max (float): O limite de convergência para PDM (por padrão, 1.0).
    """

    def __init__(self, gama=0.85, delta_max=1.0):
        """Inicializa o PlaneadorPDM com os parâmetros gama e delta_max."""
        self.__gama = gama
        self.__delta_max = delta_max

    def planear(self, modelo_plan, objectivos):
        """Planeia usando PDM.

        Args:
            modelo_plan: O modelo de planejamento.
            objectivos: Uma lista de estados que representam os objetivos.

        Returns:
            PlanoPDM: O plano de ação resultante.
        """
        # Cria um ModeloPDMPlan com o modelo de planejamento e os objetivos
        modelo_plan = ModeloPDMPlan(modelo_plan, objectivos)

        # Resolve o PDM usando o modelo criado
        pdm = PDM(modelo_plan, self.__gama, self.__delta_max)
        U, pol = pdm.resolver()

        # Se um plano de ação foi gerado, retorna um PlanoPDM
        if U and pol:
            return PlanoPDM(U, pol)
