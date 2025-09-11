"""
Controlo Deliberativo
@author: Tatiana Damaya
"""

from lib.sae.agente.controlo import Controlo
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo
from agente.controlo_delib.mec_delib import MecDelib

class ControloDelib(Controlo):
    """
    Controlador Deliberativo: Responsável por gerir o comportamento de um agente deliberativo.
    
    Numa arquitetura deliberativa, o comportamento é gerado com base em processos de planeamento suportados por representações internas do ambiente (modelo do mundo). 
    O planeador produz planos de ação com base nos objetivos gerados pelo mecanismo de deliberação. 

    No contexto de um planeador baseado em busca em espaços de estados, são considerados:
    - Modelo do problema de planejamento
    - Heurística a utilizar (se necessário)
    - Mecanismo de busca
    """
    def __init__(self, planeador):
        """
        Inicializa o controlador deliberativo.
        
        Args:
            planeador (Planeador): O planeador responsável por gerar planos de ação.
        """
        self.__planeador = planeador  # Planeador para gerar planos de ação
        self.__modelo_mundo = ModeloMundo()  # Modelo do mundo para representar o ambiente
        self.__mec_delib = MecDelib(self.__modelo_mundo)  # Mecanismo de deliberação
        self.__objectivos = None  # Conjunto de objetivos gerados
        self.__plano = None  # Plano de ação gerado

    def processar(self, percepcao):
        """
        Processa a percepção do ambiente e decide a ação a ser tomada.
        
        Args:
            percepcao (Percepcao): A percepção atual do ambiente.
        
        Returns:
            Accao: A ação a ser executada pelo agente.
        """
        self.__assimilar(percepcao)  # Atualiza o modelo do mundo com a percepção
        if self.__reconsiderar():
            self.__deliberar()  # Gera novos objetivos
            self.__planear()  # Gera um novo plano de ação
        self.__mostrar()  # Mostra a representação visual do ambiente e do plano
        return self.__executar()  # Executa o plano de ação e retorna a ação

    def __assimilar(self, percepcao):
        """
        Atualiza o modelo do mundo com base na percepção.
        
        Args:
            percepcao (Percepcao): A percepção atual do ambiente.
        """
        self.__modelo_mundo.actualizar(percepcao)

    def __reconsiderar(self):
        """
        Decide se é necessário reconsiderar o plano atual.
        
        Returns:
            bool: True se o plano deve ser reconsiderado, False caso contrário.
        """
        return self.__modelo_mundo.alterado or not self.__plano

    def __deliberar(self):
        """
        Gera um conjunto de objetivos com base na deliberação.
        """
        self.__objectivos = self.__mec_delib.deliberar()

    def __planear(self):
        """
        Gera um novo plano de ação com base nos objetivos.
        """
        if self.__objectivos:
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)
        else:
            self.__plano = None

    def __executar(self):
        """
        Executa o plano de ação gerado.
        
        Returns:
            Accao: A ação a ser executada pelo agente.
        """
        if self.__plano:
            operador = self.__plano.obter_accao(self.__modelo_mundo.obter_estado())
            if operador:
                return operador.accao

    def __mostrar(self):
        """
        Mostra a representação visual do ambiente e do plano.
        """
        self.vista.limpar()
        self.__modelo_mundo.mostrar(self.vista)
        if self.__plano:
            self.__plano.mostrar(self.vista)
        if self.__objectivos:
            for objectivo in self.__objectivos:
                self.vista.marcar_posicao(objectivo)