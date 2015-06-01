package qualification;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.math.BigDecimal;
import java.math.MathContext;
import java.util.Scanner;

/**
 * Created by yubin on 4/11/14.
 */
public class Problem2_2 {

    public static void main(String[] args) {
        int[][] first = new int[4][4];
        int[][] second = new int[4][4];
        int firstRow, secondRow;

        try {
            Scanner sc = new Scanner(new File("input.in"));
            PrintWriter writer = new PrintWriter("output.out");
            int T = sc.nextInt();
            for (int caseNo = 1; caseNo <= T; caseNo++) {
                BigDecimal c, f, x, speed, speed2;
                c = BigDecimal.valueOf(sc.nextDouble());
                f = BigDecimal.valueOf(sc.nextDouble());
                x = BigDecimal.valueOf(sc.nextDouble());
                speed = BigDecimal.valueOf(2.0);
                BigDecimal t1, t2, delta, total = BigDecimal.ZERO;
                while (true) {
                    t1 = x.divide(speed, MathContext.DECIMAL128);
                    speed2 = speed.add(f);
                    t2 = x.divide(speed2, MathContext.DECIMAL128);
                    t2 = t2.add(c.divide(speed, MathContext.DECIMAL128));
                    delta = c.divide(speed, MathContext.DECIMAL128);
                    if (delta.compareTo(BigDecimal.valueOf(1e-9)) <= 0) break;
                    if (t1.compareTo(t2) > 0) {
                        speed = speed2;
                        total = total.add(delta);
                    } else {
                        total = total.add(t1);
                        break;
                    }
                }
                writer.format("Case #%d: %.7f\n", caseNo, total.doubleValue());
            }
            writer.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

    }
}
