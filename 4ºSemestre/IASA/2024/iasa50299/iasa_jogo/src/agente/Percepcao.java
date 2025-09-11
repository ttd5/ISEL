package agente;

import ambiente.Evento;

/**
 * Representa uma percepção de um agente sobre o seu ambiente.
 */
public class Percepcao {

    private final Evento evento;

    /**
     * Construtor da classe Percepcao.
     * 
     * @param evento (O evento percebido pelo agente).
     */
    public Percepcao(Evento evento) {
        this.evento = evento;
    }

    /**
     * Retorna o evento associado à percepção.
     * 
     * @return evento (O evento percebido).
     */
    public Evento getEvento() {
        return evento;
    }
}
