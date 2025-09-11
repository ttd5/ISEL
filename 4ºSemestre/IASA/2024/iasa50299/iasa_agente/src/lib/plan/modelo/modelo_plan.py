from abc import ABC, abstractmethod

class ModeloPlan(ABC):
    """Interface para um modelo de planeamento.

    O processo de planeamento requer um modelo de planeamento que define:

    Estado - Estado inicial do problema (Define a situação inicial)
    Estados - Conjunto de estados válidos (necessário para processos de decisão de Markov), 
              serve para validar os estados
    Operadores - Conjunto de operadores (ações possíveis em cada estado) que definem transições 
                 de um estado para o outro e seus custos
    """

    @abstractmethod
    def obter_estado(self):
        """Retorna o estado inicial do problema."""
        pass

    @abstractmethod
    def obter_estados(self):
        """Retorna o conjunto de estados válidos."""
        pass

    @abstractmethod
    def obter_operadores(self):
        """Retorna o conjunto de operadores (ações possíveis em cada estado) que definem transições de um estado para o outro e os seus custos."""
        pass