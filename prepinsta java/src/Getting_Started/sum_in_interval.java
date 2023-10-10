package Getting_Started;
import java.util.Scanner;

public class sum_in_interval {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int b = 15;
        int a = 12;
        int ans = b*(b+1)/2 - a*(a+1)/2 + a;
        System.out.println(ans);
    }
}


