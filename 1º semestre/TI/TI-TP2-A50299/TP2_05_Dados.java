package TI_TP2_A50299;

import java.util.Random;
import java.util.Scanner;

public class TP2_05_Dados {

	public static void main(String[] args) {
		/** 5. Implemente um programa (TP2-05-Dados) em que o computador manda um dado (número aleatório entre 1 e 6) 
		 * e o jogador terá de acertar no número. Utilize a classe Random e o método nextInt(int n).
		 */
	
	//nome do programa
	System.out.println("..::TP2-05-Dados::..");
	
	//declaração de variáveis
	int random, num;
	
	//gerar número aleatório
	
	Random rand = new Random();
	
	random = rand.nextInt(6) + 1;
	
	Scanner keyboard = new Scanner(System.in);
	
	//jogo
	while(true)  {
		
	System.out.println("Qual o número aleatório entre 1 e 6?");
	num = keyboard.nextInt();
	
		if (num == random) {
			System.out.println("Acertou!");
			break;
		}
		else if (num != random){
		System.out.println("Tente outra vez!");
		}
	}
	
	//close the keyboard
	keyboard.close();
	
	}
}