"""
Simulador de ambiente com visualização gráfica
@author: Luís Morgado
"""

from .defamb import DEF_AMB
from .erro import Erro, erro_terminar
from .ambiente.ambiente import Ambiente
from .vistas.vista_simul import VistaSimul
from .modelo.modelo_simul import ModeloSimul
from .controlador.controlador_simul import ControladorSimul
from .plataforma.aplicacao import Aplicacao

#_____________________________________________________________

# Configuração por omissão
TEMPO_PASSO = 100 # ms
"""Tempo do passo de execução"""
TEMPO_VMAX = 10 # ms
"""Tempo do passo de execução com velocidade máxima"""

#_____________________________________________________________

class Simulador:
    def __init__(self, num_amb, agente, reiniciar=False, vista_modelo=False):
        """
        Iniciar simulador
        @param num_amb: número do ambiente
        @param agente: agente a executar
        @param reiniciar: reiniciar automático da simulação com recolha de alvo
        @param vista_modelo: mostrar vista do modelo interno do agente
        """
        # Iniciar ambiente
        self.__ambiente = self.__iniciar_ambiente(num_amb)
        # Iniciar aplicação
        self.__aplicacao = Aplicacao()
        # Iniciar modelo de simulação
        self.__modelo = ModeloSimul(self.__ambiente, agente, reiniciar)
        # Iniciar vista de simulação
        self.__vista = VistaSimul(self.__aplicacao, self.__modelo, vista_modelo)
        # Iniciar controlador de simulação
        self.__controlador = ControladorSimul(self.__vista, self.__modelo)
        # Iniciar transdutor do agente
        if agente is not None:
            agente.vista = self.__vista.vista_modelo
            agente.transdutor.iniciar(self.__ambiente)

    def __iniciar_ambiente(self, num_amb):
        """
        Obter definição de ambiente
        @param num_amb: número do ambiente
        @return: ambiente
        """
        if num_amb in DEF_AMB:
            return Ambiente(DEF_AMB[num_amb])
        else:
            erro_terminar(Erro.AMB_NAO_DEF, num_amb)

    def executar(self):
        """
        Executar simulação
        """
        # Iniciar aplicação com controlador de execução da simulação
        self.__aplicacao.iniciar(self.__controlador, TEMPO_PASSO, TEMPO_VMAX)


        
