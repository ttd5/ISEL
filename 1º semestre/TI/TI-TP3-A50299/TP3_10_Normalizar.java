package TI_TP3_A50299;

import java.util.Scanner;
public class TP3_10_Normalizar {
/**Crie o programa (TP3-10-Normalizar) que implemente o método String normalizar(String str) para normalizar nomes de uma forma recursiva. 
		 * Para a resolução do problema deverá assumir que qualquer nome a seguir a um (ou mais) espaços deverá começar por um caracter maiúsculo seguido de vários caracteres minúsculos. 
		 * Ignore os casos especiais como “de”, “das”, “e”, etc. 
		 * Como exemplo, o nome “aníbal santos” (com um ou mais espaços entre os dois nomes) deverá retornar “Aníbal Santos”. 
		 * Note que poderá ter que incluir um espaço antes da primeira palavra para que o algoritmo recursivo a consiga detectar e normalizar.
		 */
	public static void main(String[] args) {
		System.out.println("..::TP3-10-Normalizar::..");
		String palavra;
		System.out.println("Introduza um nome:");
		Scanner keyboard = new Scanner(System.in);
		palavra = keyboard.nextLine();
		System.out.print("O nome normalizado fica:"
				+ "" + normalizar(palavra));
		keyboard.close();
	}
	
	public static String normalizar(String str) {
		if (str.length() == 0) return "";
		String c = str.substring(0, 1);
		if(str.length() > 0 && c.equals(" ")) return str.substring(0,2).toUpperCase() + normalizar(str.substring(2) + "");
		if(str.length() > 0) return c.toLowerCase() + normalizar(str.substring(1));
		return "";
						
	}
}