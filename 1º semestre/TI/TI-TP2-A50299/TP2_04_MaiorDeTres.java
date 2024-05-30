package TI_TP2_A50299;
import java.util.Scanner;

public class TP2_04_MaiorDeTres {

	public static void main(String[] args) {
		/** 4. Implemente um programa (TP2-04-MaiorDeTres) que peça ao utilizador três números 
		 * e mostre qual o número maior, o menor e o do meio. 
		 * Não trate de forma especial as situações em que possa haver números iguais.
		 */
		
		//nome do programa
		System.out.println("..::TP2-04-MaiorDeTres::..");
		
		//declaração de variáveis
		int num1, num2, num3, maior = 0, meio = 0, menor = 0;
		
		//the keyboard reader
		Scanner keyboard = new Scanner(System.in);
		
		//pedir três número ao utilizador
		System.out.println("Introduza o primeiro valor:");
		num1 = keyboard.nextInt();
		
		System.out.println("Introduza o segundo valor:");
		
		num2 = keyboard.nextInt();
		
		System.out.println("Introduza o terceiro valor:");
		
		num3 = keyboard.nextInt();
		
		//mostrar qual o número maior
		
		if (num1 > num2 && num1 > num3) {
	
			maior = num1;		
		}
		
		if (num2 > num1 && num2 > num3) {
			
			maior = num2;	
		
		}
		
		if (num3 > num1 && num3 > num2) {
			
			maior = num3;
		}
	
		System.out.println("O número maior é " + maior + ".");
		
		
		//mostrar qual o número do meio

		if ((num1 < num2 && num1 > num3) || (num1 > num2 && num1 < num3)) {
			
			meio = num1;		
		}
		
		if ((num2 < num1 && num2 > num3) || (num2 > num1 && num2 < num3)) {
			
			meio = num2;		
		}
		
		
		if ((num3 < num1 && num3 > num2) || (num3 > num1 && num3 < num2)) {
		
			meio = num3;
		}
	
		System.out.println("O número do meio é " + meio + ".");
		
		//mostrar qual o número menor
		
		if (num1 < num2 && num1 < num3) {
			
			menor = num1;	
		}
		
		if (num2 < num1 && num2 < num3) {
			
			menor = num2;	
		}
		
		if (num3 < num1 && num3 < num2) {
			
			menor = num3;

		}
	
		System.out.println("O número menor é " + menor + ".");
		
		//close the keyboard
		keyboard.close();
						
	}
}