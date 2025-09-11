#from sae.agente.agente import Agente
from lib.sae import Agente
from agente.controlo_delib.controlo_delib import ControloDelib

class AgenteDelib(Agente):
    def __init__(self, planeador):
        super().__init__()
        self._controlo = ControloDelib(planeador)

    def executar(self):
        percepcao = self._percepcionar()
        accao = self._controlo.processar(percepcao)
        self._actuar(accao)

    @property
    def controlo(self):
        return self._controlo  
