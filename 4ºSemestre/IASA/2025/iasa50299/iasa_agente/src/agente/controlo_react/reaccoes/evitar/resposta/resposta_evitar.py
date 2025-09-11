from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from lib.sae.ambiente.direccao import Direccao
from lib.sae.agente.percepcao import Percepcao
from lib.sae import Rodar

class RespostaEvitar(RespostaMover):
    """
    Resposta para evitar obstáculos rodando até encontrar direção livre.
    """
    def __init__(self, dir_inicial=Direccao.NORTE):
        super().__init__(dir_inicial)

    def activar(self, percepcao, intensidade = 0):
        """
        Ativa a resposta de evitar obstáculos com base na perceção do agente

        Parâmetros:
        percepcao (objeto): Contém informações do ambiente percebido pelo agente
        intensidade (float): Representa a intensidade do estímulo associado ao comportamento

        Funcionamento:
        - A direção atual do agente é obtida através de `percepcao.direccao`
        - Se for detectado um obstáculo na direção atual (`contacto_obst`), o agente irá calcular uma nova direção,
          usando `rodar` como mecanismo para desviar do obstáculo
        - A ação de rodar é configurada e ativada utilizando a classe `Rodar`
        """
        dir_agente = percepcao.direccao #obtém a direção atual do agente

        if percepcao.contacto_obst(dir_agente): #verifica se há obstáculo na direção atual
            dir_resposta = dir_agente.rodar() #calcula uma nova direção para desviar do obstáculo
            self._accao = Rodar(dir_resposta) #configura a ação de rodar para a nova direção
            return super().activar(percepcao, intensidade) #ativa a resposta configurada