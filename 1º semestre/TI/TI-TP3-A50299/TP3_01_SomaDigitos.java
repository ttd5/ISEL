package TI_TP3_A50299;
import java.util.Scanner;

public class TP3_01_SomaDigitos {

	public static void main(String[] args) {
		/** 1. Crie uma classe (TP3-01-SomaDigitos) que implemente o método int somaDigitos(int n). 
		 * Este método deverá receber um número n e retornar a soma de todos os seus dígitos. 
		 * Ex: somaDigitos(1234) deverá retornar o número 10.
		 */
	
		System.out.println("..::TP3-01-SomaDigitos::..");
		int num;
		System.out.println("Introduza um número:");
		Scanner keyboard = new Scanner(System.in);
		num = keyboard.nextInt();
		System.out.println("A soma de todos os dígitos do número [" + num + "] é: " + somaDigitos(num));
		keyboard.close();
	}
	
		public static int somaDigitos(int n) {
			int soma = 0;
			while (n > 0)  {       
				soma += (n % 10);  
				n = n / 10;  
			}  
			return soma;  
		}  
}