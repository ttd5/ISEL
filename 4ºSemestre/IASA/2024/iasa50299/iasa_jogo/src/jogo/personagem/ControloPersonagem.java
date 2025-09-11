package jogo.personagem;

import agente.Accao;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Evento;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;
import maqest.Estado;
import maqest.MaquinaEstados;

/**
 * Controla o personagem dentro do jogo, tomando decisões com base nos eventos percebidos.
 */
public class ControloPersonagem implements Controlo {

	private MaquinaEstados maqEst;

	/**
	 * Inicializa o controlador do personagem, define estados e ações e todas as associações entre eventos e transições.
	 */
	public ControloPersonagem() {
		Estado procura = new Estado("PROCURA");
		Estado inspecao = new Estado("INSPEÇÃO");
		Estado observacao = new Estado("OBSERVAÇÃO");
		Estado registo = new Estado("REGISTO");

		Accao procurar = new Accao(ComandoJogo.PROCURAR);
		Accao aproximar = new Accao(ComandoJogo.APROXIMAR);
		Accao observar = new Accao(ComandoJogo.OBSERVAR);
		Accao fotografar = new Accao(ComandoJogo.FOTOGRAFAR);

		procura.transicao(EventoJogo.RUIDO, inspecao, aproximar).transicao(EventoJogo.SILENCIO, procura, procurar)
				.transicao(EventoJogo.ANIMAL, observacao, aproximar);

		inspecao.transicao(EventoJogo.RUIDO, inspecao, procurar).transicao(EventoJogo.SILENCIO, procura)
				.transicao(EventoJogo.ANIMAL, observacao, aproximar);

		observacao.transicao(EventoJogo.FUGA, inspecao).transicao(EventoJogo.ANIMAL, registo, observar);

		registo.transicao(EventoJogo.ANIMAL, registo, fotografar).transicao(EventoJogo.FUGA, procura)
				.transicao(EventoJogo.FOTOGRAFIA, procura);

		maqEst = new MaquinaEstados(procura);
	}

	/**
	 * Processa a percepção atual e determina a ação a ser tomada.
	 * 
	 * @param percepcao (A percepção atual do ambiente).
	 * @return accao (A ação a ser executada em resposta à percepção).
	 */
	@Override
	public Accao processar(Percepcao percepcao) {
		Evento evento = percepcao.getEvento();
		Accao accao = maqEst.processar(evento);
		mostrar();
		return accao;
	}

	/**
	 * Mostra o estado atual da máquina de estados na consola.
	 */
	private void mostrar() {
		System.out.printf("Estado: %s%n", maqEst.estado.nome);
	}

}