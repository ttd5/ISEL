from lib.plan.plano import Plano

class PlanoPEE(Plano):
    """Representa um plano de ação para o paradigma PEE (Procura em Espaço de Estados)."""

    def __init__(self, solucao):
        """
        Inicializa o plano com uma solução.

        Args:
            solucao (Solucao): A solução obtida após a procura.
        """
        self.__solucao = solucao  # Armazena a solução

    def obter_accao(self, estado):
        """
        Obtém a próxima ação a ser executada no estado especificado.

        Args:
            estado (Estado): O estado atual.

        Returns:
            Operador: A próxima ação a ser executada.
        """
        if self.__solucao.dimensao > 1:
            estado_solucao = self.__solucao[0].estado  # Obtém o estado da próxima ação na solução
            if estado == estado_solucao:  # Se o estado atual corresponde ao próximo estado na solução
                self.__solucao.remover()  # Remove o próximo estado da solução
                no = self.__solucao[0]  # Obtém o próximo nó da solução
                return no.operador  # Retorna o operador correspondente ao próximo nó

    def mostrar(self, vista):
        """Mostra o plano na interface de visualização."""
        pass
