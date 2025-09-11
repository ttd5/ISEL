package agente;

import ambiente.Evento;

/**
 * Classe que representa uma perceção de um evento no ambiente.
 *
 * Esta perceção é utilizada pelo sistema de controlo do agente para
 * decidir qual a ação a executar, servindo como ponte entre o que
 * ocorre no ambiente e as decisões do agente.
 * 
 * @author Tatiana Damaya
 */
public class Percepcao {

    /** O evento observado no ambiente que constitui a perceção. */
    private Evento evento;
    
    /**
     * Construtor que cria uma nova perceção com base num evento observado.
     *
     * @param evento o evento que originou esta perceção
     */
    public Percepcao(Evento evento) {
        this.evento = evento;
    }

    /**
     * Obtém o evento associado a esta perceção.
     *
     * @return o evento que representa a perceção do ambiente
     */
    public Evento getEvento(){
        return evento;
    }
}
