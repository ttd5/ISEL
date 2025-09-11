package jogo;

/**
 * IASA 23/24
 *
 * Trabalho realizado por:
 * Tatiana Damaya
 *
 * Docente Carlos Junior
 */

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

/*
* Aplicação: "O jogo consiste num ambiente onde a personagem tem por objectivo registar a presença de animais através de fotografias".
*/

/**
 * Classe principal que inicia e executa o jogo.
 */
public class Jogo {

    /*
     * Atributos privados correspondentes à personagem e ao ambiente.
     */
    private static AmbienteJogo ambiente;
    private static Personagem personagem;

    /**
     * Realiza o ciclo principal do jogo, onde o ambiente evolui e a personagem executa ações até que o evento TERMINAR ocorra.
     */
    private static void executar() {
        do {
            ambiente.evoluir();
            personagem.executar();
        } while (ambiente.evento != EventoJogo.TERMINAR);
    }

    /**
     * Método principal que inicializa os objetos do ambiente e da personagem, e inicia a execução do jogo.
     *
     * @param args Argumentos de linha de comando (não utilizados).
     */
    public static void main(String[] args) {
        ambiente = new AmbienteJogo();
        personagem = new Personagem(ambiente);
        executar();
    }
}