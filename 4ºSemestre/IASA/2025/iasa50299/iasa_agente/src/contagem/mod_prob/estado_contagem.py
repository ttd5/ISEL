class EstadoContagem:
    def __init__(self, valor):
        self.valor = valor

    def __eq__(self, other):
        return isinstance(other, EstadoContagem) and self.valor == other.valor

    def __hash__(self):
        return hash(self.valor)

    def __repr__(self):
        return f"<Estado: valor atual = {self.valor}>"