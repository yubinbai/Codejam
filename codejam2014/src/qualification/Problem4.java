package qualification;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by yubin on 4/11/14.
 */
public class Problem4 {

    public static void main(String[] args) {

        try {
            Scanner sc = new Scanner(new File("input.in"));
            PrintWriter writer = new PrintWriter("output.out");
            int T = sc.nextInt();
            for (int caseNo = 1; caseNo <= T; caseNo++) {
                int N;
                N = sc.nextInt();
                double[] a = new double[N];
                double[] b = new double[N];
                for (int i =0;i<N;i++) a[i] = sc.nextDouble();
                for (int i =0;i<N;i++) b[i] = sc.nextDouble();
                Arrays.sort(a);
                Arrays.sort(b);

                int c = 0;
                for(int i = 0, j = 0; i<N && j < N;) {
                       if (a[i] > b[j]) {
                           c++;
                           i++;
                           j++;
                       } else {
                           i++;
                       }
                    }
                int cc = 0;
                for(int i = 0, j = 0; i <N && j < N ;) {
                    if (b[i] > a[j]) {
                        cc++;
                        i++;
                        j++;
                    } else {
                        i++;
                    }
                }
                cc = N - cc;
                writer.format("Case #%d: %d %d\n", caseNo, c, cc);
            }
            writer.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

    }
}
