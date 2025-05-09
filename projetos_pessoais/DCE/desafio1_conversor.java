import java.util.Scanner;

public class desafio1_conversor {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Digite a temperatura em Celsius: ");
        double celsius = scan.nextDouble();
        double fahrenheit = ((celsius * 9 / 5) + 32);

        System.out.printf("%.2f°C equivalem a %.2f°F.", celsius, fahrenheit);
        scan.close();
    }
}