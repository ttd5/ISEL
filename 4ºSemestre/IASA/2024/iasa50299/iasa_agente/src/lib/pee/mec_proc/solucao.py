from typing import Iterator
from lib.pee.mec_proc.no import No 
"""
• Solução
– Representa um percurso correspondente a uma solução de um problema
• Sequência de nós que representa um percurso no espaço de estados
• Dimensão da solução (número de nós do percurso)
• Permite acesso indexado e iteração sobre o percurso
• Permite remover o primeiro nó do percurso
"""

class Solucao:
    def __init__(self, no_final):
        # Inicializa uma lista que armazenará o percurso da solução
        self.__percurso = []
        # Inicia a construção do percurso a partir do nó final, retrocedendo até o nó inicial
        no = no_final
        while no:
            self.__percurso.insert(0, no)  # Insere cada nó no início da lista para manter a ordem
            no = no.antecessor  # Retrocede para o nó antecessor

    @property
    def dimensao(self):
        # Retorna o número de nós no percurso, representando a dimensão da solução
        return len(self.__percurso)

    def remover(self):
        # Remove e retorna o primeiro nó do percurso, simbolizando a continuação da exploração
        if self.__percurso:
            return self.__percurso.pop(0)

    def __iter__(self):
        # Retorna um iterador para o percurso, permitindo iteração sobre os nós
        return iter(self.__percurso)

    def __getitem__(self, index):
        # Permite acesso indexado ao percurso, retornando o nó correspondente ao índice fornecido
        return self.__percurso[index]
