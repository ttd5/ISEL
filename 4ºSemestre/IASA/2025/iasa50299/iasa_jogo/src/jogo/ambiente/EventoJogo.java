package jogo.ambiente;

import ambiente.Evento;

/**
 * Enumeração que define os eventos que podem ocorrer no ambiente do jogo.
 * Estes eventos são percecionados pela personagem e influenciam as suas decisões.
 * 
 * @author Tatiana Damaya
 */
public enum EventoJogo implements Evento {

    /** Evento que representa o silêncio no ambiente. */
    SILENCIO, 
    
    /** Evento que representa um ruído detetado. */
    RUIDO, 
    
    /** Evento que indica a presença de um animal. */
    ANIMAL, 
    
    /** Evento que representa a fuga de um animal. */
    FUGA, 
    
    /** Evento de registo fotográfico de um animal. */
    FOTOGRAFIA, 
    
    /** Evento que termina o jogo. */
    TERMINAR;

    /**
     * Mostra o evento atual de forma textual.
     */
    @Override
    public void mostrar() {
        System.out.printf("Evento: %s%n", this);
    }
}
