package TI_TP2_A50299;

import java.util.Scanner;

public class TP2_08_Normalizar {

	public static void main(String[] args) {
		/** Implemente o programa (TP2-08-Normalizar) que peça ao utilizador um nome e que o mostre normalizado. 
		 * Tenha atenção às palavras como “do”, “dos”, “e”, etc., que normalizadas, deverão ficar em minúsculas. 
		 * Como exemplo, o nome “JOSÉ RODRIGUES DOS SANTOS E CÉU” ficará normalizado como “José Rodrigues dos Santos e Céu”.
		 */
		
		//nome do programa
		System.out.println("..::TP2-08-Normalizar::..");
		
		//declaração de variáveis
		String nome;
		char c;
		StringBuilder correcao = new StringBuilder();
		
		//the keyboard reader
		Scanner keyboard = new Scanner(System.in);
		
		//pedir o nome ao utilizador
		
		System.out.println("Qual o seu nome?");
		
		nome = keyboard.nextLine();
		String minusculas = nome.toLowerCase();//.trim();
		
		System.out.println(minusculas);
		
		//colocar tudo em minusculas e palavra a palavra meter em upper case a primeira letra e palavras com menos de 2 letras deixar  maiusculos
		//normalizar o nome
		
		//dividir frase

		for (int i = 0; i < minusculas.length(); i++) {
			
			if(i == 0) {
				c = minusculas.charAt(i);
				c = minusculas.charAt(i);
				c = (char) (c - 32);
			}
			
			else 
				c = minusculas.charAt(i);
				System.out.print(c);
				
			if( c == 32) {	
			minusculas = minusculas.substring(i + 1, minusculas.length() - i);
			System.out.println(minusculas);
			}	
					
		}
	
		
		//close the keyboard
		keyboard.close();
	}
}