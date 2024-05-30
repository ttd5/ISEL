package TI_TP2_A50299;
import java.util.Arrays;
import java.util.Random;

public class TP2_12_BubbleSort {

	public static void main(String[] args) {
		/** 12. Crie um programa (TP2-12-BubbleSort) que crie um array com números aleatórios (entre 1 e 100) 
		 * e ordene os valores no array por ordem crescente. 
		 * Deverá usar o algoritmo bubble sort (https://pt.wikipedia.org/wiki/Bubble_sort) para ordenar o array.
		 */

		//nome do programa
		System.out.println("..::TP2-12-BubbleSort::..");
		
		
		int[] arr = new int[8];
		Random rand = new Random();
		
		System.out.println("O array aleatório gerado é: ");
		
		for (int i = 0; i < arr.length; i++) {
			
			arr[i] = rand.nextInt(1, 100);
		}
		System.out.println(Arrays.toString(arr));
		
		System.out.println("O array aleatório gerado ordenado é: ");
		
		for (int i = 0; i <arr.length; i++) {     
			for (int j = i+1; j <arr.length; j++) {     
				if(arr[i] >arr[j]) {      
					int aux = arr[i];    
	                arr[i] = arr[j];    
	                arr[j] = aux; 
	            }
	        }
		}
		System.out.println(Arrays.toString(arr));		
		}
}