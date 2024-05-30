package TI_TP3_A50299;

import java.util.Scanner;

public class TP3_08_RemoveEspacosConsecutivos {

	public static void main(String[] args) {
		/** 8. Crie o programa (TP3-08-RemoveEspacosConsecutivos) que implemente o método recursivo String removeEspacosConsecutivos(String str). 
		 * Este método deverá retornar a string original sem os espaços consecutivos. 
		 * Por exemplo, para a string “ab cd” o método deverá retornar a string “ab cd”.
		 */
		
		System.out.println("..::TP3-08-RemoveEspacosConsecutivos::..");
		String palavra;
		System.out.println("Introduza uma palavra:");
		Scanner keyboard = new Scanner(System.in);
		palavra = keyboard.nextLine();
		System.out.print(removeEspacosConsecutivos(palavra));
		keyboard.close();

	}
	
	public static String removeEspacosConsecutivos(String str) {
		if(str.length() == 0) return "";
		if(str.charAt(0) == ' ' && str.charAt(1) == ' ') return removeEspacosConsecutivos(str.substring(1));
		return str.charAt(0) + removeEspacosConsecutivos(str.substring(1));
	}
}