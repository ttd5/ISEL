from abc import ABC, abstractmethod

class ModeloPDM(ABC):
    """
    Classe abstrata que define a estrutura básica de um modelo de processo de decisão de Markov (PDM).

    Métodos Abstratos:
        S: Retorna o conjunto de estados do mundo.
        A: Retorna o conjunto de ações possíveis em um determinado estado.
        T: Retorna a probabilidade de transição de um estado para outro através de uma ação.
        R: Retorna o retorno esperado ao realizar uma transição de um estado para outro através de uma ação.
        suc: Retorna o próximo estado dado um estado e uma ação.

    """

    @abstractmethod
    def S(self):
        """Retorna o conjunto de estados do mundo."""
        pass

    @abstractmethod
    def A(self, s):
        """Retorna o conjunto de ações possíveis no estado s."""
        pass

    @abstractmethod
    def T(self, s, a, sn):
        """Retorna a probabilidade de transição de s para s' através de a."""
        pass

    @abstractmethod
    def R(self, s, a, sn):
        """Retorna o retorno esperado na transição de s para s' através de a."""
        pass

    @abstractmethod
    def suc(self, s, a):
        """Retorna o próximo estado dado um estado e uma ação."""
        pass