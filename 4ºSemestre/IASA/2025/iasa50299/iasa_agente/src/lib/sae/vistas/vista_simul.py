"""
Vista de simulação
@author: Luís Morgado
"""

from ..ambiente.elemento import Elemento
from ..versao import VERSAO, REVISAO
from .visualizador import BRANCO, PRETO
from .vista_amb import VistaAmb

#_____________________________________________________________

# Configuração de visualização
LARGURA = 600
"""Largura do ambiente em pixeis"""
DY_CONTROLO = 45
"""Distância vertical antes dos controlos"""
POS_X = 10
"""Posição horizontal da janela"""
POS_Y = 10
"""Posição vertical da janela"""
TITULO_BASE = "SAE"
"""Título base da vista de simulação"""
TITULO_VISTA_MODELO = "Modelo interno do agente"
"""Título da vista do modelo interno do agente"""

#_____________________________________________________________

class VistaSimul:
    def __init__(self, aplicacao, modelo, vista_modelo=False):
        """
        Iniciar vista
        @param aplicacao: aplicação base da vista
        @param modelo: modelo de simulação
        @param vista_modelo: mostrar vista do modelo interno do agente
        """
        self._aplicacao = aplicacao
        self._modelo = modelo
        # Escala de visualização (dimensão em pixeis de cada posição)
        self._escala = round(LARGURA / self._modelo.ambiente.dim_x)
        # Dimensões de visualização
        self._dim_vis_x = modelo.ambiente.dim_x * self._escala
        self._dim_vis_y = modelo.ambiente.dim_y * self._escala
        # Iniciar janela da simulação
        aplicacao.iniciar_janela(POS_X, POS_Y, 
                                 self._dim_vis_x, 
                                 self._dim_vis_y + DY_CONTROLO, 
                                 TITULO_BASE + f" {VERSAO}.{REVISAO}")
        # Iniciar vista de ambiente
        self._vista_amb = VistaAmb(aplicacao.janela, 
                                   self._dim_vis_x, 
                                   self._dim_vis_y, 
                                   self._escala, 
                                   BRANCO)
        # Iniciar vista do modelo interno do agente
        self._vista_modelo = self.__criar_vista_modelo() if vista_modelo else None
        # Iniciar controlos da aplicação
        aplicacao.iniciar_controlos()
        # Actualizar vista
        self.actualizar()

    @property
    def vista_modelo(self):
        return self._vista_modelo
  
    def __criar_vista_modelo(self):
        """Criar nova vista do ambiente vazia"""
        dim_x = self._dim_vis_x 
        dim_y = self._dim_vis_y
        x = POS_X + dim_x
        y = POS_Y
        nova_janela = self._aplicacao.criar_janela(x, y, dim_x, dim_y, TITULO_VISTA_MODELO)
        return VistaAmb(nova_janela, dim_x, dim_y, self._escala, PRETO)
        
    def actualizar(self):
        """
        Actualizar visualização
        """
        self._vista_amb.limpar()
        # Mostrar ambiente
        ambiente = self._modelo.ambiente
        # Mostrar elementos do ambiente
        for posicao, elemento in ambiente.elementos.items():
            if elemento != Elemento.VAZIO:
                self._vista_amb.mostrar_elemento(posicao, elemento)
        # Mostrar agente        
        self._vista_amb.agente(ambiente.posicao_agente,
                               ambiente.direccao_agente.value,
                               ambiente.colisao,
                               ambiente.recolha)
