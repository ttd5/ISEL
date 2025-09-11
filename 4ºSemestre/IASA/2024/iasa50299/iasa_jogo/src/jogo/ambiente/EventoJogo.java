package jogo.ambiente;

import ambiente.Evento;

/**
 * Enum que define os eventos possíveis dentro do jogo.
 */
public enum EventoJogo implements Evento {
	SILENCIO, RUIDO, ANIMAL, FUGA, FOTOGRAFIA, TERMINAR;

	/**
	 * Exibe o evento atual.
	 */
	@Override
	public void mostrar() {
		System.out.printf("Evento: %s%n", this);
	}
}
