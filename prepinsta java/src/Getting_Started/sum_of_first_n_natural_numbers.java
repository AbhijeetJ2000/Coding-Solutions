package Getting_Started;

import java.util.Scanner;

public class sum_of_first_n_natural_numbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int ans = (int) n*(n+1)/2;
        System.out.println(ans);
    }
}


