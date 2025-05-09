import java.util.Scanner;

public class soma_facil {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int soma = A + B;
        
        System.out.print(soma);
        sc.close();
    }
}