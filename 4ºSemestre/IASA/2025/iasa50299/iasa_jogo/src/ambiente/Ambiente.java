package ambiente;

/**
 * Interface que define o ambiente de jogo.
 * Um ambiente deve poder evoluir ao longo do tempo, permitir
 * a observação de eventos e executar comandos enviados pela personagem.
 * 
 * @author Tatiana Damaya
 */
public interface Ambiente {

    /**
     * Permite que o ambiente evolua ou mude ao longo do tempo.
     */
    public void evoluir();

    /**
     * Observa o ambiente para detetar e devolver o evento atual.
     *
     * @return o evento observado no ambiente
     */
    public Evento observar();

    /**
     * Executa um comando no ambiente.
     *
     * @param comando o comando a ser executado
     */
    public void executar(Comando comando);
}