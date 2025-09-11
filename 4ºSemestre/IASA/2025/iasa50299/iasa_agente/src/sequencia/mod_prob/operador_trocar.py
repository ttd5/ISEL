from mod_prob.estado_sequencia import EstadoSequencia
from lib.mod.operador import Operador

class OperadorTrocar(Operador):
    
    def __init__(self, pos1, pos2):
        self.__pos1 = pos1
        self.__pos2 = pos2

    def aplicar(self, estado):
        nova_seq = list(estado.seq)
        nova_seq[self.__pos1], nova_seq[self.__pos2] = nova_seq[self.__pos2], nova_seq[self.__pos1]
        return EstadoSequencia(nova_seq)

    def custo(self, estado, estado_suc):
        return abs(self.__pos1 - self.__pos2)

    def __repr__(self):
        return "Trocar(%d, %d)" % (self.__pos1, self.__pos2)