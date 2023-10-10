package Getting_Started;

import java.util.Scanner;

public class greatest_of_two_nums {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int b = 15;
        int a = 12;
        int ans = (b>a)? b: a;
        System.out.println(ans);
    }
}

