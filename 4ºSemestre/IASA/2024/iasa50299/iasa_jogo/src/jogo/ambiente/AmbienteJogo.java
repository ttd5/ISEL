package jogo.ambiente;

import java.util.Map;
import java.util.Scanner;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

import java.util.HashMap;

/**
 * Implementa a interface Ambiente, gerando eventos num ambiente específico num contexto de jogo.
 * Permite a simulação de eventos baseados nos comandos do utilizador.
 */
public class AmbienteJogo implements Ambiente {

    public EventoJogo evento;
    private Scanner keyboard = new Scanner(System.in);
    private Map<String, EventoJogo> eventos;

    /**
     * Construtor para a classe Ambiente. Inicializa o mapeamento de comandos de entrada para eventos específicos.
     */
    public AmbienteJogo() {
        eventos = new HashMap<>();
        eventos.put("s", EventoJogo.SILENCIO);
        eventos.put("r", EventoJogo.RUIDO);
        eventos.put("a", EventoJogo.ANIMAL);
        eventos.put("f", EventoJogo.FUGA);
        eventos.put("p", EventoJogo.FOTOGRAFIA);
        eventos.put("t", EventoJogo.TERMINAR);
    }
    
    /**
     * Evolui o estado do ambiente gerando um novo evento com base na entrada do usuário.
     */
	@Override
	public void evoluir() {
		evento = gerarEvento();
		
	}
    
    /**
     * Exibe o evento atual.
     * 
     * @return O evento atual.
     */
    @Override
	public Evento observar() {
		evento.mostrar();
		return evento;
	}

    /**
     * Exibe o comando atual.
     */
	@Override
	public void executar(Comando comando) {
		comando.mostrar();
	}
	
    /**
     * Solicita ao utilizador a entrada de um evento para ser gerado.
     * Retorna silêncio como padrão se o evento não for reconhecido
     * 
     * @return O EventoJogo correspondente à entrada do usuário.
     */
	private EventoJogo gerarEvento() {
	    System.out.println("\nIntroduzir um evento: \n");
	    System.out.println("s -> SILENCIO, r -> RUIDO, a -> ANIMAL");
	    System.out.println("f -> FUGA, p -> FOTOGRAFIA, t -> TERMINAR");
	    String command = keyboard.next();
	    return eventos.getOrDefault(command, EventoJogo.SILENCIO);
	}

}