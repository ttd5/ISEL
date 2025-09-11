"""
AgenteReact
@author: Tatiana Damaya

No terminal antes de executar o código, para resolver os imports:
export PYTHONPATH=/Users/tatianadamaya/Documents/ISEL/4ºSemestre/IASA/iasa50299/iasa_agente/src:/Users/tatianadamaya/Documents/ISEL/4ºSemestre/IASA/iasa50299/iasa_agente/src/lib
"""

from agente.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.explorar.explorar import Explorar
from controlo_react.reaccoes.recolher import Recolher
from lib.sae.agente.agente import Agente
from lib.sae.simulador import Simulador

# Definição da classe AgenteReact
class AgenteReact(Agente):

    def __init__(self):
        # Inicialização do controlo com o comportamento de recolher
        controlo = ControloReact(Recolher([AproximarAlvo(), EvitarObst(), Explorar()]))
        # Chamada ao construtor da classe base Agente
        super().__init__(controlo)
        
# Verificação se o script está sendo executado diretamente
if __name__ == "__main__":
    # Inicialização do simulador com 1 unidade de tempo e o AgenteReact
    Simulador(1, AgenteReact()).executar()