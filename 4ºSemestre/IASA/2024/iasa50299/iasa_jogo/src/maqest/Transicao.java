package maqest;

import agente.Accao;

/**
 * Representa uma transição dentro de uma máquina de estados, incluindo o estado sucessor e a ação a ser executada.
 */
public class Transicao {

    private Estado estadoSucessor;
    private Accao accao;

    /**
     * Constrói uma nova transição.
     *
     * @param estadoSucessor (O estado para o qual esta transição leva).
     * @param accao (A ação a ser executada durante a transição).
     */
    public Transicao(Estado estadoSucessor, Accao accao) {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }

    /**
     * Retorna o estado sucessor desta transição.
     *
     * @return O estado sucessor.
     */
    public Estado getEstadoSucessor() {
        return estadoSucessor;
    }

    /**
     * Retorna a ação associada a esta transição.
     *
     * @return A ação a ser executada.
     */
    public Accao getAccao() {
        return accao;
    }
}
