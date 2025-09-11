from abc import ABC, abstractmethod

class ModeloPDM(ABC):
    """
    Classe base para a definição de um modelo de Processos de Decisão Markovianos (PDM).
    Este modelo envolve estados, ações, transições, recompensas e sucessores para determinar as melhores decisões.
    """

    @abstractmethod
    def S(self):
        """
        Obtém todos os estados possíveis no modelo PDM.

        Esse método deve ser implementado nas subclasses para fornecer todos os estados que o agente pode alcançar no PDM.
        """
        pass

    @abstractmethod
    def A(self, s):
        """
        Obtém as ações disponíveis a partir de um estado específico.

        Nas subclasses, deve-se definir as ações que o agente pode realizar a partir de um determinado estado.
        """
        pass

    @abstractmethod
    def T(self, s, a):
        """
        Define a probabilidade de transição entre estados ao aplicar uma ação.

        As subclasses devem fornecer as probabilidades de transição para os estados sucessores resultantes da ação aplicada.
        """
        pass

    @abstractmethod
    def R(self, s, a, sn):
        """
        Calcula a recompensa ao transitar de um estado para outro devido a uma ação.

        Este método deve ser implementado nas subclasses para calcular a recompensa associada a cada transição.
        """
        pass

    @abstractmethod
    def suc(self, s, a):
        """
        Retorna os estados que podem ser alcançados após realizar uma ação a partir de um estado.

        As subclasses devem definir quais estados são possíveis após a aplicação de uma ação em um dado estado.
        """
        pass
