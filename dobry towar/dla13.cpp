#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
#include <string>
#include <math.h>


using namespace std;

int main()
{

string wiadomosc="";
ifstream in("messages7.txt");

int dlugosc, liczba_wiad, liczba_znieksztalcen;


for(int ii=0;ii<23;ii++)
{
    in>>wiadomosc;

    if(0==ii)
    {
        dlugosc=stoi(wiadomosc);
        continue;
    }
    else if(1==ii)
    {
        liczba_wiad=stoi(wiadomosc);
        continue;
    }
    else if(2==ii)
    {
        liczba_znieksztalcen=stoi(wiadomosc);
        continue;
    }
    int wiad_len=wiadomosc.length();
    //int tabWiad[wiadomosc.length()]={};
    int tabWiad[wiad_len]={};

    for(int jj=0;jj<wiadomosc.length();jj++)
    {

            char s = wiadomosc[jj];
            tabWiad[jj] = s - '0';

    }


    //int tabWiad[64]={0,0,0,0,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0};

    int tabROB[64]={};
    int tabODP[64]={};
    int tabODP_Ald[7]={};
    int tabWzor[7]={};
    int tabWart[6]={};
    int a=6;
    int b=0;
    int c=5;
    int d=0;
    int rob=0;
    int ile=64;

    for(int i=0;i<128;i++)
    {
        if(0==i)
            {
            for(int x=0;x<8;x++)
                {
                    tabWzor[x]=0;
                }
            }
            b=i;
        while(b>0)
        {
            tabWzor[a]=b%2;
            b/=2;
            a--;

        }
        a=6;


        for(int j=0;j<64;j++)
        {
                if(0==j)
                {
                    for(int x=0;x<8;x++)
                    {
                        tabWart[x]=0;
                    }
                }

            d=j;
            while(d>0)
            {
                tabWart[c]=d%2;
                d/=2;
                c--;
            }

            c=5;

            tabROB[j]=tabWart[0];

            for(int x=1;x<6;x++)
            {
                tabROB[j]=tabROB[j]^tabWart[x];
            }

            tabROB[j]=!tabROB[j];
            if(0==tabWzor[0]) tabROB[j]=!tabROB[j];

            for(int x=1;x<7;x++)
            {
                if(0==tabWzor[x]) tabROB[j]=tabROB[j]^tabWart[x-1];
            }

        }

        /*for(int k=0;k<64;k++)
        {
            cout<<tabROB[k];
        }*/
        for(int e=0;e<64;e++)
            {
                if(tabWiad[e]!=tabROB[e]) rob++;

            }
       //cout<<" Liczba zmienionych bitow to: "<<rob<<"\n";
        if(rob<ile)
            {
                ile=rob;
            for(int f=0;f<64;f++)
                {
                    tabODP[f]=tabROB[f];
                }
                for(int f=0;f<7;f++)
                {
                    tabODP_Ald[f]=tabWzor[f];
                }
            }
            rob=0;

    }
    //cout<<endl;
    for(int i=0;i<64;i++)
    {
        cout<<tabODP[i];
    }
    //cout<<"   Wiadomosc aldony to: ";

    for(int i=0;i<7;i++)
    {
       // cout<<tabODP_Ald[i];
    }
    cout<<" "<<ile<<endl;

}

in.close();
    return 0;
}
