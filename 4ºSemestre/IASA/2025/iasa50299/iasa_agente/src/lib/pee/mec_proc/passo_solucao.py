from dataclasses import dataclass
from mod.estado import Estado
from mod.operador import Operador

@dataclass
class PassoSolucao:
    """
    @author: Tatiana Damaya

    Representa um passo numa solução de um problema, contendo um estado e um operador.
    
    Cada instância desta classe corresponde a um passo específico na resolução de um problema,
    onde é aplicado um operador a um estado para alcançar um novo estado.
    """

    estado: Estado  # O estado associado ao passo da solução.
    operador: Operador  # O operador aplicado para alcançar o estado seguinte.
