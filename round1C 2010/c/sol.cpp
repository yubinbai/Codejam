#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;
int mat[600][600];

int ID(char ch)
{
    if (ch >= '0' && ch <= '9')return ch - '0';
    else if (ch >= 'A' && ch <= 'F')return ch - 'A' + 10;
}

bool check(int x, int y, int len)
{
    int i, j;
    for (i = x; i < x + len; i++)
        for (j = y; j < y + len; j++)
        {
            if (mat[i][j] == -1)return false;
            if (i > x && mat[i][j] == mat[i - 1][j])return false;
            if (j > y && mat[i][j] == mat[i][j - 1])return false;
        }
    return true;
}
void mark(int x, int y, int len)
{
    int i, j;
    for (i = x; i < x + len; i++)
        for (j = y; j < y + len; j++)
            mat[i][j] = -1;
}
int min(int a, int b)
{
    return a < b ? a : b;
}
main()
{

    freopen("C-large-practice.in", "r", stdin);
    freopen("C-large-practice.out", "w", stdout);
    int T;
    scanf("%d", &T);


    for (int Case = 1; Case <= T; Case++)
    {
        int N, M;
        scanf("%d %d", &M, &N);
        memset(mat, -1, sizeof(mat));
        char str[150];
        int i = 0, j = 0;
        for (i = 0; i < M; i++)
        {
            scanf("%s", str);
            for (j = 0; j < N / 4; j++)
            {
                char ch = str[j];
                int num = ID(ch);
                for (int k = 3; k >= 0; k--)
                    mat[i][j * 4 + (3 - k)] = ((num >> k) & 1);
            }
        }

        int ret[600];
        memset(ret, 0, sizeof(ret));
        int len = min(M, N);
        for (; len > 0; len--)
        {
            for (i = 0; i < M; i++)
                for (j = 0; j < N; j++)
                    if (i + len <= M && j + len <= N)
                    {
                        if (check(i, j, len))
                        {
                            ret[len]++;
                            mark(i, j, len);
                        }
                    }
        }
        int num = 0;
        for (i = 0; i < 600; i++)if (ret[i] != 0)num++;

        printf("Case #%d: %d\n", Case, num);
        for (i = min(N, M); i > 0; i--)
        {
            if (ret[i] != 0)
                printf("%d %d\n", i, ret[i]);
        }
    }
}
