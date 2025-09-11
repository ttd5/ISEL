from abc import ABC, abstractmethod

class Planeador(ABC):
    """
    Define a interface para um planeador que gera planos de ação em algoritmos de busca.
    O planeador é responsável por criar um conjunto de ações que permitem alcançar os objetivos definidos
    a partir de um modelo de planejamento.
    """

    @abstractmethod
    def planear(self, modelo_plan, objectivos):
        """
        Cria um plano de ação para atingir os objetivos com base no modelo de planejamento fornecido.

        O modelo de planejamento define os estados e as ações possíveis, enquanto os objetivos
        especificam o que se deve alcançar. O método gera a sequência de ações necessárias para atingir os objetivos.

        Cada subclasse deve implementar a lógica para gerar o plano, considerando o modelo e os objetivos fornecidos.
        """
        pass
