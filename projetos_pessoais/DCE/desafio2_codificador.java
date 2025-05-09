import java.util.Scanner;

public class desafio2_codificador {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Digite uma palavra: ");
        String palavra = scan.nextLine();

        char primeiraLetra = palavra.charAt(0);
        char ultimaLetra = palavra.charAt(palavra.length() - 1);
        int tamanho = palavra.length();

        System.out.printf("Mensagem codificada: %c %c %d%n", primeiraLetra, ultimaLetra, tamanho);
        scan.close();
    }
}