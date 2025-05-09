import java.util.Scanner;

public class area_quadrado {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int L = sc.nextInt();

        int area = L * L;
        
        System.out.print(area);
        sc.close();
    }
}