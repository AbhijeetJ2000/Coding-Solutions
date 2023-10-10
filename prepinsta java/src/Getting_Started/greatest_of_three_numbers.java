package Getting_Started;

import java.util.Scanner;

public class greatest_of_three_numbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = 2, b = 5, c = 7;
        int ans = (a>b)? ((a>c)?a:c) : ((b>c)?b:c);
        System.out.println(ans);
    }
}

