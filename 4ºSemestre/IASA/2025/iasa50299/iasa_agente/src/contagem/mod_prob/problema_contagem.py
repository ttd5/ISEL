from contagem.mod_prob.estado_contagem import EstadoContagem
from contagem.mod_prob.operador_incremento import OperadorIncremento
from lib.mod.problema import Problema

class ProblemaContagem(Problema):
    def __init__(self, inicio, meta, passos):
        operadores = [OperadorIncremento(p) for p in passos]
        super().__init__(EstadoContagem(inicio), operadores)
        self.__meta = meta

    def objectivo(self, estado):
        return estado.valor >= self.__meta