#include <iostream>
using namespace std;

int main(){
    cout <<"Abecedario"<<"\n";
    char letra=65;
    for (int i=0; i<26; i++){
        cout <<letra<<"\t";
        letra=letra+1;
    }
    cout <<"\nAbecedario al reves \n";
    char letra2='Z';
    for (int i=0; i<26; i++){
        cout <<letra2<<"\t";
        letra2=letra2-1;
    }
    cout <<"\nNumeros en orden ascendente \n";
    for (int j=1; j<=10; j++){
        cout<<j<<"\t";
    }
    cout <<"\nNumeros en orden descendente \n";
    for (int j=10; j>=1;j--){
        cout<<j<<"\t";
    }
}