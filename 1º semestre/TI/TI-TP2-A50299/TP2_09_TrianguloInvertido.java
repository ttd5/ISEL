package TI_TP2_A50299;

import java.util.Scanner;

public class TP2_09_TrianguloInvertido {

	public static void main(String[] args) {
		/** 9. Implemente o programa (TP2-09-TrianguloInvertido) que peça um número n 
		 * e desenhe um triângulo de cardinais invertido com n linhas. 
		 * Ex: para n=4 linhas, o programa deverá desenhar o seguinte triângulo invertido.
		 */
		
		//nome do programa
		System.out.println("..::TP2-09-TrianguloInvertido::..");
		
		//declaração de variáveis
		int n;
		
		//the keyboard reader
		Scanner keyboard = new Scanner(System.in);
		
		//pedir o valor ao utilizador
		
		System.out.println("Introduza um valor para o número de linhas:");
		
		n = keyboard.nextInt();
		
		//construção do triângulo
		
		for (int i = n; i >= 1; i--) {
	
			for (int j = i; j < n + 3; j++) {
				
				System.out.print(" ");
			
				}	
			
			for (int j = 1; j <= 2 * i - 1; j++) {
				
				System.out.print("#");
			
				}
			
			System.out.println();
			
			}
		
		//close the keyboard
		keyboard.close();
	}
}