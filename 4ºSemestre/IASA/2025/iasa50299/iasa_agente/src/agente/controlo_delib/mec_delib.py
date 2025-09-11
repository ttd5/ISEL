from lib.sae import Elemento

class MecDelib():
    """
    Define o mecanismo de deliberação de um agente, responsável por avaliar o ambiente e decidir quais objetivos o agente deve perseguir.
    """

    def __init__(self, modelo_mundo):
        """
        Cria uma nova instância do mecanismo de deliberação.

        O modelo do mundo é utilizado para representar o ambiente atual e os estados que o agente observa.
        """
        self.__modelo_mundo = modelo_mundo  # Armazena o modelo do mundo do agente

    def deliberar(self):
        """
        Realiza a deliberação e decide quais objetivos o agente deve perseguir.

        O agente gera uma lista de objetivos possíveis e seleciona os mais relevantes, com base no estado atual do mundo.
        """
        objectivos = self.gerar_objectivos()  # Gera uma lista de possíveis objetivos
        if objectivos:
            return self.seleccionar_objectivos(objectivos)  # Seleciona os objetivos mais importantes

    def gerar_objectivos(self):
        """        
        Cria uma lista de objetivos potenciais com base no modelo do mundo.

        O método percorre os estados conhecidos no modelo e seleciona aqueles que contêm o elemento ALVO.
        """
        return [estado for estado in self.__modelo_mundo.obter_estados() if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]

    def seleccionar_objectivos(self, objectivos):
        """
        Organiza os objetivos com base na proximidade ao agente.

        A lista é ordenada pela distância dos objetivos em relação ao agente, priorizando os mais próximos para que o agente os alcance primeiro.
        """
        objectivos.sort(key=self.__modelo_mundo.distancia)  # Ordena os objetivos pela distância ao agente
        return objectivos  # Retorna a lista de objetivos ordenada
