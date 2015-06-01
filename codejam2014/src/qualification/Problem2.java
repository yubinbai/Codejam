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
public class Problem2 {
    public static BigDecimal solve(BigDecimal c, BigDecimal f, BigDecimal x, BigDecimal speed) {
        BigDecimal t1 = x.divide(speed, MathContext.DECIMAL128);
        BigDecimal speed2 = speed.add(f);
        BigDecimal t2 = x.divide(speed2, MathContext.DECIMAL128);
        t2 = t2.add(c.divide(speed, MathContext.DECIMAL128));
        if (t1.compareTo(t2) <= 0 || t1.compareTo(BigDecimal.valueOf(1e-9)) <= 0){
            return t1;
        } else {
            return Problem2.solve(c, f, x, speed2).add(c.divide(speed, MathContext.DECIMAL128));
        }
    }

    public static void main(String[] args) {
        int[][] first = new int[4][4];
        int[][] second = new int[4][4];
        int firstRow, secondRow;

        try {
            Scanner sc = new Scanner(new File("input.in"));
            PrintWriter writer = new PrintWriter("output.out");
            int T = sc.nextInt();
            for (int caseNo = 1; caseNo <= T; caseNo++){
                BigDecimal c, f, x;
                c = BigDecimal.valueOf(sc.nextDouble());
                f = BigDecimal.valueOf(sc.nextDouble());
                x = BigDecimal.valueOf(sc.nextDouble());

                writer.format("Case #%d: %.7f\n", caseNo, Problem2.solve(c, f, x, BigDecimal.valueOf(2.0)).doubleValue());
            }
            writer.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

    }
}
