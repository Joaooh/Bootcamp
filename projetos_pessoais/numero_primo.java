import java.util.Scanner;

public class numero_primo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite um número: ");
        int numero = sc.nextInt();

        int cont = 0;
        for(int i = 1; i <= numero; i++){
            if(numero % i == 0){
                cont++;
            }
        }

        if(cont != 2){
            System.out.println("Não é primo");
        } else {
            System.out.println("É primo");
        }
        
        sc.close();
    }
}