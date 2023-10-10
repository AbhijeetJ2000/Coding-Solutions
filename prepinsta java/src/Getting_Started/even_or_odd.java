package Getting_Started;

import java.util.Scanner;

public class even_or_odd {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String ans = (n%2==0)?"Even":"Odd";
        System.out.println(ans);
    }
}


