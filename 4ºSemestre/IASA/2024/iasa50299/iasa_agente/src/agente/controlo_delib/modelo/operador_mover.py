import math

from lib.mod.operador import Operador
from lib.sae.agente.accao import Accao
from lib.mod.agente.estado_agente import EstadoAgente

class OperadorMover(Operador):
    """Operador de Movimento: Define a transformação (transição de estado) e o custo associado.
    
    Este operador é responsável por mover o agente numa direção específica dentro do modelo do mundo, atualizando o seu estado conforme necessário e calculando o custo da transição.
    """
    def __init__(self, modelo_mundo, direcao):
        """Inicializa o operador de movimento.
        
        Args:
            modelo_mundo (ModeloMundo): A referência ao modelo do mundo.
            direcao (Direccao): A direção na qual o operador moverá o agente.
        """
        self.__modelo_mundo = modelo_mundo  # Referência ao modelo do mundo
        self.__ang = direcao.value  # Ângulo da direção em radianos
        self.__accao = Accao(direcao)  # Ação correspondente à direção

    @property
    def accao(self):
        """Propriedade para aceder a ação do operador"""
        return self.__accao
    
    @property
    def ang(self):
        """Propriedade para aceder o ângulo da direção"""
        return self.__ang
    
    def aplicar(self, estado):
        """Aplica a transformação de estado ao mover o agente.
        
        Args:
            estado (EstadoAgente): O estado atual do agente.
        
        Returns:
            EstadoAgente: O novo estado do agente após o movimento, se válido.
        """
        x, y = estado.posicao  # Posição atual do agente
        dx = round(self.__accao.passo * math.cos(self.__ang))  # Deslocamento em x
        dy = -round(self.__accao.passo * math.sin(self.__ang))  # Deslocamento em y
        nova_pos = (x + dx, y + dy)  # Nova posição após o movimento
        novo_estado = EstadoAgente(nova_pos)  # Novo estado do agente

        # Verifica se o novo estado está nos estados conhecidos do modelo do mundo
        if novo_estado in self.__modelo_mundo.obter_estados():
            return novo_estado  # Retorna o novo estado se for válido
    
    def custo(self, estado, estado_suc):
        """Calcula o custo da transição entre estados.
        
        Args:
            estado (EstadoAgente): O estado atual do agente.
            estado_suc (EstadoAgente): O estado sucessor após o movimento.
        
        Returns:
            float: O custo da transição entre os estados.
        """
        if estado_suc:
            # Retorna o custo baseado na distância euclidiana, garantindo um custo mínimo de 1
            return max(1, math.dist(estado.posicao, estado_suc.posicao))