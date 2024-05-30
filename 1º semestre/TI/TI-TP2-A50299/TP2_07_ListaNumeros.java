package TI_TP2_A50299;
import java.util.Scanner;

public class TP2_07_ListaNumeros {

	public static void main(String[] args) {
		/** 7. Implemente o programa (TP2-07-ListaNumeros) que peça dois números ao utilizador e uma das seguintes strings (“par”, “impar”, “todos”). 
		 * Caso o utilizador escolha “par”, o programa deverá mostrar todos os números pares entre os números introduzidos. 
		 * Se escolher “impar”, lista apenas os impares, e se escolher “todos”, deverá listar todos os números entre os dois introduzidos.
		 */
		
		//nome do programa
		System.out.println("..:: TP2-07-ListaNumeros ::..");
		
		//declarar variáveis
		int num1, num2;
		String opcao;
		
		//the keyboard reader
		Scanner keyboard = new Scanner(System.in);
		
		//pedir dados ao utilizador
		System.out.println("Qual o valor mais baixo do intervalo?");
		num1 = keyboard.nextInt();
		
		System.out.println("Qual o o valor mais alto do intervalo?");
		num2 = keyboard.nextInt();
		
		System.out.println("Par, impar ou todos?");
		opcao = keyboard.next();
		
		
		//todos 
		if(opcao.equals("todos")) {
			
			System.out.print("Os números entre o intervalo introduzido são: [");
			
			while (num1 <= num2 ) {
				
				System.out.print(num1 + (num1 != num2 ? ", " : ""));	
				
				num1++;
							
			}	
			
			System.out.print("].");
		}
		
		//par
		if(opcao.equals("par")) {
			
			System.out.print("Os números pares entre os números introduzidos são: [");
			
			for (int i = num1; i <= num2; i++) {
				
				if (i % 2 == 0) {
					
				System.out.print(i + (i != num2 - 1 ? ", " : ""));			
				
				}
			}
			
			System.out.print("].");
		}
		
		//impar
		if(opcao.equals("impar")) {
			
			System.out.print("Os números impares entre os números introduzidos são: [");
			for (int i = num1; i <= num2; i++) {
				
				if (i % 2 != 0) {
					
				System.out.print(i + (i != num2? ", " : ""));			
				
				}
			}
			
			System.out.print("].");
		}
		
		//close the keyboard
		keyboard.close();
	}
}