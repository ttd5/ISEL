package agente;

import ambiente.Ambiente;
import ambiente.Evento;

/**
 * Classe abstrata que define a estrutura básica de um agente.
 * Um agente percebe o seu ambiente, processa as percepções e atua sobre ele.
 */
public abstract class Agente {
    
    private final Ambiente ambiente;
    private final Controlo controlo;

    /**
     * Constrói um agente com um ambiente e um controlo especificados.
     * 
     * @param ambiente (O ambiente onde o agente atua).
     * @param controlo (O controlo que define a lógica de processamento do agente).
     */
    public Agente(Ambiente ambiente, Controlo controlo) {
        this.ambiente = ambiente;
        this.controlo = controlo;
    }

    /**
     * Executa passo de processamento do agente: percepcionar -> processar -> actuar.
     */
    public void executar() {
        Percepcao percepcao = percepcionar();
        Accao accao = controlo.processar(percepcao);
        actuar(accao);
    }

    /**
     * Percebe o ambiente observando os eventos ocorridos.
     * 
     * @return Uma percepção captada do ambiente.
     */
    protected Percepcao percepcionar() {
        Evento evento = ambiente.observar();
        return new Percepcao(evento);
    }

    /**
     * Realiza uma ação no ambiente com base na ação determinada pelo controlo.
     * 
     * @param accao (A ação a ser executada no ambiente).
     */
    protected void actuar(Accao accao) {
        if (accao != null && accao.comando != null) {
            ambiente.executar(accao.comando);
        }
    }
}
