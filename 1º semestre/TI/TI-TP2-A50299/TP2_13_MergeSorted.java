package TI_TP2_A50299;

import java.util.Arrays;

public class TP2_13_MergeSorted {

	public static void main(String[] args) {
		/** 13. Crie um programa (TP2-13-MergeSorted) que crie dois arrays ordenados (pode mesmo criá-los já ordenados no próprio código Java) 
		 * e faça a junção dos dois arrays num terceiro array, que deverá, por sua vez, também ficar ordenado. 
		 * Ex: Para os arrays A=[1, 3, 5, 6] e B=[1, 2, 4, 6], a junção dos arrays deverá resultar em [1, 1, 2, 3, 4, 5, 6, 6].
		 */

		//nome do programa
		System.out.println("..::TP2-13-MergeSorted::..");
		
		//criar arrays
		int array1[] = {1,3,5,6};
		System.out.println("Array1: " + Arrays.toString(array1));
        int array2[] = {1,2,4,6};
        System.out.println("Array2: " + Arrays.toString(array2));
        
        //criar novo array com a junção de ambos
        int length = array1.length + array2.length;

        int[] array3 =new int[length];
        
        for (int i = 0; i < array1.length; i = i + 1) {
            array3[i] = array1[i];
        }
        for (int i = 0; i < array2.length; i = i + 1) {
            array3[array1.length + i] = array2[i];
            
        }
        
        System.out.println("Array gerado: " + Arrays.toString(array3));
        
        //ordernar o array gerado
        
		for (int i = 0; i <array3.length; i++) {     
			for (int j = i+1; j <array3.length; j++) {     
				if(array3[i] >array3[j]) {      
					int aux = array3[i];    
	                array3[i] = array3[j];    
	                array3[j] = aux; 
	            }
	        }
		}
		System.out.println("Array gerado ordenado: " + Arrays.toString(array3));		

	}
}