from ecr.comportamento import Comportamento
from abc import abstractmethod

class ComportComp(Comportamento):
    """
    Agrega conjuntos de comportamentos.
    A classe ComportComp representa um comportamento composto, que é uma combinação de vários comportamentos.
    
    Ela depende da interface Comportamento.

    A multiplicidade de relacionamento "1.." significa que uma instância de ComportComp pode conter uma ou mais instâncias de Comportamento.
    O atributo privado comportamentos é o nome do atributo que armazena esses objetos da classe Comportamento na classe ComportComp.
    """
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos # Atributo privado para armazenar os comportamentos

    def activar(self, percepcao):
        """Num comportamento composto, uma percepção pode potencialmente activar múltiplas reacções, as quais geram diferentes acções.
        
        :param percepcao: A percepção atual do agente.
        :return: A ação resultante do comportamento composto.
        """
        
        accoes = [] # Lista para armazenar as ações resultantes de cada comportamento individual.

        # Itera sobre cada comportamento na lista de comportamentos.
        for comportamento in self.__comportamentos:
            # Ativa o comportamento e obtém a ação resultante.
            accao = comportamento.activar(percepcao)
            # Verifica se a ação resultante não é None (ou seja, se foi gerada uma ação).
            if accao:
                # Adiciona a ação à lista de ações
                accoes.append(accao)
                
        # Verifica se há ações na lista.
        if accoes:
            # Seleciona e retorna a ação
            return self.seleccionar_accao(accoes)

    @abstractmethod
    def seleccionar_accao(self, accoes):
        """Mecanismo de selecção de acção para determinar a acção a realizar em função das respostas dos vários comportamentos internos.

        :param accoes: Lista de ações individuais geradas pelos comportamentos.
        :return: A ação final selecionada.
        """
        pass