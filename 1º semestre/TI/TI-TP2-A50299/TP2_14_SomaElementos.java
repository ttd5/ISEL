package TI_TP2_A50299;

import java.util.Scanner;

public class TP2_14_SomaElementos {

	public static void main(String[] args) {
		/** 14. Implemente um programa (TP2-14-SomaElementos) que crie um array (pode mesmo criá-lo no próprio código Java), 
		 * peça um número n ao utilizador, e encontre todos os pares de números no array cuja soma seja igual ao número n. 
		 * Ex: Para o array A=[1, 1, 2, 3, 4, 5, 6, 6] e para n=5, deverá sugerir {1+4, 1+4, 2+3}.
		 */

			//nome do programa
			System.out.println("..::TP2-14-SomaElementos::..");
				
			//declaração de variáveis
			int n;
				
			int array[] = {1, 1, 2, 3, 4, 5, 6, 6};
				
			//the keyboard reader
			Scanner keyboard = new Scanner(System.in);
				
			//pedir os valores ao utilizador
				
			System.out.println("Introduza um valor inteiro:");
				
			n = keyboard.nextInt();
				
			System.out.print("Array : [");
				
			for (int i = 0; i < array.length; i++) {
					
				for (int j = 0; j < array.length; j++) {
						
					if (array[i] + array[j] == n) {
							
					System.out.print((i != array.length - 1?  array[i] + "+" + array[j] + ", " : ""));	
					}
				}
			}
				
			System.out.print("]");
				
			//close the keyboard
			keyboard.close();			
	}
}