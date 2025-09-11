from agente.controlo_react.reaccoes.evitar.estimulo.estimulo_obst import EstimuloObst
from lib.ecr.reaccao import Reaccao

class EvitarDir(Reaccao):
    """
    Reação para Evitar uma Direção Específica

    Esta reação é responsável por evitar uma direção específica quando um obstáculo é detectado nessa direção. 
    Herda da classe Reaccao e utiliza o estímulo EstimuloObst para detectar a presença de um obstáculo na direção especificada.

    Args:
        direccao (Direccao): A direção na qual o agente deve evitar um obstáculo.
        resposta (Resposta): A resposta a ser executada quando um obstáculo é detectado.
    """
    def __init__(self, direccao, resposta):
        """
        Inicializa a reação para evitar uma direção específica.
        
        Args:
            direccao (Direccao): A direção na qual o agente deve evitar um obstáculo.
            resposta (Resposta): A resposta a ser executada quando um obstáculo é detectado.
        """
        # Inicializa a classe base Reaccao com o estímulo de obstáculo na direção especificada e a resposta fornecida
        super().__init__(EstimuloObst(direccao), resposta)