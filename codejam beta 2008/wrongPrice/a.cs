#include <cstdlib>

#include <iostream>

#include <algorithm>

#include <cstring>

#include <string>



using namespace std;

struct Prod{

       char name[30];

       int id;

}prod[64], temp[64];

int ord[64];

int price[64];




int Compare(const void* p1, const void*p2)

{

    Prod *a1 = (Prod*) p1, *a2 = (Prod*)p2;

    return strcmp(a1->name, a2->name);

}



string mins[64][102];

bool m[64][102];



string Minchg(int n, int max)

{

       if (m[n][max]) return mins[n][max];

       char c = ord[n];

       if (n == 0)

       {

             string res;

             if (price[0] >= max) res.append(1, c);

             m[n][max] = true;

             mins[n][max] = res;

             return res;

       }

       //改变当前位的价格

       string a = Minchg(n-1, max);

       a.append(1, c);

       sort(a.begin(), a.end());

       if (price[n] < max)

       {

          string b = Minchg(n-1, price[n]);

          if (b.length() < a.length() || (b.length() == a.length() && b < a ))

             a = b;

       }

       m[n][max] = true;

       mins[n][max] = a;

       return a;

}



int main(int argc, char *argv[])

{

    int n;

    cin>>n;

    for (int i = 0; i < n; i++)

    {

        int size=0;

        while(1) 

        {

            cin>>prod[size].name;

            prod[size].id = size++;

            if (cin.get()=='/n') break;

        }

        for (int j = 0; j < size; j++) cin>>price[j];

        qsort(prod, size, sizeof(Prod), Compare);        

        for (int j = 0; j < size; j++)

          ord[prod[j].id] = j;

        memset(m, false, sizeof(m));

        string res = Minchg(size-1, 101);

        cout<<"Case #"<<i+1<<":";

        for (int j = 0; j < res.length(); j++)

          cout<<" "<<prod[res[j]].name;

        cout<<endl;

    }

}

