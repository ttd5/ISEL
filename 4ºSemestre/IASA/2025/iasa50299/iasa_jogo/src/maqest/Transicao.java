package maqest;

import agente.Accao;

/**
 * Classe que representa uma transição entre estados na máquina de estados.
 * Cada transição define o estado sucessor e a ação a executar durante
 * essa transição.
 * 
 * @author Tatiana Damaya
 */
public class Transicao {

    /** O estado sucessor para onde ocorre a transição. */
    private Estado estadoSucessor;

    /** A ação a executar durante a transição. */
    private Accao accao;

    /**
     * Construtor que cria uma transição com um estado sucessor e uma ação.
     *
     * @param estadoSucessor o estado para o qual transitar
     * @param accao a ação a executar durante a transição
     */
    public Transicao(Estado estadoSucessor, Accao accao) {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }

    /**
     * Obtém o estado sucessor da transição.
     *
     * @return o estado para o qual esta transição leva
     */
    public Estado getEstadoSucessor() {
        return estadoSucessor;
    }

    /**
     * Obtém a ação associada a esta transição.
     *
     * @return a ação a executar durante a transição
     */
    public Accao getAccao() {
        return accao;
    }
}