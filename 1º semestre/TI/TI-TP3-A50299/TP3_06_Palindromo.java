package TI_TP3_A50299;

import java.util.Scanner;

public class TP3_06_Palindromo {

	public static void main(String[] args) {
		/** 6. Crie um programa (TP3-06-Palindromo) que implemente o método recursivo boolean palindromo(String str). 
		 * Este método deverá devolver true caso a string seja um palíndromo, e false caso contrário. 
		 * Um palíndromo é uma palavra que se lê da mesma forma da esquerda para a direita e ao contrário. 
		 * Considere usar o método str.substring(int a, int b) que retorna uma sub-string entre os índices a e b.
		 */
		
		System.out.println("..::TP3-06-Palindromo::..");
		String palavra;
		System.out.println("Introduza uma palavra:");
		Scanner keyboard = new Scanner(System.in);
		palavra = keyboard.nextLine();
		System.out.print("A palavra [" + palavra + (palindromo(palavra) != true? "] não é um palíndromo!" : "] é um palíndromo!"));
		keyboard.close();	
	
	}

	public static boolean palindromo(String str) {
		if(str.length() == 1) return true;
		else if (str.length() == 2 && str.charAt(0) == str.charAt(1)) return true;
		else if(str.charAt(0) ==  str.charAt(str.length() - 1)) return palindromo(str.substring(1, str.length() - 1));
		return false;
	}
}