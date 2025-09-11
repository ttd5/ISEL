"""
Direcção de movimentação no ambiente
@author: Luís Morgado
"""

import math
from enum import Enum

#__________________________________________________

ANG_90 = math.pi / 2
ANG_180 = math.pi
ANG_360 = math.pi * 2

class Direccao(Enum):
    """
    Direcção de movimento
    """
    NORTE = ANG_90
    SUL   = -ANG_90
    ESTE  = 0
    OESTE = ANG_180

    def rodar(self, passo_rot=1):
        """
        Rodar direcção
        @param passo_rot: passo de rotação (+1: 90º, -1: -90º)
        @return: nova direcção
        """
        # Calcular novo ângulo, normalizado no intervalo ]-pi, pi]
        novo_angulo = self.value + passo_rot * ANG_90 % (ANG_360)
        if novo_angulo > ANG_180:
            novo_angulo -= ANG_360
        # Retornar instância de direcção por valor
        return Direccao(novo_angulo)

