package agente;

/**
 * Interface para o componente de controle de um agente.
 * Define a lógica de processamento de percepções para ações.
 */
public interface Controlo {

    /**
     * Processa uma percepção e retorna uma ação correspondente.
     * 
     * @param percepcao (A percepção captada pelo agente).
     * @return A ação a ser realizada pelo agente.
     */
    public Accao processar(Percepcao percepcao);
}
