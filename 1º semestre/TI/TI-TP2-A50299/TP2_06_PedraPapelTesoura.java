package TI_TP2_A50299;
import java.util.Random;
import java.util.Scanner;

public class TP2_06_PedraPapelTesoura {

	public static void main(String[] args) {
		/** 6. Implemente o programa (TP2-06-PedraPapelTesoura) que permita jogar ao jogo da “Pedra, papel ou tesoura”. 
		 * O programa deverá começar por gerar aleatoriamente um valor {0, 1, 2} que corresponde a {“Papel”, “Pedra”, “Tesoura”}. 
		 * Deve então colocar numa variável do tipo String a palavra correspondente ao valor aleatório gerado. 
		 * Depois, deve pedir ao utilizador para introduzir a sua escolha, devendo este escrever “Papel”, “Pedra” ou “Tesoura”. 
		 * Esse valor deve ser lido para outra variável do tipo String. Por fim, deve indicar quem ganhou (o programa ou o utilizador) 
		 * seguindo as regras do jogo: a tesoura ganha ao papel (cortando-o), 
		 * a pedra ganha à tesoura (quebrando-a), e o papel ganha à pedra (embrulhando-a).
		 */

	System.out.println("..::TP2_06_PedraPapelTesoura::..");
		
	//declaração de variáveis
	int random;
	String pc = "", player = "";
		
	//gerar número aleatório
	Random rand = new Random();
	random = rand.nextInt(2);
	
	//atribuir número aleatório a papel, pedra, tesoura
	if(random == 0) {
		
		pc = "papel";
	
	}
		
	else if(random == 1) {
			
		pc = "pedra";
			
	}
		
	else if(random == 2) {
		
		pc = "tesoura";
		
	}
	
	//jogada do utilizador
	
	Scanner keyboard = new Scanner(System.in);
	
	System.out.println("Pedra, papel, tesoura?");
	
	player = keyboard.nextLine();
	

	//empate
	
	if(player.equals(pc)) {
		System.out.println("Pc jogou [" + pc + "] e player jogou [" + player + "]. EMPATE!");	
	}
	
	//ganhar
	
	else if(player.equals("papel") && pc.equals("pedra")) {
		
		System.out.println("Pc jogou [" + pc + "] e player jogou [" + player + "]. GANHOU!");	
	
	} 
	
	else if(player.equals("pedra") && pc.equals("tesoura")) {
		
		System.out.println("Pc jogou [" + pc + "] e player jogou [" + player + "]. GANHOU!");	
	
	}	
	
	else if(player.equals("tesoura") && pc.equals("papel")) {
		
		System.out.println("Pc jogou [" + pc + "] e player jogou [" + player + "]. GANHOU!");
	}
	
	//perder
	
	else if(player.equals("papel") && pc.equals("tesoura")) {
			
		System.out.println("Pc jogou [" + pc + "] e player jogou [" + player + "]. PERDEU!");
		
	}
	
	else if(player.equals("pedra") && pc.equals("papel")) {
		
		System.out.println("Pc jogou [" + pc + "] e player jogou [" + player + "]. PERDEU!");
	
	}	
	
	else if(player.equals("tesoura") && pc.equals("pedra")) {
		
		System.out.println("Pc jogou [" + pc + "] e player jogou [" + player + "]. PERDEU!");	
	
	}

	//close the keyboard
	keyboard.close();

	}
}