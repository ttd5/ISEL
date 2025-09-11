package maqest;

import agente.Accao;
import ambiente.Evento;

/**
 * Classe que gere uma máquina de estados finitos.
 * Processa eventos, executa as transições associadas e atualiza
 * o estado atual.
 * 
 * @author Tatiana Damaya
 */
public class MaquinaEstados {

    /** O estado atual da máquina de estados. */
    private Estado estado;

    /**
     * Construtor que cria a máquina de estados a partir de um estado inicial.
     *
     * @param estadoInicial o estado inicial da máquina
     */
    public MaquinaEstados(Estado estadoInicial) {
        this.estado = estadoInicial;
    }

    /**
     * Obtém o estado atual da máquina.
     *
     * @return o estado atual
     */
    public Estado getEstado() {
        return estado;
    }

    /**
     * Processa um evento e executa a transição correspondente,
     * se existir, atualizando o estado atual e devolvendo a ação
     * a executar.
     *
     * @param evento o evento a processar
     * @return a ação associada à transição, ou {@code null} se não existir
     */
    public Accao processar(Evento evento) {
        Transicao transicao = estado.processar(evento);
        if (transicao != null) {
            estado = transicao.getEstadoSucessor();
            return transicao.getAccao();
        } else {
            return null;
        }
    }
}