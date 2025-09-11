"""
Acção rodar
@author: Luís Morgado
"""

from .accao import Accao

#_______________________________________________________________________________

class Avancar(Accao):
    """Acção um passo mantendo a direcção do agente"""
    def __init__(self):
        super().__init__(None)
        
    def __repr__(self):
        return "Avancar:" + super().__repr__()
