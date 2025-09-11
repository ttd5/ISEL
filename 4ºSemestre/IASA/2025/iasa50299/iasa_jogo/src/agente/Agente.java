package agente;

import ambiente.Ambiente;

/**
 * Classe que representa um agente genérico no ambiente do jogo.
 * Um agente é responsável por perceber o ambiente, processar as perceções
 * e executar ações de acordo com as decisões do seu sistema de controlo.
 * 
 * Esta classe base fornece o ciclo de operação do agente:
 * percecionar o ambiente, processar a perceção e atuar no ambiente.
 * 
 * 
 * @author Tatiana Damaya
 */
public class Agente {

    /** O ambiente em que o agente atua. */
    private Ambiente ambiente;

    /** O sistema de controlo que processa perceções e determina ações. */
    private Controlo controlo;

    /**
     * Construtor que inicializa o agente com um ambiente e um sistema de controlo.
     *
     * @param ambiente o ambiente em que o agente atua
     * @param controlo o sistema de controlo responsável pela tomada de decisões
     */
    public Agente(Ambiente ambiente, Controlo controlo) {
        this.ambiente = ambiente;
        this.controlo = controlo;
    }

    /**
     * Executa um ciclo completo de perceção, processamento e ação.
     * O agente observa o ambiente, processa a perceção através do controlo
     * e executa a ação resultante no ambiente.
     */
    public void executar() {
        actuar(controlo.processar(percepcionar()));
    }

    /**
     * Observa o ambiente para obter uma perceção.
     *
     * @return a perceção criada a partir do evento observado no ambiente
     */
    protected Percepcao percepcionar(){
        return new Percepcao(ambiente.observar());
    }

    /**
     * Executa a ação recebida no ambiente.
     *
     * @param accao a ação a ser executada no ambiente
     */
    protected void actuar(Accao accao) {
        if (accao != null){
            ambiente.executar(accao.getComando());
        }
    }
}
