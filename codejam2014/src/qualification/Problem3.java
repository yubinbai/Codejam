package qualification;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by yubin on 4/11/14.
 */
public class Problem3 {
    static char MINE = '*', PLAYER = 'c', EMPTY = '.';
    public static void main(String[] args) {

        try {
            Scanner sc = new Scanner(new File("input.in"));
            PrintWriter writer = new PrintWriter("output.out");
            int T = sc.nextInt();
            for (int caseNo = 1; caseNo <= T; caseNo++) {
                int r, c, m;
                r = sc.nextInt();
                c = sc.nextInt();
                m = sc.nextInt();

                boolean done = false;
                char[][] board = new char[r][c];
                for(int i=0; i<r; i++)
                    for(int j=0; j<c; j++)
                        board[i][j] = EMPTY;
                writer.format("Case #%d:\n", caseNo);
                if(m == r*c-1) {
                    for(char[] x : board) Arrays.fill(x, MINE);
                    board[0][0] = PLAYER;
                    done = true;
                }
                else if(r == 1 || c == 1) {
                    for(int i=r-1; i>=0; i--)
                        for(int j=c-1; j>=0; j--)
                            if(m --> 0)
                                board[i][j] = MINE;
                    board[0][0] = PLAYER;
                    done = true;
                }
                else {
                    for(int filledRows = 0; !done && filledRows <= r - 2; filledRows++) {
                        for(int filledCols = 0; !done && filledCols <= c - 2; filledCols++) {
                            int left = m - filledRows*c - filledCols*r + filledRows*filledCols;
                            if(left < 0) continue;
                            int leftRows = r-filledRows, leftCols = c-filledCols;
                            int playable = (leftRows-2)*(leftCols-2);
                            if(playable < left) continue;

                            board[0][0] = PLAYER;
                            for(int i=0; i<r; i++)
                                for(int j=0; j<c; j++)
                                    if(i >= leftRows || j >= leftCols)
                                        board[i][j] = MINE;
                            for(int i=leftRows-1; i>= 2; i--)
                                for(int j=leftCols-1; j >=2; j--)
                                    if(left-->0)
                                        board[i][j] = MINE;
                            done = true;
                        }
                    }
                }
                if(done) for(char[] x : board) writer.println(new String(x));
                else writer.println("Impossible");
            }
            writer.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

    }
}
