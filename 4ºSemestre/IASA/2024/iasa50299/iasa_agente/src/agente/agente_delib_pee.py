"""
AgenteDelibPEE
@author: Tatiana Damaya

No terminal antes de executar o código, para resolver os imports:
export PYTHONPATH=/Users/tatianadamaya/Documents/ISEL/4ºSemestre/IASA/iasa50299/iasa_agente/src:/Users/tatianadamaya/Documents/ISEL/4ºSemestre/IASA/iasa50299/iasa_agente/src/lib
"""

from agente.controlo_delib.controlo_delib import ControloDelib
from lib.sae.agente.agente import Agente
from lib.sae.simulador import Simulador
from lib.plan.plan_pee.planeador_pee import PlaneadorPEE

# Definição da classe AgenteDelibPEE
class AgenteDelibPEE(Agente):
    
    def __init__(self):
        # Inicialização do controlo com o PlaneadorPEE
        controlo = ControloDelib(PlaneadorPEE(3))
        # Chamada ao construtor da classe base Agente
        super().__init__(controlo)
        
# Verificação se o script está sendo executado diretamente
if __name__ == "__main__":
    # Inicialização do simulador e o AgenteDelibPEE
    Simulador(4, AgenteDelibPEE()).executar()