package ambiente;

/**
 * Interface que representa um comando que pode ser executado no ambiente.
 * Os comandos são as ações que a personagem executa durante o jogo.
 * 
 * @author Tatiana Damaya
 */
public interface Comando {

    /**
     * Mostra o comando atual de forma textual.
     */
    public void mostrar();
}