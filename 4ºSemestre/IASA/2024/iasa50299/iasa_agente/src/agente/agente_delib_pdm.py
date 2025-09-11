"""
AgenteDelibPDM
@author: Tatiana Damaya

No terminal antes de executar o código, para resolver os imports:
export PYTHONPATH=/Users/tatianadamaya/Documents/ISEL/4ºSemestre/IASA/iasa50299/iasa_agente/src:/Users/tatianadamaya/Documents/ISEL/4ºSemestre/IASA/iasa50299/iasa_agente/src/lib
"""
from controlo_delib.controlo_delib import ControloDelib
from lib.plan.plan_pdm.planeador_pdm import PlaneadorPDM
from lib.sae import Simulador
from lib.sae.agente.agente import Agente

# Definição da classe AgenteDelibPDM
class AgenteDelibPDM(Agente):
    
    def __init__(self):
        # Inicialização do controlo com o PlaneadorPDM
        controlo = ControloDelib(PlaneadorPDM(0.95,1))
        # Chamada ao construtor da classe base Agente
        super().__init__(controlo)
        
# Verificação se o script está a ser executado diretamente
if __name__ == "__main__":
    # Inicialização do simulador e o AgenteDelibPDM
    Simulador(4, AgenteDelibPDM()).executar()