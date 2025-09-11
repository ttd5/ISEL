"""
Controlador MVC de simulação
@author: Luís Morgado
"""

#_____________________________________________________________

class ControladorSimul:
    """
    Controlador de simulação
    """
    def __init__(self, vista, modelo):
        """
        Iniciar controlador de simulação
        @param modelo: modelo de simulação
        """
        self.__vista = vista
        self.__modelo = modelo

    def comando_passo(self):
        """
        Processar passo de simulação
        """
        # Executar passo
        self.__modelo.executar_passo()
        # Actualizar visualização
        self.__vista.actualizar()


    def comando_reiniciar(self):
        """
        Reiniciar simulação
        """
        self.__modelo.iniciar()
        # Actualizar visualização
        self.__vista.actualizar()

        
