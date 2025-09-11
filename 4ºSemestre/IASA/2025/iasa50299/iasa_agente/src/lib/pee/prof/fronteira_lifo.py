from lib.pee.mec_proc.fronteira import Fronteira


class FronteiraLIFO(Fronteira):
    """
    Implementa uma fronteira LIFO (Last In, First Out), onde o último nó inserido será o primeiro a ser removido.
    """
    
    def inserir(self, no):
        """
        Insere um nó na fronteira, colocando-o no início da lista.

        Esse comportamento segue a lógica LIFO, ou seja, o último nó adicionado será o primeiro a ser retirado.
        """
        self._nos.insert(0, no) 