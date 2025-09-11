"""
Acção rodar
@author: Luís Morgado
"""

from .accao import Accao

#_______________________________________________________________________________

class Rodar(Accao):
    """Acção rodar mantendo a posição (passo = 0)"""
    def __init__(self, direccao):
        super().__init__(direccao, 0)
        
    def __repr__(self):
        return "Rodar:" + super().__repr__()
