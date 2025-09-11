from agente.controlo_delib.mec_delib import MecDelib
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo

class ControloDelib:
    """
    Classe responsável por controlar as decisões deliberativas de um agente.
    Ela gerencia os objetivos do agente e utiliza um planeador para criar planos de ação com base nos objetivos e percepções do ambiente.
    """

    def __init__(self, planeador):
        """
        Inicializa o controle deliberativo do agente.

        O planeador é utilizado para criar planos de ação conforme os objetivos e o estado do mundo.
        """
        self.__objectivos = []  # Mantém os objetivos do agente
        self.__planeador = planeador  # Utiliza o planeador para criar planos de ação
        self.__vista = None  # A vista que permite a representação gráfica do ambiente
        self.__modelo_mundo = ModeloMundo()  # O modelo que representa o ambiente do agente
        self.__mec_delib = MecDelib(self.__modelo_mundo)  # Mecanismo que delibera os objetivos
        self.__plano = None  # Plano de ação gerado pelo planeador

    @property
    def vista(self):
        return self.__vista

    @vista.setter
    def vista(self, nova_vista):
        self.__vista = nova_vista

    def processar(self, percepcao):
        """
        Processa uma nova percepção do ambiente e atualiza o estado interno do agente.

        A percepção é assimilada, e dependendo das mudanças, o agente reconsidera seus objetivos e gera um novo plano de ação.
        O agente então executa a ação planejada.
        """
        self.__assimilar(percepcao)  # Atualiza o modelo do mundo com a nova percepção
        if self.__reconsiderar():  # Avalia se os objetivos precisam ser revistos
            self.__deliberar()  # Delibera novos objetivos
            self.__planear()  # Gera um novo plano de ação
        self.__mostrar()  # Exibe graficamente o estado atual
        return self.__executar()  # Executa a próxima ação com base no plano

    def __planear(self):
        """
        Planeja uma nova ação com base nos objetivos e no modelo do mundo.

        O planeador cria um plano de ação com base nos objetivos e no estado atual do ambiente.
        """
        if self.__objectivos:  # Se houver objetivos, o agente planeja a ação
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)
        else:
            self.__plano = None  # Se não houver objetivos, não há plano a ser gerado

    def __assimilar(self, percepcao):
        """
        Atualiza o modelo do mundo com a nova percepção do agente.

        Este método atualiza as informações internas do modelo do mundo com base nas percepções recebidas.
        """
        self.__modelo_mundo.actualizar(percepcao)

    def __reconsiderar(self):
        """
        Verifica se os objetivos ou plano de ação precisam ser revistos.

        A reconsideração ocorre se o modelo do mundo foi alterado ou se não há plano ativo.
        """
        return self.__modelo_mundo.alterado  # Retorna True se o modelo foi alterado ou não houver plano ativo

    def __deliberar(self):
        """
        Realiza a deliberação dos objetivos do agente.

        O agente usa o mecanismo de deliberação para obter uma nova lista de objetivos com base no estado atual do ambiente.
        """
        self.__objectivos = self.__mec_delib.deliberar()  # Obtém a lista de objetivos do mecanismo de deliberação

    def __executar(self):
        """
        Executa a ação do plano de ação atual.

        O agente consulta o plano de ação e realiza a ação correspondente. Caso não haja ação disponível, o plano é descartado.
        """
        if self.__plano:
            operador = self.__plano.obter_accao(self.__modelo_mundo.obter_estado())
            if operador:
                return operador.accao  # Retorna a ação a ser executada
            else:
                self.__plano = None  # Se não houver ação, descarta o plano

    def __mostrar(self):
        """
        Exibe graficamente o estado do mundo, o plano de ação e os objetivos.

        A visualização é feita através da vista fornecida, onde o estado atual do mundo, o plano e os objetivos são mostrados.
        """
        if self.vista is None:
            return  # Se não houver vista configurada, não faz nada

        self.vista.limpar()  # Limpa a visualização do ambiente
        self.__modelo_mundo.mostrar(self.vista)  # Exibe o estado do mundo atual

        if self.__plano:
            self.__plano.mostrar(self.vista)  # Exibe o plano de ação

        if self.__objectivos:
            for objectivo in self.__objectivos:
                self.vista.marcar_posicao(objectivo.posicao)  # Marca os objetivos na visualização