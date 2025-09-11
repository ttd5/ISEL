from lib.pee.prof.procura_prof_lim import ProcuraProfLim

class ProcuraProfIter(ProcuraProfLim):
    """Procura em Profundidade Iterativa (Iterative Deepening Search).

    Esta classe implementa a procura em profundidade iterativa com limites de profundidade crescentes.
    Não é mantida memória de nós explorados entre as procuras, mantendo as características de complexidade da busca em profundidade.

    Processo de procura:
    - Para um limite de profundidade crescente:
        - Realizar uma procura em profundidade com o limite de profundidade atual.
        - Se existe solução, retornar a solução.
    """

    def procurar(self, problema, inc_prof=1, limite_prof=100):
        """Método para realizar a procura em profundidade iterativa.

        Args:
            problema: O problema a ser resolvido.
            inc_prof: O incremento do limite de profundidade a cada iteração.
            limite_prof: O limite de profundidade máximo.

        Returns:
            A solução encontrada ou None se não houver solução.
        """
        for i in range(0, limite_prof + 1, inc_prof):
            self.prof_max = i
            solucao = super().procurar(problema)
            if solucao:
                return solucao