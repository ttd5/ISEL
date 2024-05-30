package TI_TP3_A50299;

import java.util.Scanner;

public class TP3_03_EscreveDigitos {

	public static void main(String[] args) {
		/**Crie um programa (TP3-03-EscreveDigitos) que peça ao utilizador um número positivo, e que escreva por ordem os seus dígitos. 
		 * Por exemplo, para o número 2490 deverá escrever “dois quatro nove zero”. 
		 * Deverá implementar os seguintes métodos: 
		 * String getDigitoEmString(int digito) que recebe um digito em inteiro e retorna a sua representação da forma “zero”, “um”, “dois” até “nove”; 
		 * int getDigito(int n, int i) que retorna o i-ésimo digito do número n, em que zero é o dígito mais à direita (de menor peso); 
		 * int getNumDigitos(int n) que retorna o número de dígitos de n; 
		 * String mostraDigitos(int n) que recebe o número n e retorna uma string com os seus dígitos por extenso.
		 */
		
		System.out.println("..::TP3-03-EscreveDigitos::..");
		int num;
		System.out.println("Introduza um número:");
		Scanner keyboard = new Scanner(System.in);
		num = keyboard.nextInt();
		System.out.print(mostraDigitos(num));
		keyboard.close();
	}
	
	public static String getDigitoEmString(int digito) {
		String digitoStr = "";
		
		switch (digito) {
		
		case 0:
			digitoStr = "zero";
			break;
		case 1:
			digitoStr = "um";
			break;
		case 2:
			digitoStr = "dois";
			break;	
		case 3:
			digitoStr = "três";
			break;	
		case 4:
			digitoStr = "quatro";
			break;
		case 5:
			digitoStr = "cinco";
			break;
		case 6:
			digitoStr = "seis";
			break;
		case 7:
			digitoStr = "sete";
			break;
		case 8:
			digitoStr = "oito";
			break;
		case 9:
			digitoStr = "nove";
			break;
		}
		return digitoStr;
	}
	
	public static int getNumDigitos(int n) {
		int ndigitos = 0;
		while(n > 0) {
			ndigitos++;
			n = n / 10;
		}
		return ndigitos;
	}
	
	public static int getDigito(int n, int i) {		
		int digito = 0;
		if(i == 0) {
			digito = n % 10;
		}
		else {
			for(i = 1; i <= getNumDigitos(n); i++)
			digito = n % 10;
			n = n / 10;
		}
		return digito;
	}
	
	public static String mostraDigitos(int n) {
		String mostraDigitos = "";
		if (getNumDigitos(n) > 0) {
			for(int i = getNumDigitos(n); i >= getNumDigitos(n); i--) {
				mostraDigitos += getDigitoEmString(getDigito(n, i)) + " ";	
			}	
		} 
		return mostraDigitos;
	}
}