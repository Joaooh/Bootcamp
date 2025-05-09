import java.util.Scanner;

public class media_inteira {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int soma = A + B;
        int media = soma / 2;
        
        System.out.print(media);
        sc.close();
    }
}