from lib.ecr.estimulo import Estimulo


class EstimuloObst(Estimulo):
    def __init__(self, direccao):
        super().__init__()
        self.direccao = direccao

    def detectar(self, percepcao):
        return 1.0 if percepcao.contacto_obst(self.direccao) else 0.0