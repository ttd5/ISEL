package jogo.personagem;

import agente.Agente;
import jogo.ambiente.AmbienteJogo;

/**
 * Representa um personagem no jogo, capaz de interagir com o ambiente.
 */
public class Personagem extends Agente {

	/**
	 * Cria um novo personagem com um ambiente e controlador específicos.
	 * 
	 * @param ambiente (O ambiente do jogo ao qual o personagem pertence).
	 */
	public Personagem(AmbienteJogo ambiente) {
		super(ambiente, new ControloPersonagem());
	}
}
