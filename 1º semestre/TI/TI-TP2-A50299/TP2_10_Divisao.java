package TI_TP2_A50299;

import java.util.Scanner;

public class TP2_10_Divisao {

	public static void main(String[] args) {
		/**Implemente o programa (TP2-10-Divisao) que peça dois números inteiros positivos ao utilizador 
		 * e retorne a divisão inteira do primeiro número pelo segundo número usando apenas subtrações. 
		 * O programa deverá imprimir o resultado da divisão inteira e o resto da divisão.
		 */
		
		//nome do programa
		System.out.println("..::TP2-10-Divisao::..");
		
		//declaração de variáveis
		int num1, num2, resto = 0, resultado = 0;
		
		//the keyboard reader
		Scanner keyboard = new Scanner(System.in);
		
		//pedir os valores ao utilizador
		
		System.out.println("Introduza um valor inteiro para o Dividendo:");
		
		num1 = keyboard.nextInt();
		
		System.out.println("Introduza um valor inteiro para o divisor:");
		num2 = keyboard.nextInt();
		
		//cálculo da divisão
		
		int aux = num1;
		
		while (aux > 0) {
			
			aux = aux - num2;
			resultado++;
			resto = num1/(num1+aux);
		}
		
		//output do resultado ao utilizador

		System.out.println("A divisão de [" + num1 + "]" + " : " + "[" + num2 + "]" + " = " + resultado + ", e o resto da divisão é " + resto + ".");
		
		//close the keyboard
		keyboard.close();

	}
}