"""
Comportamento Explorar com Memória
@author: Tatiana Damaya
"""

from random import choice
from lib.sae.agente.rodar import Rodar
from lib.sae.ambiente.direccao import Direccao
from lib.ecr.comportamento import Comportamento
from lib.ecr.resposta import Resposta
from lib.sae.agente.avancar import Avancar

class ExplorarMem(Comportamento):
    """
    Comportamento de Exploração com Memória

    Este comportamento permite ao agente explorar o ambiente de forma mais eficiente,
    evitando repetir direções já visitadas. Quando o agente deteta que está a visitar uma 
    situação (posição + direção) nova, avança. Caso contrário, roda para uma direção aleatória 
    diferente da atual, para evitar repetição.

    Attributes:
        _dim_max_mem (int): Tamanho máximo da memória de situações visitadas.
        __memoria (list): Lista de tuplos (posição, direção) representando situações já visitadas.
        __resposta (Resposta): Objeto de resposta responsável por ativar a ação definida.
    """

    def __init__(self, dim_max_mem=100):
        """
        Inicializa o comportamento com memória de exploração.

        Args:
            dim_max_mem (int): Número máximo de situações a manter na memória. As mais antigas
                               são descartadas quando o limite é atingido.
        """
        self._dim_max_mem = dim_max_mem
        self.__memoria = []
        self.__resposta = Resposta(Avancar())  # Ação padrão inicial

    def activar(self, percepcao):
        """
        Ativa o comportamento com base na situação atual do agente.

        Se a situação ainda não foi visitada, avança e guarda-a na memória.
        Caso já tenha sido visitada, roda para uma nova direção aleatória.

        Args:
            percepcao (Percepcao): Perceção atual do ambiente pelo agente.

        Returns:
            Accao: A ação a ser executada (Avançar ou Rodar).
        """
        situacao = (percepcao.posicao, percepcao.direccao)

        if situacao not in self.__memoria:
            self.__memoria.append(situacao)
            if len(self.__memoria) > self._dim_max_mem:
                self.__memoria.pop(0)
            accao = Avancar()
        else:
            # Roda para uma nova direção aleatória diferente da atual
            direccoes_possiveis = [d for d in Direccao if d != percepcao.direccao]
            nova_direccao = choice(direccoes_possiveis)
            accao = Rodar(nova_direccao)

        # Atualiza a ação da resposta e ativa
        self.__resposta._accao = accao
        return self.__resposta.activar(percepcao)