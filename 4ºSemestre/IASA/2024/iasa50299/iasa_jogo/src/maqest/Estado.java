package maqest;

import java.util.HashMap;
import java.util.Map;
import agente.Accao;
import ambiente.Evento;

/**
 * Representa um estado dentro de uma máquina de estados, contendo transições para outros estados.
 */
public class Estado {
	
	public String nome;
	private Map<Evento, Transicao> transicoes;

	/**
	 * Constrói um novo estado com o nome especificado.
	 * 
	 * @param nome O nome do estado.
	 */
	public Estado(String nome) {
		this.nome = nome;
        transicoes = new HashMap<>();
	}
	
	/**
	 * Processa um evento e retorna a transição associada a esse evento, se houver.
	 * 
	 * @param evento (O evento a ser processado).
	 * @return A transição correspondente ao evento, ou null se o evento não tiver uma transição associada.
	 */
	public Transicao processar(Evento evento) {
		return transicoes.get(evento);	
	}
	
	/**
	 * Adiciona uma transição a partir deste estado, sem definir uma ação específica.
	 * 
	 * @param evento (O evento que desencadeia a transição).
	 * @param estadoSucessor (O estado para o qual a transição leva).
	 * @return A transição.
	 */
	public Estado transicao(Evento evento, Estado estadoSucessor) {
		return transicao(evento, estadoSucessor, null);	
	}
	
	/**
	 * Adiciona uma transição a partir deste estado, especificando uma ação a ser realizada.
	 * 
	 * @param evento (O evento que desencadeia a transição).
	 * @param estadoSucessor (O estado para o qual a transição leva).
	 * @param accao (A ação a ser realizada durante a transição).
	 * @return O estado atual.
	 */
	public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao) {
		Transicao transicao = new Transicao(estadoSucessor, accao);
        transicoes.put(evento, transicao);
        return this;
	}
}
