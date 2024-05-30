package TI_TP2_A50299;
import java.util.Scanner;

public class TP2_02_FormulaResolvente {

	public static void main(String[] args) {
		/** 2. Crie um programa (TP2-02-FormulaResolvente) que peça três números ao utilizador 
		 * e encontre os zeros da função ax2+bx+c, recorrendo à fórmula resolvente.
		 */
		
		System.out.println("TP2-02-FormulaResolvente");
		
		double a, b, c, d = 0, zero1 = 0, zero2 = 0;
		
		Scanner keyboard = new Scanner(System.in);
		
		System.out.println("Introduza o valor de (a):");
		
		a = keyboard.nextInt();
		
		System.out.println("Introduza o valor de (b):");
		
		b = keyboard.nextInt();
		
		System.out.println("Introduza o valor de (c):");
		
		c = keyboard.nextInt();
		
		d = (Math.pow(b, 2)) - (4.0 * a * c);
		
		if(d > 0.0) {
			zero1 =  (-b + Math.sqrt(d)) / (2 * a);
			zero2 =  (-b - Math.sqrt(d)) / (2 * a);	
			System.out.println("Os zeros da função (" + a + "x2 + " + b + "x + " + c + ") são: " + zero1 + " e " + zero2 + ".");
					
		}
		
		else if (d==0.0) {
			zero1 = (- b) / (2 * a );
			System.out.println("O zero da função (" + a + "x2 + " + b + "x + " + c + ") é: " + zero1 + ".");
		}
		
		else {
			System.out.println("Os zeros da função (" + a + "x2 + " + b + "x + " + c + ") não são reais.");
			
		}

		keyboard.close();
		
	}
}