from lib.mod.agente.estado_agente import EstadoAgente
from lib.plan.modelo.modelo_plan import ModeloPlan
from agente.controlo_delib.modelo.operador_mover import OperadorMover
from lib.sae.ambiente.direccao import Direccao
import math
from lib.sae.ambiente.elemento import Elemento

class ModeloMundo(ModeloPlan):
    """Representação interna do ambiente/problema

    Este modelo é utilizado no contexto de um agente deliberativo, que toma decisões com base em processos de planeamento e raciocínio automático. 
    A resolução de problemas de planeamento é realizada sobre uma abstração do domínio do problema, conhecida como espaço de estados.

    Componentes principais:
    - Estado: cada configuração possível na resolução do problema.
    - Operadores: ações que produzem mudanças (transformações) de uma configuração para outra, gerando novos estados.
    
    O ModeloMundo implementa a interface do modelo de planeamento, permitindo que seja utilizado por um planejador.
    Em arquiteturas deliberativas, o comportamento do agente é gerado com base em processos de planeamento suportados por representações internas do ambiente (modelo do mundo).
    """
    def __init__(self):
        """Inicializa o modelo do mundo com atributos padrão"""
        self.__alterado = False  # Flag para indicar se o modelo foi alterado
        self.__estado = None  # Estado atual do agente
        self.__estados = []  # Lista de estados conhecidos
        self.__elementos = {}  # Dicionário de elementos no ambiente
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]  # Lista de operadores de movimento

    @property
    def alterado(self):
        """Propriedade para acessar o estado alterado"""
        return self.__alterado
    
    @property
    def elementos(self):
        """Propriedade para acessar os elementos do ambiente"""
        return self.__elementos
    
    def obter_estado(self):
        """Obtém o estado atual do agente"""
        return self.__estado
    
    def obter_estados(self):
        """Obtém todos os estados conhecidos"""
        return self.__estados
    
    def obter_operadores(self):
        """Obtém os operadores disponíveis"""
        return self.__operadores
    
    def obter_elemento(self, estado):
        """Obtém o elemento na posição do estado especificado
        
        Args:
            estado (EstadoAgente): O estado do agente cuja posição será usada para obter o elemento.
        
        Returns:
            Elemento: O elemento na posição do estado, ou None se não houver elemento.
        """
        return self.__elementos.get(estado.posicao)
    
    def distancia(self, estado):
        """Calcula a distância entre o estado atual do agente e outro estado
        
        Args:
            estado (EstadoAgente): O estado para o qual a distância será calculada.
        
        Returns:
            float: A distância euclidiana entre os dois estados.
        """
        return math.dist(estado.posicao, self.__estado.posicao)
    
    def actualizar(self, percepcao):
        """Atualiza o modelo do mundo com base na percepção do ambiente
        
        Args:
            percepcao (Percepcao): A percepção atual do ambiente.
        """
        self.__estado = EstadoAgente(percepcao.posicao)  # Atualiza o estado do agente com a nova posição
        if self.__elementos != percepcao.elementos:
            # Se os elementos percebidos são diferentes dos conhecidos, atualiza o modelo
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
            self.__alterado = True  # Marca o modelo como alterado
        else:
            self.__alterado = False  # Não houve alteração no modelo
    
    def mostrar(self, vista):
        """Mostra a representação visual do ambiente
        
        Args:
            vista (Vista): A interface visual para mostrar os elementos do ambiente.
        """
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)  # Mostra os elementos alvo e obstáculo
        vista.marcar_posicao(self.__estado.posicao)  # Marca a posição atual do agente na vista