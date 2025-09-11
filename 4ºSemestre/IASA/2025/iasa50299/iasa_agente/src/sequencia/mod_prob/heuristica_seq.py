class HeuristicaSequencia:
    def __init__(self, seq_final):
        self.seq_final = seq_final

    def h(self, estado):
        return self._num_elem_dif(estado, self.seq_final)

    def _num_elem_dif(self, lista1, lista2):
        return sum(1 for a, b in zip(lista1, lista2) if a != b)
    