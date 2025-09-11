"""
AgenteReact
@author: Tatiana Damaya

No terminal antes de executar o código, para resolver os imports:
export PYTHONPATH=/Users/tatianadamaya/Documents/ISEL/6ºSemestre/IASA/iasa50299/iasa_agente/src:/Users/tatianadamaya/Documents/ISEL/6ºSemestre/IASA/iasa50299/iasa_agente/src/lib
"""

from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.recolher_alvos import RecolherAlvos
from lib.sae.agente.agente import Agente
from lib.sae.simulador import Simulador


# Definição da classe AgenteReact

class AgenteReact(Agente):
    def __init__(self):
        super().__init__()
        self.__comportamento = RecolherAlvos()
        self._controlo = ControloReact(self.__comportamento)
    
    def executar(self):
        percepcao = self._percepcionar()
        accao = self._controlo.processar(percepcao)
        self._actuar(accao)

if __name__ == "__main__":
    agente = AgenteReact()
    simulador = Simulador(1, agente)
    simulador.executar()