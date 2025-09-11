"""
Área de desenho gráfico
@author: Luís Morgado
"""

import tkinter as tk

#___________________________________________________________

# Definição de cores
BRANCO = "white"
PRETO = "black"
AMARELO = "#FFFF00"
VERMELHO = "#FF0000"
VERDE = "#00FF00"
AZUL = "#0000FF"
CINZENTO = "#969696"
LARANJA = "#FFDC00"

CONFIG_SETA = (5, 5, 2)
"""Configuração base de uma seta"""

#___________________________________________________________

class AreaGrafica:
    """
    Representa e abstrai uma área de desenho
    """

    def __init__(self, janela, dim_x, dim_y, cor_fundo):
        """Iniciar superfície de desenho"""
        self._canvas = tk.Canvas(janela, width=dim_x, height=dim_y, bg=cor_fundo)
        self._canvas.pack()

    def limpar(self):
        """Limpar superfície de desenho"""
        self._canvas.delete("all")

    def linha(self, pos_ini, pos_fin, cor, linha=1):
        """Desenhar uma linha"""
        self._canvas.create_line((pos_ini, pos_fin), fill=cor, width=linha)

    def rect(self, pos_ini, pos_fin, cor, linha=0, preencher=True):
        """Desenhar um rectângulo"""
        self._canvas.create_rectangle((pos_ini, pos_fin), 
                                      fill=cor if preencher else "", 
                                      outline=cor if linha > 0 else "", 
                                      width=linha)

    def circulo(self, pos_ini, pos_fin, cor, linha=0):
        """Desenhar um círculo"""
        self._canvas.create_oval((pos_ini, pos_fin), 
                                 fill=cor, 
                                 outline=cor if linha > 0 else "", 
                                 width=linha)

    def vector(self, pos_ini, pos_fin, cor=AMARELO, linha=1, seta=True, forma=CONFIG_SETA):
        """Desenhar um vector"""
        arrow = "last" if seta else None
        self._canvas.create_line((pos_ini, pos_fin), 
                                 fill=cor, 
                                 width=linha, 
                                 arrow=arrow, 
                                 arrowshape=forma)
