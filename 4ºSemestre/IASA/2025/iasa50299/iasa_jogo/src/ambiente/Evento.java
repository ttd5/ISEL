package ambiente;

/**
 * Interface que representa um evento ocorrido no ambiente.
 * Os eventos são percecionados pela personagem e desencadeiam ações.
 * 
 * @author Tatiana Damaya
 */
public interface Evento {

    /**
     * Mostra o evento atual de forma textual.
     */
    public void mostrar();
}