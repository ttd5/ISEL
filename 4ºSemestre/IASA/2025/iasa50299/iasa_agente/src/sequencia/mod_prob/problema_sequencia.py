from lib.mod.problema import Problema
from mod_prob.estado_sequencia import EstadoSequencia
from mod_prob.operador_trocar import OperadorTrocar

class ProblemaSequencia(Problema):
    def __init__(self, seq_inicial, seq_final):
        estado_inicial = EstadoSequencia(seq_inicial)
        self.__estado_objetivo = EstadoSequencia(seq_final)

        operadores = []
        n = len(seq_inicial)
        for i in range(n):
            j = (i + 1) % n
            operadores.append(OperadorTrocar(i, j))

        super().__init__(estado_inicial, operadores)

    def objectivo(self, estado):
        return estado.id_valor() == self.__estado_objetivo.id_valor()
