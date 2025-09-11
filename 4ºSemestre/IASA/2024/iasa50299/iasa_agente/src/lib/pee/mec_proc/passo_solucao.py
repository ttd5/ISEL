from dataclasses import dataclass
from mod.estado import Estado
from mod.operador import Operador

@dataclass
class PassoSolucao:
    """Representa um passo numa solução de um problema, contendo um estado e um operador."""
    estado: Estado  # O estado associado ao passo da solução
    operador: Operador  # O operador aplicado para chegar ao estado seguinte