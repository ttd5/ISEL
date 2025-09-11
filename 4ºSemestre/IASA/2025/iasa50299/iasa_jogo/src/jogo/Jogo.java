package jogo;

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

/**
 * Classe principal do jogo. Responsável por inicializar o ambiente e a personagem,
 * e por controlar o ciclo de interação entre eles.
 * 
 * O jogo termina quando o evento {@code EventoJogo.TERMINAR} ocorre.
 * 
 * @author Tatiana Damaya
 */
public class Jogo {

    /** A personagem principal do jogo. */
    private static Personagem personagem;

    /** O ambiente onde o jogo ocorre. */
    private static AmbienteJogo ambiente;

    /**
     * Método principal que inicia o jogo.
     *
     * @param args argumentos da linha de comandos (não são usados)
     */
    public static void main(String[] args) {
        ambiente = new AmbienteJogo();
        personagem = new Personagem(ambiente);
        executar();
    }

    /**
     * Executa o ciclo principal do jogo.
     * O ambiente gera eventos e a personagem reage a esses eventos
     * até que o evento {@code TERMINAR} seja gerado.
     */
    private static void executar() {
        while (ambiente.getEvento() != EventoJogo.TERMINAR) {
            ambiente.evoluir();
            personagem.executar();
        }
    }
}