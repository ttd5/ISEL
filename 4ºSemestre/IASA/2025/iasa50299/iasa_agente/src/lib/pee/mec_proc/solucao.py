from pee.mec_proc.passo_solucao import PassoSolucao

class Solucao:

    def __init__(self, no_final):
        self.__no_final = no_final  # Armazena o nó final da solução
        self.__passos = []  # Inicializa a lista de passos
        no = self.__no_final

        # Traça o caminho de volta do nó final para o nó inicial, construindo a solução
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)  # Cria um passo com o estado do antecessor e a ação realizada
            self.__passos.insert(0, passo)  # Insere o passo no início da lista
            no = no.antecessor  # Move para o antecessor do nó atual

    @property
    def dimensao(self):
        # Retorna a profundidade do nó final, que indica a quantidade de passos até o objetivo
        return self.__no_final.profundidade

    @property
    def custo(self):
        # Retorna o custo total para atingir o nó final
        return self.__no_final.custo

    def __iter__(self):
        # Retorna um iterador para iterar pelos passos da solução
        return iter(self.__passos)

    def __getitem__(self, index):
        # Permite acessar os passos da solução por índice
        return self.__passos[index]
