package jogo.personagem;

import agente.Accao;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Evento;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;
import maqest.Estado;
import maqest.MaquinaEstados;

/**
 * Classe que define o sistema de controlo da personagem do jogo.
 * Usa uma máquina de estados para processar perceções e determinar
 * as ações a executar em cada estado.
 * 
 * @author Tatiana Damaya
 */
public class ControloPersonagem implements Controlo {

    /** Máquina de estados que gere o comportamento da personagem. */
    private MaquinaEstados maqEst;

    /** Estado atual da máquina de estados. */
    private Estado estado;

    /**
     * Construtor que inicializa a máquina de estados com todos os estados
     * e transições definidos para a personagem.
     */
    public ControloPersonagem() {
        Estado procura = new Estado("PROCURA");
        Estado inspecao = new Estado("INSPEÇÃO");
        Estado observacao = new Estado("OBSERVAÇÃO");
        Estado registo = new Estado("REGISTO");

        Accao procurar = new Accao(ComandoJogo.PROCURAR);
        Accao aproximar = new Accao(ComandoJogo.APROXIMAR);
        Accao observar = new Accao(ComandoJogo.OBSERVAR);
        Accao fotografar = new Accao(ComandoJogo.FOTOGRAFAR);

        // transições do estado procura
        procura
                .transicao(EventoJogo.ANIMAL, observacao, aproximar)
                .transicao(EventoJogo.RUIDO, inspecao, aproximar)
                .transicao(EventoJogo.SILENCIO, procura);
        // transições do estado inspecção
        inspecao
                .transicao(EventoJogo.RUIDO, inspecao, procurar)
                .transicao(EventoJogo.ANIMAL, observacao, aproximar)
                .transicao(EventoJogo.SILENCIO, procura);
        // transições do estado observação
        observacao
                .transicao(EventoJogo.ANIMAL, registo, observar)
                .transicao(EventoJogo.FUGA, inspecao);
        // transições do estado registo
        registo
                .transicao(EventoJogo.ANIMAL, registo, fotografar)
                .transicao(EventoJogo.FUGA, procura)
                .transicao(EventoJogo.FOTOGRAFIA, procura);

        estado = procura;
        maqEst = new MaquinaEstados(estado);
    }

    /**
     * Obtém o estado atual da máquina de estados.
     *
     * @return o estado atual
     */
    public Estado getEstado() {
        return estado;
    }

    /**
     * Processa uma perceção e devolve a ação correspondente de acordo com
     * a máquina de estados.
     *
     * @param percepcao a perceção observada no ambiente
     * @return a ação a executar, ou {@code null} se não existir perceção
     */
    @Override
    public Accao processar(Percepcao percepcao) {
        if (percepcao == null) {
            return null;
        }
        Evento evento = percepcao.getEvento();
        Accao accao = maqEst.processar(evento);
        estado = maqEst.getEstado();
        mostrar();
        return accao;
    }

    /**
     * Mostra o estado atual da personagem no ambiente.
     */
    private void mostrar() {
        System.out.printf("Estado: %s%n", getEstado().nome);
    }
}