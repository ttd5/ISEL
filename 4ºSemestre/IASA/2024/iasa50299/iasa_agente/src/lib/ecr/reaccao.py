from ecr.comportamento import Comportamento

class Reaccao(Comportamento):
    """
    A classe Reaccao representa uma associação Estímulo - Resposta, ou seja, uma reação a um estímulo do ambiente.
    
    Ela depende da interface Comportamento, que define um método abstracto 'activar' e é uma parte na relação de agregação com Estímulo e Resposta, 
    ou seja, contém referências aos objetos Estimulo e Resposta,mas esses objetos podem existir independentemente da classe Reaccao.

    Uma arquitectura de agentes reactivos define um ciclo percepção-reacção-acção, onde as reacções definem de forma modular as associações 
    entre estímulos (derivados da percepção) e respostas (geradoras de acção).

    Estimulo - Define informação activadora de uma reacção.
    Resposta - Define uma resposta a estímulos, em termos de acção a realizar e da respectiva prioridade.
    Reacão - Módulo que associa estímulos a respostas.
    """

    def __init__(self, estimulo, resposta):
        """
        Inicializa a classe Reaccao com um estímulo e uma resposta associados.
        
        :param estimulo: Representa a detecção de um estímulo presente numa percepção.
        :param resposta: Representa a geração de uma resposta a um estímulo.
        """
        self.__estimulo = estimulo  # Atributo privado para armazenar o estímulo
        self.__resposta = resposta  # Atributo privado para armazenar a resposta

    def activar(self, percepcao):
        """
        Avalia a intensidade do estímulo com base na percepção atual e ativa a resposta associada, se necessário.
        
        :param percepcao: A percepção atual do ambiente.
        :return: A ação associada à resposta ao estímulo, ou None se nenhum estímulo for detectado.
        """
        # Detecta a intensidade do estímulo com base na percepção atual.
        intensidade = self.__estimulo.detectar(percepcao)
        
        # Verifica se a intensidade do estímulo é maior que zero.
        if intensidade > 0:
            # Ativa a resposta associada ao estímulo com a percepção e a intensidade do estímulo.
            accao = self.__resposta.activar(percepcao, intensidade)
            # Retorna a ação associada à resposta.
            return accao
        else:
            # Se nenhum estímulo for detectado, retorna None.
            return None