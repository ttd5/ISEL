package agente;

/**
 * Interface que define o comportamento de um sistema de controlo para um agente.
 *
 * Um sistema de controlo processa perceções vindas do ambiente e devolve
 * uma ação que deve ser executada pelo agente.
 *
 * 
 * @author Tatiana Damaya
 */
public interface Controlo {

    /**
     * Processa uma perceção e determina a ação a executar.
     *
     * @param percepcao a perceção observada no ambiente
     * @return a ação a executar com base nessa perceção
     */
    Accao processar(Percepcao percepcao);
}
