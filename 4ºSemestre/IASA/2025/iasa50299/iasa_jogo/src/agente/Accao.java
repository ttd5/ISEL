package agente;

import ambiente.Comando;

/**
 * Classe que encapsula uma ação a ser executada no ambiente do jogo.
 * Uma ação consiste num comando específico que será interpretado e
 * executado pelo ambiente.
 * 
 * Esta classe é fundamental para permitir a interação do agente com o ambiente,
 * uma vez que as decisões tomadas pelo sistema de controlo do agente são
 * traduzidas em ações concretas através de instâncias desta classe.
 *
 * @author Tatiana Damaya
 */
public class Accao {
    
    /** O comando associado a esta ação. */
    private Comando comando;
    
    /**
     * Construtor que cria uma nova ação com o comando especificado.
     *
     * @param comando o comando a ser associado a esta ação
     */
    public Accao(Comando comando){
        this.comando = comando;
    }

    /**
     * Obtém o comando associado a esta ação.
     *
     * @return o comando desta ação
     */
    public Comando getComando(){
        return comando;
    }
}
