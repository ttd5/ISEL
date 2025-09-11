from lib.pee.mec_proc.fronteira.fronteira import Fronteira

class FronteiraLIFO(Fronteira):
    """Uma fronteira LIFO (Last-In, First-Out) para busca em profundidade.
    
    Esta fronteira mantém os nós numa pilha, seguindo a ordem de inserção reversa.
    O último nó a ser inserido será o primeiro a ser retirado.
    """
    def inserir(self, no):
        """Insere um nó na fronteira."""
        self._nos.insert(0, no)  # Adiciona o nó no início da lista
