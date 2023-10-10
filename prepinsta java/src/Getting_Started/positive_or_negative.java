package Getting_Started;

import java.util.Scanner;

public class positive_or_negative {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n==0){
            System.out.println("zero");
            return;
        }
        String res = n>0?"positive":"negative";
        System.out.println(res);
    }
}


