from lib.pee.mec_proc.mecanismo_procura import MecanismoProcura

class ProcuraGrafo(MecanismoProcura):
    """
    O processo de procura ocorre por exploração do espaço de estados a partir do estado inicial.
    O espaço de estados é representado como um grafo, onde cada vértice corresponde a um estado e cada arco corresponde a uma transição entre estados
    """
    def _iniciar_memoria(self):
        # Chama o método da superclasse para inicializar a memória padrão
        super()._iniciar_memoria()
        # Inicializa um dicionário para armazenar os nós explorados durante a busca
        self._explorados= {}

    def _memorizar(self,no):
        # Verifica se o nó deve ser mantido na busca
        if self._manter(no):
            # Adiciona o nó aos explorados e à fronteira se atender aos critérios
            self._explorados[no.estado] = no
            self._fronteira.inserir(no)
        
    def _manter(self,no):
        # Verifica se o estado associado ao nó já foi explorado
        return no.estado not in self._explorados
