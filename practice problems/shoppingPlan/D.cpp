//MADE BY lordmonsoon A.I.
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<sstream>
#include<iostream>
#include<utility>
#include<bitset>

using namespace std;

#define pi pair<int,int>
#define vi vector<int>
#define vpi vector<pi>
#define fst first
#define snd second
#define pb push_back
#define SIZE(a) (int)(a.size())
#define LENGTH(a) (int)(a.length())
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n);i>=0;i--)
#define FOR(i,n,m) for(int i=(n);i<=(m);i++)
#define FORD(i,n,m) for(int i=(n);i>=(m);i--)
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define ABS(a) ( (a)<0 ? -(a) : (a))
#define STRUMIEN(A,B) istringstream A(B)
#define SORT(A) sort(A.begin(),A.end())


////////////////////////////////////////////////////////////////////////////////

int t,n,m,c,p;
int dupa;
char bufor[10000];
char bufor2[10000];
char bufor3[10000];
map<string,int> M;

int G[55][16];
int T[55];
int X[55],Y[55];

double A[1<<16][55];

double dist(int a,int b)
{
      return c*sqrt( (X[a] - X[b])*(X[a] - X[b]) + (Y[a] - Y[b])*(Y[a] - Y[b]));
}

double gogo(int mask,int store)
{
      if(mask == 0) return dist(m,store);
      if(A[mask][store]<0.0)
      {
            A[mask][store] = 1e20;
            if((mask&dupa)==mask)
            {
                  //mozesz te glupie rzeczy
                  REP(i,m) if((mask&T[i])==mask)
                  {
                        double cost = dist(store,i) + dist(i,m);
                        REP(j,n) if(mask&(1<<j)) cost+=G[i][j];
                        A[mask][store] <?= cost;
                  }
            }
            else
            {
                  //wybierz sklep i jedna nieglupia rzecz ktora w nim kupisz
/*
                  REP(i,m)
                  {
                        REP(j,n) if(((mask&T[i])&(1<<j)) && !((1<<j)&dupa))
                        A[mask][store] <?= dist(i,store) + G[i][j] + gogo(mask - (1<<j),i);
                  }
*/
                  REP(j,n) if(((mask&T[store])&(1<<j)) && !((1<<j)&dupa))
                  {
                        REP(i,m) A[mask][store] <?= dist(i,store) + G[store][j] + gogo(mask - (1<<j),i);
                  }
            }
      }
      return A[mask][store];
}

double B[1<<15];

int main()
{
      freopen("input.txt","r",stdin);
      freopen("output.txt","w",stdout);
      scanf("%d",&t);
      FOR(tt,1,t)
      {
            scanf("%d %d %d",&n,&m,&c);
            REP(i,m+1) REP(j,n) G[i][j] = -1;
            REP(i,m+1) T[i] = 0;
            dupa = 0;
            M.clear();
//najglupsza rzecz wczytanie danych!!!
            REP(i,n)
            {
                  scanf("%s",bufor);
                  int len = strlen(bufor);
                  if(bufor[len-1] == '!') {dupa+=1<<i;bufor[len-1] = 0;}
                  M[string(bufor)] = i;
            }
            REP(j,m)
            {
                  scanf("%d %d ",X+j,Y+j);
                  gets(bufor);
                  int i = 0,len = strlen(bufor);
                  while(i<len)
                  {
                        int k = 0, off = 0;
                        while(i<len && bufor[i]!=' ') {bufor2[k++] = bufor[i];i++;}i++;
                        bufor2[k] = 0;
                        REP(s,k) if(bufor2[s]==':')
                        {
                              bufor2[s] = 0;
                              off = s+1;
                        }
                        sscanf(bufor2,"%s",bufor3);
                        sscanf(bufor2+off,"%d",&p);
                        G[j][M[string(bufor3)]] = p;
                        T[j] += 1<<M[string(bufor3)];
                  }
            }
//oblicz pojedyncze cykle
            Y[m] = X[m] = 0;
            REP(i,1<<n) REP(j,m+1) A[i][j] = -1.0;
            
            REP(i,m+1) A[0][i] = dist(i,m);
            FOR(i,1,(1<<n)-1) {A[i][m] = 1e100;REP(j,m) A[i][m] <?= dist(m,j) + gogo(i,j);}
//scal cykle
            B[0] = 0.0;
            FOR(i,1,(1<<n)-1)
            {
                  B[i] = 1e100;
                  int start=0;
                  while(start!=i)
                  {
                        start = ((start  | (~i))+1) & i;
                        B[i] <?= A[start][m] + B[i&(~start)];       
                  }            
            }       
            printf("Case #%d: %.7lf\n",tt,B[(1<<n)-1]);
      }
      return 0;
}
