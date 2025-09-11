from abc import ABC, abstractmethod

class ModeloPlan(ABC):
    """
    Define a interface para um modelo de planeamento, utilizado para gerir o estado e as ações no domínio de um problema.
    Esse modelo fornece os estados iniciais, os estados válidos e as operações possíveis para o planejamento.
    """

    @abstractmethod
    def obter_estado(self):
        """
        Obtém o estado atual do modelo.

        Este método deve ser implementado nas subclasses para fornecer o estado em que o agente se encontra no momento.
        """
        pass

    @abstractmethod
    def obter_estados(self):
        """
        Obtém todos os estados válidos no modelo.

        Nas subclasses, este método deve retornar todos os estados possíveis dentro do domínio do problema.
        """
        pass

    @abstractmethod
    def obter_operadores(self):
        """
        Obtém os operadores ou ações disponíveis no modelo.

        Deve ser implementado nas subclasses para fornecer todas as operações que podem ser realizadas nos estados do modelo.
        """
        pass
