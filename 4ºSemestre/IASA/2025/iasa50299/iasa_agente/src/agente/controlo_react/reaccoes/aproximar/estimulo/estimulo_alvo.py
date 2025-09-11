from lib.ecr.estimulo import Estimulo
from lib.sae.ambiente.elemento import Elemento

class EstimuloAlvo(Estimulo):
    def __init__(self, direccao, gama = 0.9):
        self.__direccao = direccao
        self.__gama = gama
    

        """
        Detecta a presença de um alvo na direção especificada na percepção do agente.

        Args:
            percepcao (Percepcao): A percepção atual do ambiente pelo agente.

        Returns:
            float: O valor do estímulo com base na proximidade do alvo e no fator de desconto gama.
        """
    def detectar(self, percepcao):
        elemento, distancia, _ = percepcao[self.__direccao]

        intensidade = self.__gama**distancia if elemento==Elemento.ALVO else 0
        return intensidade
