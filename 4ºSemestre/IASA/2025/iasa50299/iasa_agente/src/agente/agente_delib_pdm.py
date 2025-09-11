from lib.sae import Agente, Simulador
from agente.controlo_delib.controlo_delib import ControloDelib
from lib.plan.plan_pdm.planeador_pdm import PlaneadorPDM

class AgenteDelibPDM(Agente):
    """
    Agente deliberativo que utiliza Planeamento baseado em Processos de Decisão de Markov (PDM).
    """
    def __init__(self):
        self.__controlo = ControloDelib(PlaneadorPDM(gama=0.95))

    def executar(self):
        percepcao = super()._percepcionar()
        accao = self.__controlo.processar(percepcao)
        self.__controlo.mostrar(self.vista)
        super()._actuar(accao)

if __name__ == "__main__":
    Simulador = Simulador(4, AgenteDelibPDM(), vista_modelo=True)
    Simulador.executar()