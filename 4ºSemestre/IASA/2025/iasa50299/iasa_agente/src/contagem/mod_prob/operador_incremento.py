from contagem.mod_prob.estado_contagem import EstadoContagem
from lib.mod.operador import Operador

class OperadorIncremento(Operador):
    def __init__(self, incremento):
        self.__incremento = incremento

    def aplicar(self, estado):
        return EstadoContagem(estado.valor + self.__incremento)

    def custo(self, estado, estado_suc):
        return self.__incremento ** 2  

    @property
    def incremento(self):
        return self.__incremento