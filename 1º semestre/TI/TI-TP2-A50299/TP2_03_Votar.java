package TI_TP2_A50299;
import java.util.Scanner;

public class TP2_03_Votar {
	
	public static void main(String[] args) {
		/** 3. Implemente um programa (TP2-03-Votar) que peça o nome do utilizador e o seu ano de nascimento. 
		 * O programa deverá validar se o utilizador é maior de idade e se pode votar ou não.
		 * O programa deverá informar “O ABC pode votar” ou “O ABC não pode votar”
		 * , em que “ABC” deverá ser substituído pelo nome do utilizador.
		 */
		
		//nome do programa
		System.out.println("..::TP2_03_Votar::..");
		
		//declaração de variáveis
		String nome;
		int ano, idade;
		
		//the keyboard reader
		Scanner keyboard = new Scanner(System.in);
		
		//pedir o nome ao utilizador
		System.out.println("Qual o seu nome?");
		nome = keyboard.nextLine();
		
		//pedir o ano de nascimento ao utilizador
		System.out.println("Em que ano nasceu?");
		ano = keyboard.nextInt();
		
		//cálculo da idade
		idade = 2022 - ano;
		
		//validar se o utilizador é maior de idade e se pode votar ou não
		if (idade >= 18)
			System.out.println("O/A " + nome + " pode votar.");
		else 
			System.out.println("O/A " + nome + " não pode votar.");
		
		//close the keyboard
		keyboard.close();
		
	}
}