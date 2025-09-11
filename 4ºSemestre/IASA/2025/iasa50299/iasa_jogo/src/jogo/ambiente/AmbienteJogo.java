package jogo.ambiente;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;
import java.util.HashMap;
import java.util.Scanner;

/**
 * Classe que implementa o ambiente de jogo, gerindo os eventos e as interações
 * com o utilizador através de texto.
 *
 * O ambiente permite que o utilizador introduza eventos e observa as ações
 * da personagem, mantendo o ciclo de jogo até ao evento {@code TERMINAR}.
 *
 * 
 * @author Tatiana Damaya
 */
public class AmbienteJogo implements Ambiente {

    /** O evento atual do ambiente. */
    private EventoJogo evento;

    /** Mapa que associa comandos de texto aos eventos do jogo. */
    private HashMap<String, EventoJogo> eventos;

    /** Scanner para ler a entrada do utilizador. */
    private Scanner scanner;

    /**
     * Construtor que inicializa o ambiente e mapeia os comandos de texto
     * para os respetivos eventos.
     */
    public AmbienteJogo() {
        eventos = new HashMap<String, EventoJogo>();
        eventos.put("s", EventoJogo.SILENCIO);
        eventos.put("r", EventoJogo.RUIDO);
        eventos.put("a", EventoJogo.ANIMAL);
        eventos.put("f", EventoJogo.FUGA);
        eventos.put("p", EventoJogo.FOTOGRAFIA);
        eventos.put("t", EventoJogo.TERMINAR);
        
        scanner = new Scanner(System.in);
    }

    /**
     * Avança o ambiente para o próximo evento, solicitando a entrada
     * do utilizador.
     */
    @Override
    public void evoluir() {
        evento = gerarEvento();
    }

    /**
     * Mostra o evento atual e devolve-o.
     *
     * @return o evento atual do ambiente
     */
    @Override
    public Evento observar() {
        evento.mostrar();
        return evento;
    }

    /**
     * Executa o comando especificado e mostra-o.
     *
     * @param comando o comando a executar
     */
    @Override
    public void executar(Comando comando) {
        comando.mostrar();
    }

    /**
     * Solicita ao utilizador a introdução de um evento e devolve o evento correspondente.
     *
     * @return o evento escolhido pelo utilizador
     */
    private EventoJogo gerarEvento() {
        System.out.println("\nIntroduza um evento:");
        System.out.println("[s] SILÊNCIO   [r] RUIDO   [a] ANIMAL");
        System.out.println("[f] FUGA       [p] FOTOGRAFIA   [t] TERMINAR");
        System.out.print("Escolha: ");

        String comando = scanner.next().toLowerCase();
        return eventos.get(comando);
    }

    /**
     * Obtém o evento atual do ambiente.
     *
     * @return o evento atual
     */
    public EventoJogo getEvento() {
        return evento;
    }
}