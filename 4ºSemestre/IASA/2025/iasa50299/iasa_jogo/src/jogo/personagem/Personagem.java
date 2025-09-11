package jogo.personagem;

import agente.Agente;
import jogo.ambiente.AmbienteJogo;

/**
 * Classe que representa a personagem principal do jogo.
 * Estende a classe base {@code Agente} e define o ambiente de jogo e o
 * sistema de controlo específico da personagem.
 * 
 * @author Tatiana Damaya
 */
public class Personagem extends Agente {

    /**
     * Construtor que cria a personagem com o ambiente de jogo e o controlo
     * específico {@code ControloPersonagem}.
     *
     * @param ambiente o ambiente de jogo onde a personagem atua
     */
    public Personagem(AmbienteJogo ambiente) {
        super(ambiente, new ControloPersonagem());
    }
}