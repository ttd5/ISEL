from math import cos, sin, dist
from agente.controlo_delib.estado_agente import EstadoAgente
from lib.sae import Accao

class OperadorMover:
    """
    Classe que representa o operador de movimento de um agente.
    Permite mover o agente em uma direção específica, alterando sua posição no modelo do mundo.
    """

    def __init__(self, modelo_mundo, direccao):
        """
        Inicializa o operador de movimento com a direção e o modelo do mundo.

        O modelo do mundo é usado para acessar e validar o novo estado após o movimento. 
        A direção define para qual direção o agente vai se mover.
        """
        self.__modelo_mundo = modelo_mundo
        self.__ang = direccao.value  # Armazena o ângulo da direção de movimento
        self.__accao = Accao(direccao)  # Associa a ação ao movimento

    @property
    def ang(self):
        """Retorna o ângulo da direção de movimento."""
        return self.__ang

    @property
    def accao(self):
        """Retorna a ação associada ao movimento na direção específica."""
        return self.__accao

    def __repr__(self):
        """Retorna uma representação em string do operador de movimento."""
        return "OperadorMover(%s)" % self.accao

    def aplicar(self, estado):
        """
        Aplica o movimento ao estado do agente e gera o novo estado.

        A nova posição do agente é calculada com base na direção de movimento. 
        Se o novo estado for válido dentro do modelo do mundo, ele será retornado.
        Caso contrário, nada será retornado.
        """
        nova_posicao = self.__translacao(estado.posicao, self.accao.passo, self.accao.ang)
        novo_estado = EstadoAgente(nova_posicao)

        # Verifica se o novo estado é válido no modelo do mundo
        if novo_estado in self.__modelo_mundo.obter_estados():
            return novo_estado

    def custo(self, estado, estado_suc):
        """
        Calcula o custo da transição entre dois estados com base na distância entre eles.

        O custo é sempre no mínimo 1, mas pode aumentar dependendo da distância.
        """
        return max(1, dist(estado.posicao, estado_suc.posicao))

    def __translacao(self, posicao, distancia, ang):
        """
        Calcula a nova posição do agente com base na direção e distância do movimento.

        A translação é feita aplicando funções trigonométricas (cosseno e seno) para determinar os deslocamentos em x e y.
        """
        x, y = posicao  # Pega a posição atual do agente

        # Calcula os deslocamentos nas coordenadas x e y
        dx = round(distancia * cos(ang))
        dy = -round(distancia * sin(ang))
        
        return (x + dx, y + dy)  # Retorna a nova posição do agente após o movimento