"""
Controlo Reactivo
@author: Tatiana Damaya
"""

class ControloReact():
    """
    Controlo Reactivo de um Agente

    Esta classe representa o controlo reactivo de um agente, baseado em reações a percepções.
    Na arquitetura de um agente, o processamento interno que relaciona percepções com ações pode ser modularizado com base em um módulo de controlo. 
    No caso de um agente reativo, esse controlo será um controlo reativo, onde o processamento das percepções é realizado com base num módulo comportamental, também denominado comportamento.

    Attributes:
        __comportamento (Comportamento): O comportamento que guiará o processamento de percepções.
        mostrar_per_dir (bool): Uma flag para definir se as percepções direcionais serão mostradas.
    """

    def __init__(self, comportamento):
        """
        Inicializa o Controlo Reactivo com um comportamento específico.

        Args:
            comportamento (Comportamento): O comportamento que guiará o processamento de percepções.
        """
        self.__comportamento = comportamento

    def processar(self, percepcao):
        """
        Executa o processamento de percepções utilizando o comportamento definido.

        Args:
            percepcao (Percepcao): A percepção a ser processada pelo controlo reativo.

        Returns:
            Accao: A ação resultante após o processamento das percepções.
        """
        return self.__comportamento.activar(percepcao)