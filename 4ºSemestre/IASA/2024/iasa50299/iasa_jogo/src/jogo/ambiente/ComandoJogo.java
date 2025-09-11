package jogo.ambiente;

import ambiente.Comando;

/**
 * Enum que define os comandos disponíveis no jogo.
 */
public enum ComandoJogo implements Comando {
	PROCURAR, APROXIMAR, OBSERVAR, FOTOGRAFAR;

	/**
	 * Exibe o comando atual.
	 */
	@Override
	public void mostrar() {
		System.out.printf("Ação: %s%n", this);
        System.out.println();
	}
}
