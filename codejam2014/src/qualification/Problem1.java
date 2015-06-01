package qualification;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * Created by yubin on 4/11/14.
 */
public class Problem1 {

    public static void main(String[] args) {
        int[][] first = new int[4][4];
        int[][] second = new int[4][4];
        int firstRow, secondRow;

        try {
            Scanner sc = new Scanner(new File("input.in"));
            PrintWriter writer = new PrintWriter("output.out");
            int T = sc.nextInt();
            for (int caseNo = 1; caseNo <= T; caseNo++){
                firstRow = sc.nextInt() - 1;
                for (int i = 0;i< 4;i++)
                    for (int j = 0;j< 4;j++){
                        first[i][j] = sc.nextInt();
                    }
                secondRow = sc.nextInt() - 1;
                for (int i = 0;i< 4;i++)
                    for (int j = 0;j< 4;j++){
                        second[i][j] = sc.nextInt();
                    }
                int count = 0;
                int value = -1;
                for (int i = 0;i < 4;i++) {
                    int currV = first[firstRow][i];
                    for (int j = 0;j< 4;j++ ){
                        if (currV == second[secondRow][j]) {
                            count++;
                            value = currV;
                        }
                    }
                }
                if (count >= 2) {
                    writer.format("Case #%d: Bad magician!\n", caseNo);
                } else if (count == 0) {
                    writer.format("Case #%d: Volunteer cheated!\n", caseNo);
                } else {
                    writer.format("Case #%d: %d\n", caseNo, value);
                }
            }
            writer.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

    }
}
