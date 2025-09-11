from lib.pee.prof.procura_prof_lim import ProcuraProfLim


class ProcuraProfIter(ProcuraProfLim):
    """
    Implementa a busca em profundidade iterativa, onde o limite de profundidade é incrementado em cada iteração.
    """

    def procurar(self, problema, inc_prof=1, limite_prof=100):
        """
        Realiza a busca em profundidade iterativa.

        Para cada nível de profundidade, tenta encontrar uma solução dentro do limite especificado.
        A profundidade é incrementada a cada iteração até que a solução seja encontrada ou o limite de profundidade seja atingido.
        """
        for profundidade in range(0, limite_prof, inc_prof):
            self._prof_max = profundidade  # Define o novo limite de profundidade
            solucao = super().procurar(problema)  # Chama a busca no mecanismo de profundidade
            if solucao:
                return solucao  # Retorna a solução se encontrada
