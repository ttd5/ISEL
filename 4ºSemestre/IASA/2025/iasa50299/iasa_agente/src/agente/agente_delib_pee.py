"""
AgenteDelibPEE
@author: Tatiana Damaya

No terminal antes de executar o código, para resolver os imports:
export PYTHONPATH=/Users/tatianadamaya/Documents/ISEL/4ºSemestre/IASA/iasa50299/iasa_agente/src:/Users/tatianadamaya/Documents/ISEL/4ºSemestre/IASA/iasa50299/iasa_agente/src/lib
"""

from controlo_delib.controlo_delib import ControloDelib
from lib.plan.plan_pee.planeador_pee import PlaneadorPEE
from agente_delib import AgenteDelib  
from lib.sae import Simulador



class AgenteDelibPEE(AgenteDelib):
    def __init__(self):
        planeador = PlaneadorPEE()
        super().__init__(planeador)  
        self.controlo.vista = self.vista  

# Ativação
if __name__ == "__main__":
    Simulador(4, AgenteDelibPEE(), vista_modelo=True).executar()


