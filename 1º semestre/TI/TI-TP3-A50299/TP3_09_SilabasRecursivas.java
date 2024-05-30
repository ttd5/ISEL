package TI_TP3_A50299;

import java.util.Scanner;

public class TP3_09_SilabasRecursivas {

	public static void main(String[] args) {
		/** 9. Crie o programa (TP3-09-SilabasRecursivas) que reimplemente o método int silabas(String str) de forma recursiva. 
		 * Tenha atenção que duas vogais seguidas devem contar apenas como uma sílaba. 
		 * Utilize o método boolean isVogal(char ch) para facilitar a lógica do programa.
		 */
		System.out.println("..::TP3-09-SilabasRecursivas::..");
		String palavra;
		System.out.println("Introduza uma palavra:");
		Scanner keyboard = new Scanner(System.in);
		palavra = keyboard.nextLine();
		System.out.print("A palavra [" + palavra + "] tem " + silabas(palavra) + " silabas!");
		keyboard.close();

	}

	public static int silabas(String str) {
		if (str.length() == 1) return 0;
		int count = silabas(str.substring(1));
		if(isVogal(str.charAt(0)) == true && isVogal(str.charAt(1)) == false) count ++;
		if(isVogal(str.charAt(0)) == true && isVogal(str.charAt(1)) == true) count ++;
		return count;
	}
	
	public static boolean isVogal(char ch) {
		if(ch == 97 || ch == 101 || ch == 105 || ch == 111 || ch == 117 || ch == 65 || ch == 69 || ch == 73 || ch == 79 || ch == 85) {
			return true;
		} else return false;
	}
}