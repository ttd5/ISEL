from lib.ecr.estimulo import Estimulo
from lib.sae.ambiente.elemento import Elemento

class EstimuloAlvo(Estimulo):
    """
    Estímulo de Detecção de Alvo

    Este estímulo é responsável por detectar a presença de um alvo numa direção específica na percepção do agente e gerar um valor de estímulo 
    com base na proximidade do alvo e no fator de desconto gama.
    """
    def __init__(self, direccao, gama=0.9):
        """
        Inicializa o estímulo de detecção de alvo.

        Args:
            direccao (Direccao): A direção na qual o agente deve procurar um alvo.
            gama (float): O fator de desconto gama para calcular o valor do estímulo.
        """
        self.__direccao = direccao  # Direção na qual o agente deve procurar um alvo
        self.__gama = gama  # Fator de desconto gama para calcular o valor do estímulo
        
    def detectar(self, percepcao):
        """
        Detecta a presença de um alvo na direção especificada na percepção do agente.

        Args:
            percepcao (Percepcao): A percepção atual do ambiente pelo agente.

        Returns:
            float: O valor do estímulo com base na proximidade do alvo e no fator de desconto gama.
        """
        # Verifica se o elemento na direção especificada é um alvo
        if percepcao.per_dir[self.__direccao][0] == Elemento.ALVO:
            # Se for um alvo, calcula e retorna o valor do estímulo baseado no gama
            return self.__gama ** percepcao.per_dir[self.__direccao][1]
        else:
            # Se não for um alvo, retorna 0
            return 0