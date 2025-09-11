from controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from lib.ecr.prioridade import Prioridade
from lib.sae.ambiente.direccao import Direccao

class AproximarAlvo(Prioridade):
    """
    Comportamento Composto: Aproximar do Alvo com Base em Prioridades

    Este comportamento composto seleciona ações com base em prioridades associadas, que podem variar ao longo da execução. 
    A coordenação dos sub-comportamentos depende das suas características e do objetivo do comportamento composto que os agrega.

    O objetivo do comportamento "AproximarAlvo" é aproximar o agente do alvo mais próximo.
    Cada sub-comportamento direcionado (AproximarDir) gera informações de prioridade relativas à proximidade de um alvo detectado. 
    O mecanismo de seleção de ação por prioridade escolhe a ação que aproxima o agente do alvo mais próximo com base nessas prioridades.

    Este exemplo considera que o agente pode perceber e mover-se em quatro direções:
    NORTE, SUL, ESTE, OESTE. Portanto, os sub-comportamentos específicos para cada direção são:
    - Aproximar alvo (direção = NORTE)
    - Aproximar alvo (direção = SUL)
    - Aproximar alvo (direção = ESTE)
    - Aproximar alvo (direção = OESTE)

    Cada sub-comportamento direcionado deve gerar informações de prioridade relativas à proximidade de um alvo detectado e deve haver um mecanismo de seleção de ação 
    or prioridade que produza a ação de aproximação ao alvo mais próximo com base nessas prioridades.
    """
    def __init__(self):
        """
        Inicializa o comportamento composto AproximarAlvo com sub-comportamentos direcionais.
        """
        # Cria uma lista de sub-comportamentos de aproximação em quatro direções
        comportamentos = [
            AproximarDir(Direccao.NORTE),
            AproximarDir(Direccao.SUL),
            AproximarDir(Direccao.ESTE),
            AproximarDir(Direccao.OESTE)
        ]
        # Inicializa a classe base Prioridade com os sub-comportamentos criados
        super().__init__(comportamentos)