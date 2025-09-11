from lib.ecr.estimulo import Estimulo

class EstimuloObst(Estimulo):
    """
    Estímulo de Detecção de Obstáculo

    Este estímulo é responsável por detectar a presença de um obstáculo numa direção específica na percepção do agente e gerar um valor de estímulo com base na intensidade fornecida.
    """
    
    def __init__(self, direccao, intensidade = 1.0):
        """
        Inicializa o estímulo de detecção de obstáculo.

        Args:
            direccao (Direccao): A direção na qual o agente deve procurar um obstáculo.
            intensidade (float): A intensidade do estímulo gerado quando um obstáculo é detectado.
        """
        # Direção na qual o agente deve procurar um obstáculo
        self.__direccao = direccao  
        # Intensidade do estímulo gerado quando um obstáculo é detectado
        self.__intensidade = intensidade
        
    def detectar(self, percepcao):
        """
        Detecta a presença de um obstáculo na direção especificada na percepção do agente.

        Args:
            percepcao (Percepcao): A percepção atual do ambiente pelo agente.

        Returns:
            float: O valor do estímulo com base na presença de um obstáculo e na intensidade fornecida.
        """
        # Verifica se há um obstáculo na direção especificada
        if percepcao.contacto_obst(self.__direccao):
            # Se houver obstáculo, retorna a intensidade do estímulo
            return self.__intensidade
        # Se não houver obstáculo, retorna 0
        return 0