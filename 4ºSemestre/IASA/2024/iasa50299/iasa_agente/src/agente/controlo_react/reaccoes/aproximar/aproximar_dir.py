from controlo_react.reaccoes.aproximar.estimulo_alvo import EstimuloAlvo
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from lib.ecr.reaccao import Reaccao

class AproximarDir(Reaccao):
    """
    Sub-comportamento de Aproximação Direcional ao Alvo

    Este sub-comportamento é responsável por gerar informação de prioridade relativa à proximidade a um alvo detectado numa direção específica e 
    selecionar a ação de mover-se nessa direção para se aproximar do alvo mais próximo, com base nessas prioridades.
    """
    def __init__(self, direccao):
        """
        Inicializa o sub-comportamento de aproximação direcional ao alvo.

        Args:
            direccao (Direccao): A direção na qual o agente deve se mover para se aproximar do alvo.
        """
        # Inicializa a classe base Reaccao com o estímulo de alvo na direção específica
        # e a resposta de mover-se nessa direção
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))
