"""
AgenteSimul
@author: Tatiana Damaya

No terminal antes de executar o código, para resolver os imports:
export PYTHONPATH=/Users/tatianadamaya/Documents/ISEL/4ºSemestre/IASA/iasa50299/iasa_agente/src:/Users/tatianadamaya/Documents/ISEL/4ºSemestre/IASA/iasa50299/iasa_agente/src/lib
"""

from lib.sae import Agente, Simulador
from agente.controlo_simul.controlo_simul import ControloSimul

# Definição da classe AgenteSimul
class AgenteSimul(Agente):
    """
    Agente Simulado
    """
    def __init__(self):
        # Inicialização do controlo simulado
        controlo = ControloSimul()
        # Chamada ao construtor da classe base Agente
        super().__init__(controlo)
        
# Verificação se o script está sendo executado diretamente
if __name__ == "__main__":
    # Inicialização do simulador com 1 unidade de tempo e o AgenteSimul
    Simulador(1, AgenteSimul()).executar()