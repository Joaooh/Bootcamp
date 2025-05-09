import java.util.Scanner;

public class desafio3_contador {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Digite algo: ");
        String frase = scan.nextLine().toLowerCase();

        int vogais = 0;
        int consoantes = 0;
        String todasVogais = "aeiouáàãâéêíóôõú";

        for (int i = 0; i < frase.length(); i++) {
            char letra = frase.charAt(i);
            if (Character.isLetter(letra)) {
                if (todasVogais.indexOf(letra) != -1) {
                    vogais++;
                } else {
                    consoantes++;
                }
            }
        }
        System.out.println("Número de vogais: " + vogais);
        System.out.println("Número de consoantes: " + consoantes);
        scan.close();
    }
}