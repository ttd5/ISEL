package TI_TP3_A50299;

import java.util.Arrays;
import java.util.Scanner;

public class TP3_07_MaioresQue {
	public static void main(String[] args) {
		/** 7. Crie o programa (TP3-07-MaioresQue) que implemente o método recursivo int maioresQue(int[] array, int val). 
		 * Este método deverá retornar quantos números no array são maiores do que o número val. 
		 * Por exemplo, para o array {1, 2, 3, 4, 5} existem 2 números maiores do que o 3 (i.e., o 4 e o 5). 
		 * Considere usar o método Arrays.copyOfRange(int[] original, int from, int to) que retorna uma cópia do array original entre os índices from e to.
		 */
		
		System.out.println("..::TP3-07-MaioresQue::..");

		int n, val;
		
		Scanner keyboard = new Scanner(System.in);
		
		//criar array do utilizador
		System.out.println("Introduza um valor para o número de posições do array:");
		n = keyboard.nextInt();
		int[] arr = new int[n];
		System.out.println("Introduza " + n + " valores para as posições do array:");
		for (int i = 0; i < arr.length; i++) {
			arr[i] = keyboard.nextInt();
		}
		System.out.println("Introduza o valor a ser comparado:");
		val = keyboard.nextInt();
		
		System.out.println("O Array formado foi: " + Arrays.toString(arr));
		System.out.println("Existem " + maioresQue(arr, val) + " números no array que são maiores do que o número " + val + "!");
		
		keyboard.close();	
	}
	
	public static int maioresQue(int[] array, int val) {
		if (array.length == 0) return 0;
		int count = maioresQue(Arrays.copyOfRange(array, 1, array.length), val);
		if(array[0] > val) count++;
		return count;
	}
}	