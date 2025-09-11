from sae.agente.accao import Accao

class Resposta(Accao):
    """
    Define uma resposta a estímulos, em termos de acção a realizar e da respectiva prioridade.

    ASSOCIAÇÕES ESTÍMULO - RESPOSTA
    • Acções são directamente activadas em função das percepções
    • Não são utilizadas representações internas do mundo
    • Respostas rápidas a alterações no ambiente
    • Respostas fixas e predefinidas aos estímulos do ambiente

    Percepção é um tipo que define os vários estímulos de uma percepção e Resposta é um tipo que define as várias acções que podem ser realizadas.
    """
    def __init__(self, accao):
        """
        Inicializa a resposta com a ação associada.

        :param accao: A ação a ser associada à resposta.
        """
        self._accao = accao # Atributo protegido

    def activar(self, percepcao, intensidade = 0.0):
        """
        Ativa a resposta (execução da acção) se a percepção for verdadeira, definindo a prioridade da ação.

        :param percepcao: A percepção atual.
        :param intensidade: A intensidade da percepção, se aplicável.
        :return: A ação associada, se a percepção for verdadeira ou None caso contrário.
        """
        if percepcao:
            """ Define a prioridade da ação com base na intensidade do estímulo percepcionado"""
            self._accao.prioridade = intensidade
            return self._accao
        else:
            # Retorna None se a percepção for falsa
            return None