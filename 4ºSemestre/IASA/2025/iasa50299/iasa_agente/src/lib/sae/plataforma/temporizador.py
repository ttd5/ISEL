"""
Temporizador de execução
@author: Luís Morgado
"""

class Temporizador:
    def __init__(self, janela):
        """
        Criar temporizador
        @param janela: janela base do temporizador
        """
        self._janela = janela
        self._temporizador = None
        
    def iniciar(self, intervalo, receptor):
        """
        Iniciar temporização
        @param intervalo: período de temporização em milisegundos
        @param receptor: processador do evento de temporização (função)
        """
        self.terminar()
        self._temporizador = self._janela.after(intervalo, receptor)

    def terminar(self):
        """Terminar temporização"""
        if self._temporizador:
            self._janela.after_cancel(self._temporizador)
            self._temporizador = None
