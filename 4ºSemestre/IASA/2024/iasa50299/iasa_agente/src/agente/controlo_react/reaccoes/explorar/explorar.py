import random
from lib.ecr.comportamento import Comportamento
from lib.sae.ambiente.direccao import Direccao
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover

class Explorar(Comportamento):
    """
    Comportamento de Exploração Aleatória

    Este comportamento é responsável por explorar o ambiente movendo-se em direções aleatórias.
    É menos eficiente do que um sistema que utiliza memória para navegar no espaço, onde a exploração é mais sistemática.

    Methods:
        activar(percepcao): Ativa o comportamento de exploração, escolhendo uma direção aleatória
        para mover-se com base na percepção do ambiente atual.

    Attributes:
        Nenhum.
    """
    def activar(self, percepcao):
        """
        Ativa o comportamento de exploração, escolhendo uma direção aleatória para mover-se.

        Args:
            percepcao (Percepcao): A percepção atual do ambiente pelo agente.

        Returns:
            Direccao: A direção escolhida aleatoriamente para o movimento.
        """
        # Escolhe uma direção aleatória dentre as direções disponíveis
        direccao = random.choice(list(Direccao))
        # Ativa a resposta de mover-se na direção escolhida
        return RespostaMover(direccao).activar(percepcao)