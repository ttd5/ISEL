from math import dist
from agente.controlo_delib.estado_agente import EstadoAgente
from agente.controlo_delib.modelo.operador_mover import OperadorMover
from lib.sae import Direccao
from lib.sae import Elemento
from lib.plan.modelo.modelo_plan import ModeloPlan

class ModeloMundo(ModeloPlan):
    """
    Classe que representa o modelo do mundo para um agente autónomo.
    Esta classe herda de ModeloPlan e fornece informações sobre o estado do mundo, os operadores disponíveis e os elementos presentes no ambiente.
    """

    def __init__(self):
        """
        Inicializa uma nova instância do modelo do mundo.

        Este construtor configura os operadores disponíveis, o estado atual do agente, os estados conhecidos, 
        um dicionário que mapeia posições para elementos e uma flag que indica se houve alterações no mundo.
        """
        self.__operadores = [OperadorMover(self, direcao) for direcao in Direccao]  # Lista de operadores de movimento
        self.__estado = None  # Estado atual do modelo do mundo
        self.__estados = []  # Lista de estados conhecidos
        self.__elementos = dict()  # Dicionário que mapeia posições para elementos do ambiente
        self.__alterado = False  # Flag que indica se o mundo foi alterado

    @property
    def elementos(self):
        """
        Retorna o dicionário de elementos presentes no ambiente.
        
        O dicionário associa posições aos elementos localizados nessas posições.
        """
        return self.__elementos

    @property
    def alterado(self):
        """ 
        Indica se houve mudanças recentes no modelo do mundo.

        O modelo foi alterado se houver alguma modificação desde a última atualização.
        """
        return self.__alterado

    def obter_estado(self):
        """
        Retorna o estado atual do agente no mundo.

        Este é o estado atual do agente no modelo do mundo.
        """
        return self.__estado

    def obter_estados(self):
        """        
        Retorna a lista de estados conhecidos no mundo.

        Esta lista contém todos os estados conhecidos do ambiente.
        """
        return self.__estados

    def obter_operadores(self):
        """        
        Retorna os operadores disponíveis para o mundo.

        Esses operadores podem ser aplicados sobre os estados para alterar o modelo do mundo.
        """
        return self.__operadores

    def obter_elemento(self, estado):
        """
        Retorna o elemento presente na posição correspondente ao estado dado.

        Se não houver nenhum elemento nessa posição, retorna None.
        """
        return self.__elementos.get(estado.posicao)

    def distancia(self, estado):
        """
        Calcula a distância entre o estado atual e o estado fornecido.

        A distância é calculada utilizando a fórmula de distância euclidiana entre as posições dos dois estados.
        """
        return dist(estado.posicao, self.__estado.posicao)

    def actualizar(self, percepcao):
        """
        Atualiza o modelo do mundo com base na nova percepção do ambiente.

        Este método atualiza o estado do agente e verifica se houve alterações nos elementos do ambiente.
        Caso haja mudanças, ele atualiza os estados conhecidos e marca o modelo como alterado.
        """
        self.__estado = EstadoAgente(percepcao.posicao)  # Atualiza o estado do agente com a nova posição

        # Se os elementos do ambiente mudaram, atualiza os elementos e os estados conhecidos
        if self.__elementos != percepcao.elementos:
            self.__elementos = percepcao.elementos  # Atualiza os elementos no ambiente
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]  # Atualiza os estados conhecidos
            self.__alterado = True  # Marca o modelo como alterado
        else:
            self.__alterado = False  # Se não houver mudanças, marca como não alterado

    def __contains__(self, estado):
        """
        Verifica se um estado está presente na lista de estados conhecidos.

        Retorna True se o estado estiver presente, caso contrário retorna False.
        """
        return estado in self.__estados

    def mostrar(self, vista):
        """
        Exibe graficamente o modelo do mundo através da vista fornecida.

        A visualização mostra os alvos, obstáculos e a posição atual do agente no ambiente.
        """
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)  # Exibe o elemento na posição correspondente
        vista.marcar_posicao(self.__estado.posicao)  # Marca a posição atual do agente na vista
