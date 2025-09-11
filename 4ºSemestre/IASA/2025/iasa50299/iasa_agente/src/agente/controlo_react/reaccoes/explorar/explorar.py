"""
Comportamento Explorar
@author: Tatiana Damaya
"""

from lib.ecr.comportamento import Comportamento
from lib.ecr.resposta import Resposta
from lib.sae import Rodar, Avancar, Direccao
from random import choice, random

class Explorar(Comportamento):
    """
    Comportamento de Exploração Aleatória

    Esta classe define um comportamento reativo simples que permite ao agente explorar o ambiente
    quando não há estímulos relevantes a considerar. O agente escolhe aleatoriamente entre
    avançar ou rodar, promovendo uma navegação básica.

    Attributes:
        __taxa_rotacao (float): Probabilidade de o agente rodar em vez de avançar.
        __direccoes (list[Direccao]): Lista de direções possíveis no ambiente.
    """

    def __init__(self, taxa_rotacao=0.1):
        """
        Inicializa o comportamento de exploração com uma taxa de rotação específica.

        Args:
            taxa_rotacao (float): Probabilidade de rotação a cada passo. Valores mais altos 
                                  aumentam a frequência de rotação.
        """
        self.__taxa_rotacao = taxa_rotacao
        self.__direccoes = list(Direccao)

    def activar(self, percepcao):
        """
        Decide aleatoriamente entre avançar ou rodar numa direção aleatória.

        Args:
            percepcao (Percepcao): Percepção atual do agente no ambiente.

        Returns:
            Accao: A ação a ser executada pelo agente.
        """
        accao = None
        if random() < self.__taxa_rotacao:
            accao = Rodar(choice(self.__direccoes))
        else:
            accao = Avancar()
        resposta = Resposta(accao)
        return resposta.activar(percepcao)
