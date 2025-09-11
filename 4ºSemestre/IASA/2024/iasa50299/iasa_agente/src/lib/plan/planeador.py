from abc import ABC, abstractmethod

class Planeador(ABC):
    """Interface para os planeadores."""

    @abstractmethod
    def planear(self, modelo_plan, objetivos):
        """
        Realiza o planeamento para alcançar os objetivos no modelo de plano especificado.

        Args:
            modelo_plan (ModeloPlan): O modelo de plano que define o ambiente e as ações possíveis.
            objetivos (list): Uma lista de objetivos a serem alcançados.

        Returns:
            Plano: O plano resultante para alcançar os objetivos, ou None se nenhum plano for encontrado.
        """
        pass