from abc import ABC, abstractmethod

class Plano(ABC):
    """
    Define a interface para um plano de ações no contexto de um agente autônomo.
    Essa classe serve como base para a criação de diferentes tipos de planos gerados por mecanismos de planejamento variados.
    """

    @abstractmethod
    def obter_accao(self, estado):
        """
        Obtém a ação a ser executada a partir de um estado específico.

        Este método deve ser implementado nas subclasses para definir qual ação deve ser tomada em determinado estado.
        A lógica para selecionar a ação será definida conforme o tipo de plano e o objetivo do agente.
        """
        pass

    @abstractmethod
    def mostrar(self, vista):
        """
        Exibe a sequência de ações do plano na interface gráfica.

        O método será implementado nas subclasses para exibir o conteúdo do plano de acordo com a visualização desejada.
        A forma como os dados são apresentados dependerá da implementação concreta e do tipo de vista fornecida.
        """
        pass
