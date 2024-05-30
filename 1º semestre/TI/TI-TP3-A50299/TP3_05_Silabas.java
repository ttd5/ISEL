package TI_TP3_A50299;

import java.util.Scanner;

public class TP3_05_Silabas {

	public static void main(String[] args) {
		/** 5. Crie um programa (TP3-05-Silabas) que conte o número de sílabas de uma palavra. 
		 * O número de sílabas pode ser obtido (aproximadamente) pelo número de vogais não sucessivas existentes numa palavra. 
		 * Por exemplo “valor” tem duas sílabas enquanto “biblioteca” tem 4 sílabas (note que “io” conta apenas uma vez). 
		 * Use os seguintes métodos: 
		 * boolean isVogal(char ch) que verifica se o caracter ch é uma vogal (“a, e, i, o, u”); 
		 * int countVogais(String str) que retorna o número de vogais numa string; 
		 * int countParesVogais(String str) que retorna o número de pares sucessivos de vogais; 
		 * int silabas(String str) que calcula o número de sílabas (num. Vogais – num. Pares vogais).
		 */	

		System.out.println("..::TP3-05-Silabas::..");
		String palavra;
		System.out.println("Introduza uma palavra:");
		Scanner keyboard = new Scanner(System.in);
		palavra = keyboard.nextLine();
		System.out.print("A palavra " + palavra + " tem " + silabas(palavra) + " silabas.");
		keyboard.close();	
	}
	
	public static boolean isVogal(char ch) {
		if(ch == 97 || ch == 101 || ch == 105 || ch == 111 || ch == 117 || ch == 65 || ch == 69 || ch == 73 || ch == 79 || ch == 85) {
			return true;
		} else return false;
	}
	
	public static int countVogais(String str) {
		int countVogais = 0;
		for(int i = 0; i < str.length(); i++) {
			if(isVogal(str.charAt(i)) == true) {
				countVogais++;
			}
		}
		return countVogais;
	}
	
	public static int countParesVogais(String str) {
		int countParesVogais = 0;
		for(int i = 0; i < str.length() - 1 ; i++) {
			if(isVogal(str.charAt(i)) == true && isVogal(str.charAt(i + 1)) == true) {
				countParesVogais++;
			}	
		}
		return countParesVogais;
	}	
	
	
	public static int silabas(String str) {
		int silabas = countVogais(str) - countParesVogais(str);
		return silabas;
	}
}