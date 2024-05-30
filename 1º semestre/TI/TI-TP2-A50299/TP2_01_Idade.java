package TI_TP2_A50299;
import java.util.Scanner;

public class TP2_01_Idade {

	public static void main(String[] args) {
		
		/** 1. Implemente um programa (TP2-01-Idade) que peça o ano de nascimento ao utilizador 
		 * e calcule a sua idade com base no ano actual. 
		 */
		
		//nome do programa
		System.out.println("..::TP2-01-Idade::..");
		
		//declaração de variáveis
		int ano, idade;
		
		//the keyboard reader
		Scanner keyboard = new Scanner(System.in);
		
		//pedir o ano de nascimento ao utilizador
		
		System.out.println("Em que ano nasceu?");
		
		ano = keyboard.nextInt();
		
		//cálculo da idade
		idade = 2022 - ano;
		
		//output da idade ao utilizador
		System.out.println("Nasceu em " + ano + " e tem " + idade + " anos!");
		
		//close the keyboard
		keyboard.close();
	}
}