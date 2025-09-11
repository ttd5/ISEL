package agente;

import ambiente.Comando;

/**
 * Representa uma ação que um agente pode realizar no ambiente.
 */
public class Accao {

    Comando comando;

    /**
     * Construtor da classe Accao.
     * 
     * @param comando (O comando associado à ação).
     */
    public Accao(Comando comando) {
        this.comando = comando;
    }
}