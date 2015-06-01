#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include "memory.h"
using namespace std;

#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))
typedef long long ll;

int nhand, ndeck, n;
int draw[80], score[80], turns[80];

int best0[81][81];
int mem[81][81][81][81];

int go(int next1, int next2, int pos, int t, int d)
{
    if (t == 0) return 0;

    int extra = 0;
    while (d > 0 && pos < n)
    {
        if (turns[pos] > 0)
        {
            d += draw[pos];
            extra += score[pos];
            t += turns[pos] - 1;
        }
        --d; ++pos;
    }

    while (next1 < pos && (turns[next1] > 0 || draw[next1] != 1)) ++next1;
    while (next2 < pos && (turns[next2] > 0 || draw[next2] != 2)) ++next2;
    t = min(t, n);

    int &ret = mem[next1][next2][pos][t];
    if (ret == -1)
    {
        ret = best0[pos][min(pos, t)];
        if (next1 < pos) ret = max(ret, score[next1] + go(next1 + 1, next2, pos, t + turns[next1] - 1, draw[next1]));
        if (next1 < pos) ret = max(ret, go(next1 + 1, next2, pos, t, 0));
        if (next2 < pos) ret = max(ret, score[next2] + go(next1, next2 + 1, pos, t + turns[next2] - 1, draw[next2]));
        if (next2 < pos) ret = max(ret, go(next1, next2 + 1, pos, t, 0));
    }
    return ret + extra;
}

void check(int expect)
{
    int s = 0, t = 1, d = nhand, pos = 0;
    vector<int> zero, one;
    int ret = 0;
    while (t > 0)
    {
        while (d > 0 && pos < n)
        {
            if (turns[pos] > 0)
            {
                s += score[pos];
                t += turns[pos] - 1;
                d += draw[pos];
            }
            else if (draw[pos] == 0) zero.PB(score[pos]); else one.PB(score[pos]);
            --d; ++pos;
        }
        sort(zero.begin(), zero.end());
        sort(one.begin(), one.end());
        int cur = s; for (int i = 0; i < t && i < SZ(zero); ++i) cur += zero[SZ(zero) - i - 1]; if (cur > ret) ret = cur;
        if (SZ(one) == 0) break;
        s += one.back(); t--; d += 1; one.pop_back();
        if (s > ret) ret = s;
    }
    if (ret != expect)
    {
        printf("%d\n", nhand);
        REP(i, nhand) printf("%d %d %d\n", draw[i], score[i], turns[i]);
        printf("%d\n", ndeck);
        FOR(i, nhand, n) printf("%d %d %d\n", draw[i], score[i], turns[i]);
        printf("!!!!! %d vs %d\n", ret, expect);
        exit(0);
    }
}

void run(int casenr)
{
    scanf("%d", &nhand);
    REP(i, nhand) scanf("%d%d%d", &draw[i], &score[i], &turns[i]);
    scanf("%d", &ndeck);
    REP(i, ndeck) scanf("%d%d%d", &draw[nhand + i], &score[nhand + i], &turns[nhand + i]);
    n = nhand + ndeck;

    //  printf("pos=%d turns=%d score=%d\n",pos,t,s);

    REPE(i, n)
    {
        vector<int> have; REP(j, i)
        if (turns[j] == 0 && draw[j] == 0)
            have.PB(score[j]);
        sort(have.rbegin(), have.rend());
        best0[i][0] = 0;
        FORE(j, 1, i)
        {
            best0[i][j] = best0[i][j - 1] + (j - 1 < SZ(have) ? have[j - 1] : 0);
        }
    }

    memset(mem, -1, sizeof(mem));
    int ret = go(0, 0, 0, 1, nhand);
    printf("Case #%d: %d\n", casenr, ret);

    //check(ret);
}

int main()
{
    // freopen("input.txt", "r", stdin);
    freopen("C-small-practice.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n; scanf("%d", &n); FORE(i, 1, n) run(i);
    return 0;
}


