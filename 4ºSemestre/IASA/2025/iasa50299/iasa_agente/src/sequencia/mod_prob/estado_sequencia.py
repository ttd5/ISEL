from lib.mod.estado import Estado

class EstadoSequencia(Estado):
    def __init__(self, seq):
        self.__seq = tuple(seq)

    def id_valor(self):
        return self.__seq

    @property
    def seq(self):
        return self.__seq

    def __repr__(self):
        return str(self.__seq)

    def __hash__(self):
        return hash(self.__seq)

    def __eq__(self, other):
        if isinstance(other, EstadoSequencia):
            return self.__seq == other.__seq
        return False