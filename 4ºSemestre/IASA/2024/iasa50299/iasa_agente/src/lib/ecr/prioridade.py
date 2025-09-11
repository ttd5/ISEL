from ecr.comport_comp import ComportComp

class Prioridade(ComportComp):
    """
    A classe Prioridade representa um comportamento composto com prioridade entre comportamentos.
    Herda de ComportComp.
    As respostas são selecionadas de acordo com uma prioridade associada que varia ao longo da execução.

    PRIORIDADE DE AÇÕES:
        - As ações interferem entre si.
        - Não podem ser executadas em conjunto.
        - É associada informação de prioridade a cada ação.
        - A ação com maior prioridade é selecionada para execução.
    """
    def seleccionar_accao(self, accoes):
        """
        Seleciona a ação com a maior prioridade.
        
        :param accoes: Lista de ações possíveis.
        :return: A ação de maior prioridade ou None se a lista estiver vazia.
        """
        if not accoes:  # Verifica se a lista está vazia
            return None
        # Retorna a ação de maior prioridade.
        return max(accoes, key=lambda x: x.prioridade)  # Seleciona a ação com a maior prioridade na lista de ações disponíveis.