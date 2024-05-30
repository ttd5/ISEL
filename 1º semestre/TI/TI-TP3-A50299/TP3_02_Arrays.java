package TI_TP3_A50299;
import java.util.Arrays;
import java.util.Scanner;

public class TP3_02_Arrays {

	public static void main(String[] args) {
		/** 2. Crie uma classe (TP3-02-Arrays) que implemente os seguintes métodos: 
		 * int max(int[] array) que retorna o valor maior de um array; 
		 * int min(int[] array) que retorna o valor menor do array; 
		 * int sum(int[] array) que retorna a soma de todos os números do array; 
		 * double avg(int[] array) que retorna o valor médio do array.
		 */
		
		System.out.println("..::TP3-02-Arrays::..");

		int n;
		
		Scanner keyboard = new Scanner(System.in);
		
		//criar array do utilizador
		System.out.println("Introduza um valor para o número de posições do array:");
	
		n = keyboard.nextInt();
		int[] arr = new int[n];
		
		System.out.println("Introduza " + n + " valores para as posições do array:");
		
		for (int i = 0; i < arr.length; i++) {
			arr[i] = keyboard.nextInt();
		}
		System.out.println("O Array formado foi : " + Arrays.toString(arr));
		System.out.println("O número maior do Array é : " + max(arr));
		System.out.println("O número menor do Array é : " + min(arr));
		System.out.println("A soma do Array é : " + sum(arr));
		System.out.println("A média do Array é : " + avg(arr));
		keyboard.close();
	}
	
	//maior
	public static int max(int[] array) {
		int max = array[0];
		for (int i = 0; i < array.length; i++) {
			if(array[i] > max) {
				max = array[i];
			}
		}
		return max;
	}
	
	//menor
	public static int min(int[] array) {
		int min = array[0];
		for (int i = 0; i < array.length; i++) {
			if(array[i] < min) {
				min = array[i];
			}
		}
		return min;
	}
	
	//soma
	public static int sum(int[] array) {
		int sum = 0;
		for (int i = 0; i < array.length; i++) {
			sum += array[i];
		}
		return sum;
	}
	
	//valor médio
	public static double avg(int[] array) {
		double media = sum(array)/array.length;
		return media;
	}		
}