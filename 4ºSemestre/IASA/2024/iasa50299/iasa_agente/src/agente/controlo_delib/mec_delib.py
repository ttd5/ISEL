from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo
from lib.sae.ambiente.elemento import Elemento

class MecDelib(ModeloMundo):
    """
    Mecanismo de Deliberação: Responsável por gerar objetivos para o agente.

    Numa arquitetura de agente autônomo, o planeador produz planos de ação com base nos objetivos gerados pelo mecanismo de deliberação. 
    Esta classe estende o ModeloMundo para aceder aos estados e elementos do ambiente e determinar quais são os objetivos do agente.
    """
    
    def __init__(self, modelo_mundo):
        """
        Inicializa o mecanismo de deliberação.
        
        Args:
            modelo_mundo (ModeloMundo): A referência ao modelo do mundo.
        """
        self.__modelo_mundo = modelo_mundo  # Referência ao modelo do mundo

    def deliberar(self):
        """
        Gera um conjunto de objetivos com base no modelo do mundo.
        
        Numa arquitetura de agente autônomo, o planeador produz planos de ação com base nos objetivos gerados pelo mecanismo de deliberação. 
        Este método retorna uma lista de estados que são considerados objetivos, ordenados pela distância ao estado atual do agente.
        
        Returns:
            list[EstadoAgente]: Lista de estados objetivo ordenados pela distância ao estado atual.
        """
        # Seleciona estados que têm um elemento ALVO
        objetivos = [estado for estado in self.__modelo_mundo.obter_estados() if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]

        if objetivos:
            # Ordena os estados objetivo pela distância ao estado atual do agente
            objetivos.sort(key=self.__modelo_mundo.distancia)
            return objetivos
