package TI_TP3_A50299;

import java.util.Scanner;

public class TP3_04_Password {

	public static void main(String[] args) {
		/** 4. Crie um programa (TP3-04-Password) que peça uma password ao utilizador e verifique se é válida. 
		 * Uma password válida deverá conter pelo menos 10 caracteres (letras e números) onde, no mínimo, dois caracteres são numéricos e três caracteres são letras. 
		 * Para tal deverá criar os seguintes métodos: 
		 * boolean isLetter(char ch) que verifica se o caracter ch é uma letra (“a-z”, “A-Z”); 
		 * boolean isDigit(char ch) que verifica se o caracter ch é um digito numérico; 
		 * boolean isValid(String password) que verifica se a password é válida ou não consoante as regras mencionadas.
		 */
		
		System.out.println("..::TP3-04-Password::..");
		String password;
		System.out.println("Introduza uma password:");
		Scanner keyboard = new Scanner(System.in);
		password = keyboard.nextLine();
		System.out.print("A sua password é " + (isValid(password) != true? "inválida!" : "válida!"));
		keyboard.close();
		
	}
	
	public static boolean isLetter(char ch) {
		
		if (ch >= 65 && ch <= 90 || ch >= 97 && ch <= 122) {
			return true;
		} else return false;		
	}
	
	public static boolean isDigit(char ch) {
		
		if (ch >= 48 && ch <= 57) {
			return true;
		} else return false;
	}
	
	public static boolean isValid(String password) {
		
		boolean isValid = false;
		
		if (password.length() >= 10) {
			int countLetter = 0;
			int countDigit = 0;
			
		for(int i = 0; i < password.length(); i++) {
			
			char ch = password.charAt(i);
				
			if (isLetter(ch) == true) {
			
				countLetter++;
			
			}
			
			if(isDigit(ch) == true) {
				
				countDigit ++;
				
			}
			
			if(countLetter >= 3 && countDigit >= 2) {
				isValid = true;
			} else isValid = false;
		}
		}
		return isValid;
	}
}