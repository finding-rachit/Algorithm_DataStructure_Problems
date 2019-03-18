import java.util.*;


public class staircase {

    static void staircase(int n) {
        for (int i = 0; i < n; i++){
            int j = 0;
            int spaces = n - i - 1;

            while (j < spaces)
            {
                System.out.print(" ");
                j++;
            }
            j = 0;
            while (j <= i)
            {
                System.out.print("#");
                j++;
            }
            System.out.println();
        }

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        staircase(n);

        scanner.close();
    }
}
