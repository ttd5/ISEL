package TI_TP2_A50299;
import java.util.Random;
import java.util.Scanner;

public class TP2_11_RandomArray {

	public static void main(String[] args) {
		/** 11. Implemente o programa (TP2-11-RandomArray) que peça um número n ao utilizador, 
		 * crie um array com n posições, e coloque um número aleatório (entre 0 e 100) em cada uma das posições do array. 
		 * Por fim, deverá mostrar todos os números e o seu somatório.
		 */
		
				//nome do programa
				System.out.println("..::TP2-11-RandomArray::..");
				
				//declaração de variáveis
				int n, soma = 0;
				
				//the keyboard reader
				Scanner keyboard = new Scanner(System.in);
				
				//pedir os valores ao utilizador
				
				System.out.println("Introduza um valor para o número de posições do array:");
				
				n = keyboard.nextInt();
				
				//criar o array com n posições e colocar um número aleatório (entre 0 e 100) em cada uma das posições do array 
				
				int[] array = new int[n];
				
				System.out.print("O array aleatório gerado foi : [");
				
				Random rand = new Random();
				
				for (int i = 0; i < array.length; i++) {
					
					array[i] = rand.nextInt(100);
					soma += array[i];
	
					System.out.print(array[i] + (i != array.length - 1? ", " : ""));
						
				}
				
				System.out.println("]");
				
				System.out.println("A soma do array aleatório gerado foi " + soma + ".");
				
				//close the keyboard
				keyboard.close();
	}
}