from ecr.comport_comp import ComportComp

class Hierarquia(ComportComp):
    """
    A classe Hierarquia representa um comportamento composto com uma hierarquia de comportamentos.
    Herda de ComportComp (Relação Generalização - Relação estrutural que indica que uma parte é uma especialização de outra parte mais geral)
    
    """
    def seleccionar_accao(self, accoes):
        """
        Seleciona a ação mais prioritária de uma lista de ações.
        
        :param accoes: Lista de ações possíveis, ordenadas por prioridade.
        :return: A ação de maior prioridade, ou None se a lista estiver vazia.
        """
        if not accoes:  # Verifica se a lista está vazia
            return None
        return accoes[0]