package jogo.ambiente;

import ambiente.Comando;

/**
 * Enumeração que define os comandos disponíveis no jogo.
 * Estes comandos representam as ações que a personagem pode executar.
 * Cada comando pode ser mostrado de forma textual.
 * 
 * @author Tatiana Damaya
 */
public enum ComandoJogo implements Comando {

    /** Comando para procurar animais. */
    PROCURAR, 
    
    /** Comando para aproximar-se de um animal ou zona de ruído. */
    APROXIMAR, 
    
    /** Comando para observar o animal. */
    OBSERVAR, 
    
    /** Comando para fotografar o animal. */
    FOTOGRAFAR;

    /**
     * Mostra o comando atual de forma textual.
     */
    @Override
    public void mostrar() {
        System.out.printf("Ação: %s%n", this);
    }
}