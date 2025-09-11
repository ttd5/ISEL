from agente.controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from agente.controlo_react.reaccoes.evitar.resposta.resposta_evitar import RespostaEvitar
from lib.ecr.hierarquia import Hierarquia
from lib.sae.ambiente.direccao import Direccao

class EvitarObst(Hierarquia):
    """
    Comportamento Hierárquico para Evitar Obstáculos

    Este comportamento organiza quatro sub-comportamentos, um para cada direção (NORTE, SUL, ESTE, OESTE).
    Cada sub-comportamento tenta evitar um obstáculo na direção correspondente usando a reação EvitarDir.

    Comportamentos:
    - Evitar obstáculo no NORTE
    - Evitar obstáculo no SUL
    - Evitar obstáculo no ESTE
    - Evitar obstáculo no OESTE

    Args:
        comportamentos (list): Lista contendo os sub-comportamentos de evitar obstáculos em direções específicas.
    """
    def __init__(self):
        """
        Inicializa o comportamento hierárquico para evitar obstáculos.
        
        Cria sub-comportamentos específicos para cada direção e os organiza numa hierarquia.
        """
        # Lista de sub-comportamentos, um para cada direção
        comportamentos = [
            EvitarDir(Direccao.NORTE, RespostaEvitar(Direccao.NORTE)),  # Sub-comportamento para evitar no NORTE
            EvitarDir(Direccao.SUL, RespostaEvitar(Direccao.SUL)),  # Sub-comportamento para evitar no SUL
            EvitarDir(Direccao.ESTE, RespostaEvitar(Direccao.ESTE)),  # Sub-comportamento para evitar no ESTE
            EvitarDir(Direccao.OESTE, RespostaEvitar(Direccao.OESTE))  # Sub-comportamento para evitar no OESTE
        ]
        # Inicializa a classe base Hierarquia com os sub-comportamentos criados
        super().__init__(comportamentos)