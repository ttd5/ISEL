package TI_TP2_A50299;

import java.util.Random;
import java.util.Scanner;

public class TP2_15_SomaMatrizes {

	public static void main(String[] args) {
		/**15. Faça um programa (TP2-15-SomaMatrizes) que crie duas matrizes n x n e faça a soma das matrizes. 
		 * Pode pedir o n ao utilizador e preencher a matriz com números aleatórios.
		 */

		int n;
		
		Scanner keyboard = new Scanner(System.in);
		System.out.println("Introduza um valor para o tamanho da matriz:");
		
		n = keyboard.nextInt();
		
		int[][] arr1 = new int[n][n];
		int[][] arr2 = new int[n][n];

		Random rand = new Random();
		
		System.out.print("Matriz 1:\n");
				
		for (int i = 0; i < arr1.length; i++) {
			
			for (int j = 0; j < arr1.length; j++) {
			
				arr1[i][j] = rand.nextInt(10);
				 
				System.out.print(arr1[i][j] + "  ");
			}
			
			System.out.println("  ");
		}
		
		System.out.println("\nMatriz 2:");
		
		for (int i = 0; i < arr2.length; i++) {
			
			for (int j = 0; j < arr2.length; j++) {
			
				arr2[i][j] = rand.nextInt(10);
				System.out.print(arr2[i][j]+ "  ");
				
			}
			
			System.out.println("  ");
		}
		
		System.out.println("\nSoma: ");
		
		for (int i = 0; i < arr1.length; i++) {
			
			for (int j = 0; j < arr2.length; j++) {
				
				int soma = arr1[i][j] + arr2[i][j];
				
				System.out.print(soma + "  ");
				
			}
			System.out.println("  ");
		}
		
		//close the keyboard
		keyboard.close();
	}
}