from ..planeador import Planeador
from .plano_pdm import PlanoPDM
from pdm.pdm import PDM
from pdm.modelo.modelo_pdm_plan import ModeloPDMPlan

class PlaneadorPDM(Planeador):
    """
    Classe responsável por planejar ações utilizando o Processo de Decisão Markoviano (PDM).
    Herda da classe Planeador e usa o algoritmo PDM para resolver o problema de planeamento, gerando um plano de ação.
    """

    def __init__(self, gama=0.85, delta_max=1.0):
        self.__gama = gama  # Define o fator de desconto usado para calcular a utilidade futura
        self.__delta_max = delta_max  # Define o limite máximo de variação aceito para a convergência do algoritmo
        self.__pos_init = None  # Inicializa o estado inicial como None

    def planear(self, modelo_plan, objectivos):
        """
        Cria um plano de ação com base no modelo de planejamento e nos objetivos fornecidos.

        Se não forem fornecidos objetivos, o estado inicial será usado como objetivo.
        O modelo PDM é instanciado, e o problema é resolvido utilizando o algoritmo PDM para calcular a utilidade e a política.
        """
        if not objectivos:
            objectivos.append(self.__pos_init)  # Se não houver objetivos, define o estado inicial como objetivo
        modelo = ModeloPDMPlan(modelo_plan, objectivos)  # Cria um modelo PDM com o modelo de planejamento e os objetivos
        problema = PDM(modelo, self.__gama, self.__delta_max)  # Instancia o PDM com os parâmetros fornecidos
        utilidade, politica = problema.resolver()  # Resolve o problema PDM, obtendo utilidade e política
        return PlanoPDM(utilidade, politica)  # Retorna o plano de ação com a utilidade e a política calculadas
