from controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from controlo_react.reaccoes.evitar.resposta_evitar import RespostaEvitar
from lib.ecr.hierarquia import Hierarquia
from lib.sae.ambiente.direccao import Direccao

class EvitarObst(Hierarquia):
    """
    Comportamento Hierárquico para Evitar Obstáculos

    Este comportamento hierárquico organiza os sub-comportamentos de evitar obstáculos em quatro direções (NORTE, SUL, ESTE, OESTE).
    Cada sub-comportamento específico para uma direção utiliza a reação EvitarDir correspondente para detectar e evitar um obstáculo naquela direção.

    Comportamentos:
    - Evitar direcional nas 4 direções

    Args:
        comportamentos (list): Uma lista de sub-comportamentos de evitar obstáculos em direções específicas.
    """
    def __init__(self):
        """
        Inicializa o comportamento hierárquico para evitar obstáculos.
        """
        # Lista de sub-comportamentos de evitar obstáculos em direções específicas
        comportamentos = [
            EvitarDir(Direccao.NORTE, RespostaEvitar(Direccao.NORTE)),
            EvitarDir(Direccao.SUL, RespostaEvitar(Direccao.SUL)),
            EvitarDir(Direccao.ESTE, RespostaEvitar(Direccao.ESTE)),
            EvitarDir(Direccao.OESTE, RespostaEvitar(Direccao.OESTE))
        ]
        # Inicializa a classe base Hierarquia com os sub-comportamentos criados
        super().__init__(comportamentos)