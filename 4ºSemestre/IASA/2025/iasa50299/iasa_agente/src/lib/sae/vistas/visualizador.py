"""
Visualizador de ambiente
@author: Luís Morgado
"""

import math

from ..plataforma.area_grafica import *

#___________________________________________________________
    
# Cores específicas de elementos
COR_AGENTE = LARANJA
COR_ALVO = VERDE
COR_BASE = VERDE
COR_OBST = CINZENTO
COR_COLIS = VERMELHO
COR_AGLINHA = PRETO

#___________________________________________________________

class Visualizador:
    def __init__(self, janela, dim_x, dim_y, escala, cor_fundo):
        """
        Iniciar visualizador
        @param janela: janela base
        @param dim_x: dimensão do eixo x
        @param dim_y: dimensão do eixo y
        @param escala: dimensão de cada elemento
        @param cor_fundo: cor de fundo
        """
        self._escala = escala
        self._forma_seta = (escala/4, escala/4, escala/9)
        self._cor_fundo = cor_fundo
        self._area = AreaGrafica(janela, dim_x, dim_y, cor_fundo)
        self.limpar()
        
    def limpar(self):
        """
        Limpar visualizador
        """
        self._area.limpar()
       
    def agente(self, pos, ang=None, col=False, carga=False):
        """
        Visualizar agente
        @param pos: posição do elemento
        @param ang: ângulo de orientação
        @param col: colisão True/False
        @param carga: carga True/False
        """
        r = round(0.4 * self._escala)
        margem = 0.1 * self._escala
        x, y = self.pvpix(pos)
        x0 = round(x + r + margem)
        y0 = round(y + r + margem)
        cor = COR_COLIS if col else COR_AGENTE
        xi, yi = x, y
        xf = xi + self._escala - 2
        yf = yi + self._escala - 2
        self._area.circulo((xi, yi), (xf, yf), cor)
        if ang is not None:
            dx = r * math.cos(ang)
            dy = -r * math.sin(ang)
            x1 = round(x0 + dx)
            y1 = round(y0 + dy)
            self._area.linha((x0, y0), (x1, y1), COR_AGLINHA)
        if carga:
            self.rect(pos, COR_ALVO, margem=int(0.3 * self._escala))
    
    def alvo(self, pos):
        """
        Visualizar alvo
        @param pos: posição do elemento
        """
        self.rect(pos, COR_ALVO, linha=0)
    
    def obstaculo(self, pos):
        """
        Visualizar obstáculo
        @param pos: posição do elemento
        """
        self.rect(pos, COR_OBST, linha=0)
    
    def vazio(self, pos):
        """
        Visualizar vazio
        @param pos: posição do elemento
        """
        self.rect(pos, self._cor_fundo)

    def linha(self, pos_ini, pos_fin, cor, linha=1):
        """
        Visualizar uma linha
        @param pos: posição do ambiente
        @param cor: cor RGB
        @param linha: espessura de linha (0 - preencher)
        @param margem: margem em pixeis
        """
        self._area.linha(pos_ini, pos_fin, cor, linha=1)

    def rect(self, pos, cor=AMARELO, linha=1, margem=0, preencher=True):
        """
        Visualizar rectângulo
        @param pos: posição do ambiente
        @param cor: cor RGB
        @param linha: espessura de linha (0 - preencher)
        @param margem: margem em pixeis
        """
        x, y = self.pvpix(pos)
        spx = margem
        spy = margem
        xi = x + spx - 1
        yi = y + spy - 1
        xf = xi + self._escala - spx*2
        yf = yi + self._escala - spy*2
        self._area.rect((xi, yi), (xf, yf), cor, linha, preencher)

    def vector(self, pos, mod, ang, cor=AMARELO, linha=1, seta=True):
        """
        Visualizar vector
        @param pos: posição do elemento
        @param mod: módulo (dimensão do vector)
        @param ang: ângulo de orientação
        @param cor: cor RGB
        @param linha: espessura de linha
        @param seta: seta no final True/False
        """
        x, y = self.pvpix(pos)
        xi = x + self._escala / 2.0
        yi = y + self._escala / 2.0
        PROP_VECT = 0.5 # Proporção do vector em relação à escala
        dim = PROP_VECT * mod * self._escala
        dx, dy = self.inc_pos(dim, ang)
        xf = xi + dx
        yf = yi + dy
        self._area.vector((xi,yi), (xf,yf), cor, linha, seta, forma=self._forma_seta) 

    def marcar(self, posicoes, margem=2, cor=AMARELO, linha=0):
        """
        Marcar posições
        @param posicoes: conjunto de posições
        @param margem: margem em pixeis
        @param cor: cor RGB
        @param linha: espessura de linha (0 - preencher)
        """
        for pos in posicoes:
            self.rect(pos, cor, linha, margem, preencher=(linha == 0))              
    
    def pvpix(self, pos_virt):
        """
        Converter posição virtual em pixeis
        @param pos_virt: posição virtual
        @return: posição (x, y) em pixeis
        """
        xv, yv = pos_virt
        x = round(xv * self._escala)
        y = round(yv * self._escala)
        return x, y

    def inc_pos(self, mod, ang):   
        """
        Gerar incremento de posição (dx,dy)
        @param mod: módulo da distância de movimentação
        @param ang: ângulo de movimentação
        @return: incremento de posição (dx, dy)
        """
        dx = mod * math.cos(ang)
        dy = -mod * math.sin(ang)
        return dx, dy
