"""
Teste SAE
@author: Tatiana Damaya

No terminal antes de executar o código, para resolver os imports:
export PYTHONPATH=/Users/tatianadamaya/Documents/ISEL/6ºSemestre/IASA/iasa50299/iasa_agente/src:/Users/tatianadamaya/Documents/ISEL/6ºSemestre/IASA/iasa50299/iasa_agente/src/lib
"""

from lib.sae import Agente, Simulador

class Teste(Agente):

    def __init__(self):
        super().__init__()

    def executar(self):
        print("processar")

agente = Teste()
Simulador(1, agente).executar()