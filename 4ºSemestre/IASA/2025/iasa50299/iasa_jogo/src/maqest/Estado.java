package maqest;

import agente.Accao;
import ambiente.Evento;
import java.util.HashMap;
import java.util.Map;

/**
 * Classe que representa um estado numa máquina de estados finitos.
 * Cada estado possui um nome e um conjunto de transições que definem
 * como o agente se comporta ao receber determinados eventos.
 * 
 * @author Tatiana Damaya
 */
public class Estado {

    /** Nome do estado. */
    public String nome;

    /** Mapa de transições a partir deste estado, indexado por eventos. */
    private Map<Evento, Transicao> transicoes;

    /**
     * Construtor que cria um estado com o nome especificado.
     *
     * @param nome o nome do estado
     */
    public Estado(String nome) {
        this.nome = nome;
        this.transicoes = new HashMap<Evento, Transicao>();
    }

    /**
     * Processa um evento e devolve a transição associada a esse evento,
     * se existir.
     *
     * @param evento o evento a processar
     * @return a transição correspondente, ou {@code null} se não existir
     */
    public Transicao processar(Evento evento) {
        return transicoes.get(evento);
    }

    /**
     * Adiciona uma transição a partir deste estado para outro estado,
     * sem ação associada.
     *
     * @param evento o evento que dispara a transição
     * @param estadoSucessor o estado para o qual transitar
     * @return este estado, para encadeamento de chamadas
     */
    public Estado transicao(Evento evento, Estado estadoSucessor) {
        return transicao(evento, estadoSucessor, null);
    }

    /**
     * Adiciona uma transição a partir deste estado para outro estado,
     * com a ação a executar.
     *
     * @param evento o evento que dispara a transição
     * @param estadoSucessor o estado para o qual transitar
     * @param accao a ação a executar durante a transição
     * @return este estado, para encadeamento de chamadas
     */
    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao) {
        Transicao transicao = new Transicao(estadoSucessor, accao);
        transicoes.put(evento, transicao);
        return this;
    }
}