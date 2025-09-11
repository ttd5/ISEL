package ambiente;

/**
 * Define as operações básicas que um ambiente deve suportar para ser utilizado por um agente.
 */
public interface Ambiente {
	
	/**
	 * Evolui o estado do ambiente, gerando novos eventos.
	 */
	public void evoluir();
	
	/**
	 * Observa o estado atual do ambiente e retorna o evento que ocorre no momento.
	 * 
	 * @return O evento atual do ambiente.
	 */
	public Evento observar();
	
	/**
	 * Executa um comando no ambiente.
	 * 
	 * @param comando (O comando a ser executado no ambiente).
	 */
	public void executar(Comando comando);
}
