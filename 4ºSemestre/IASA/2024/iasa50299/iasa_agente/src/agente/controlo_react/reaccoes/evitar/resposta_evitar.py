import random
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from lib.sae.ambiente.direccao import Direccao

class RespostaEvitar(RespostaMover):
    """
    Resposta Específica para Evitar Obstáculos

    Esta resposta é responsável por modificar a direção de movimento quando um obstáculo é detectado, escolhendo uma nova direção aleatória dentre as direções livres.

    Attributes:
        dir_inicial (Direccao): A direção inicial para o movimento.
    """
    def __init__(self, dir_inicial=Direccao.ESTE):
        """
        Inicializa a resposta de evitar com a direção inicial especificada.

        Args:
            dir_inicial (Direccao): A direção inicial para o movimento. (Padrão: Direccao.ESTE)
        """
        super().__init__(dir_inicial)
        
    def activar(self, percepcao, intensidade):
        """
        Ativa a resposta de evitar obstáculos, modificando a direção de movimento quando necessário
        ou mantendo-a, com base na percepção atual do agente e na intensidade do estímulo.

        Args:
            percepcao (Percepcao): A percepção atual do ambiente pelo agente.
            intensidade (float): A intensidade do estímulo recebido.

        Returns:
            Direccao or None: A nova direção de movimento escolhida aleatoriamente ou None se não houver direções livres.
        """
        if percepcao.contacto_obst(self._accao.direccao):
            # Se houver um obstáculo na direção atual, escolhemos uma nova direção
            direccao_livre = self.__direccao_livre(percepcao)
            if direccao_livre:
                self._accao.direccao = direccao_livre
            else:
                # Se não encontrarmos nenhuma direção livre, retornamos None
                return None
        # Se não houver obstáculo, mantemos o comportamento padrão de movimento
        return super().activar(percepcao, intensidade)

    def __direccao_livre(self, percepcao):
        """
        Verifica e retorna uma direção livre escolhida aleatoriamente entre as direções disponíveis.

        Args:
            percepcao (Percepcao): A percepção atual do ambiente pelo agente.

        Returns:
            Direccao or None: A direção livre escolhida aleatoriamente ou None se não houver direções livres.
        """
        direccoes_livres = list(Direccao)
        # Removemos as direções que têm obstáculos
        for direcao in list(direccoes_livres):
            if percepcao.contacto_obst(self._accao.direccao):
                direccoes_livres.remove(direcao)
        if direccoes_livres:
            # Escolhemos uma nova direção aleatoriamente dentre as direções livres
            return random.choice(direccoes_livres)
        # Se não houver direções livres, retornamos None
        return Noneclass RespostaEvitar(RespostaMover):
    """
    Resposta Específica para Evitar Obstáculos

    Esta resposta é responsável por modificar a direção de movimento quando um obstáculo é detectado, escolhendo uma nova direção aleatória dentre as direções livres.

    Attributes:
        dir_inicial (Direccao): A direção inicial para o movimento.
    """
    def __init__(self, dir_inicial=Direccao.ESTE):
        """
        Inicializa a resposta de evitar com a direção inicial especificada.

        Args:
            dir_inicial (Direccao): A direção inicial para o movimento. (Padrão: Direccao.ESTE)
        """
        super().__init__(dir_inicial)
        
    def activar(self, percepcao, intensidade):
        """
        Ativa a resposta de evitar obstáculos, modificando a direção de movimento quando necessário
        ou mantendo-a, com base na percepção atual do agente e na intensidade do estímulo.

        Args:
            percepcao (Percepcao): A percepção atual do ambiente pelo agente.
            intensidade (float): A intensidade do estímulo recebido.

        Returns:
            Direccao or None: A nova direção de movimento escolhida aleatoriamente ou None se não houver direções livres.
        """
        if percepcao.contacto_obst(self._accao.direccao):
            # Se houver um obstáculo na direção atual, escolhemos uma nova direção
            direccao_livre = self.__direccao_livre(percepcao)
            if direccao_livre:
                self._accao.direccao = direccao_livre
            else:
                # Se não encontrarmos nenhuma direção livre, retornamos None
                return None
        # Se não houver obstáculo, mantemos o comportamento padrão de movimento
        return super().activar(percepcao, intensidade)

    def __direccao_livre(self, percepcao):
        """
        Verifica e retorna uma direção livre escolhida aleatoriamente entre as direções disponíveis.

        Args:
            percepcao (Percepcao): A percepção atual do ambiente pelo agente.

        Returns:
            Direccao or None: A direção livre escolhida aleatoriamente ou None se não houver direções livres.
        """
        direccoes_livres = list(Direccao)
        # Removemos as direções que têm obstáculos
        for direcao in list(direccoes_livres):
            if percepcao.contacto_obst(self._accao.direccao):
                direccoes_livres.remove(direcao)
        if direccoes_livres:
            # Escolhemos uma nova direção aleatoriamente dentre as direções livres
            return random.choice(direccoes_livres)
        # Se não houver direções livres, retornamos None
        return None