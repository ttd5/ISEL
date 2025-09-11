"""
Controlo Simulativo
@author: Tatiana Damaya
"""
from lib.sae.agente.controlo import Controlo

class ControloSimul(Controlo):
    """
    Controlo Simulado de um Agente

    Esta classe representa um controlo simulado de um agente, usado para testes.

    Methods:
        processar(percepcao): Simula o processamento de percepções, apenas imprime uma mensagem.

    Attributes:
        Nenhum.
    """
    def processar(self, percepcao):
        """
        Simula o processamento de percepções, apenas imprime uma mensagem.

        Args:
            percepcao: A percepção a ser processada pelo controle simulado.
        """
        print("Processar Controlo")  # Apenas imprime uma mensagem para simular o processamento