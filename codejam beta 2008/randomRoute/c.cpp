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

map<string,int> mp;
int bian[100][3];
double d[1000];
double num[1000];
int shortest[1000];
int used1[1000];
int used[1000];
int zhan[1000];
double ans[1000];

int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int i,j,l,t,len,x1,x2,top,bottom,sx;
  char s[1000];
  string s1,s2,st;
  int min,max,tot,n,nn,bj;
  double tt;

  scanf("%d",&t);
  for (l=0;l<t;l++)
  {
    scanf("%d%s",&n,s);
    st=s;
    nn=0;
    mp.clear();
    for (i=0;i<n;i++)
    {
      scanf("%s",s);
      s1=s;
      scanf("%s",s);
      s2=s;
      scanf("%d",&len);
      if (mp.find(s1)!=mp.end()) x1=mp[s1];
      else
      {
        mp[s1]=nn;
        x1=nn;
        nn++;
      }
      if (mp.find(s2)!=mp.end()) x2=mp[s2];
      else
      {
        mp[s2]=nn;
        x2=nn;
        nn++;
      }
      bian[i][0]=x1;
      bian[i][1]=x2;
      bian[i][2]=len;
      ans[i]=0;
    }
    memset(used,0,sizeof(used));
    sx=mp[st];
    used[sx]=1;
    zhan[0]=sx;
    top=0;bottom=1;
    while (top<bottom)
    {
      for (i=0;i<n;i++)
        if ((bian[i][0]==zhan[top])&&(used[bian[i][1]]==0))
        {
          used[bian[i][1]]=1;
          zhan[bottom]=bian[i][1];
          bottom++;
        }
      top++;
    }
    tot=0;
    for (i=0;i<nn;i++)
      if ((used[i]==1)&&(i!=sx))
      {
        tot++;
      }
    for (i=0;i<nn;i++)
      if ((used[i]==1)&&(i!=sx))
      {
        for (j=0;j<nn;j++)
          shortest[j]=2000000000;
        shortest[i]=0;
        for (j=0;j<nn;j++)
          num[j]=0;
        num[i]=1;
        memset(used1,0,sizeof(used1));
        while (1)
        {
          min=2000000000;
          for (j=0;j<nn;j++)
            if ((used1[j]==0)&&(shortest[j]<min))
            {
              min=shortest[j];
              bj=j;
            }
          if (min==2000000000) break;
          used1[bj]=1;
          for (j=0;j<n;j++)
            if (bian[j][1]==bj)
            {
              if (shortest[bian[j][0]]>min+bian[j][2])
                shortest[bian[j][0]]=min+bian[j][2];
            }
          for (j=0;j<n;j++)
            if (bian[j][0]==bj)
            {
              if (min==shortest[bian[j][1]]+bian[j][2])
                num[bj]+=num[bian[j][1]];
            }
        }
        for (j=0;j<nn;j++) d[j]=0;
        d[sx]=1;
        memset(used1,0,sizeof(used1));
        for (j=0;j<nn;j++)
          if (shortest[j]>shortest[sx]) used1[j]=1;
        while (1)
        {
          max=-1;
          for (j=0;j<nn;j++)
            if ((used1[j]==0)&&(shortest[j]>max))
            {
              max=shortest[j];
              bj=j;
            }
          if (max==-1) break;
          used1[bj]=1;
          tt=0;
          for (j=0;j<n;j++)
            if (bian[j][0]==bj)
            {
              if (max-bian[j][2]==shortest[bian[j][1]]) tt+=num[bian[j][1]];
            }
          for (j=0;j<n;j++)
            if (bian[j][0]==bj)
            {
              if (max-bian[j][2]==shortest[bian[j][1]])
              {
                d[bian[j][1]]+=d[bj]/tt*num[bian[j][1]];
                ans[j]+=d[bj]/tt*num[bian[j][1]]/tot;
              }
            }
        }
      }
      printf("Case #%d:",l+1);
      for (i=0;i<n;i++)
        printf(" %.7lf",ans[i]);
      printf("\n");
  }
  return 0;
}

