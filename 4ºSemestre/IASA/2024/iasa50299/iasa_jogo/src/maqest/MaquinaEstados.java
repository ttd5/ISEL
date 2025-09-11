package maqest;

import agente.Accao;
import ambiente.Evento;

/**
 * Implementa uma máquina de estados que gere as transições entre estados baseado em eventos.
 */
public class MaquinaEstados {
	
	public Estado estado;

	/**
	 * Constrói uma nova máquina de estados com um estado inicial.
	 * 
	 * @param estadoInicial (O estado inicial da máquina de estados).
	 */
	public MaquinaEstados(Estado estadoInicial){
        this.estado = estadoInicial;
    }

	/**
	 * Processa um evento, realizando uma transição de estado se aplicável.
	 * 
	 * @param evento (O evento a ser processado).
	 * @return A ação resultante da transição de estado, ou null se não ocorrer transição.
	 */
    public Accao processar(Evento evento){
        Transicao transicao = estado.processar(evento);
        if (transicao != null) {
            estado = transicao.getEstadoSucessor();
            return transicao.getAccao();
        } else { 
            return null; 
        }
    }
}
