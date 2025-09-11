from lib.pee.mec_proc.fronteira.fronteira import Fronteira

class FronteiraFIFO(Fronteira):
    """Uma fronteira FIFO (First-In, First-Out) para busca em largura.
    
    Esta fronteira mantém os nós numa fila, seguindo a ordem de inserção.
    O primeiro nó a ser inserido será o primeiro a ser retirado.
    """
    def inserir(self, no):
        """Insere um nó na fronteira."""
        self._nos.append(no)  # Adiciona o nó ao final da lista
