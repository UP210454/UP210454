#include <iostream>
#include <cstring>
using namespace std;

int main(){
    string nombre;
    string AP;
    string AM;
    string fe;
    string rfc="";
    printf("Introduce el nombre: ");
    cin >> nombre;
    printf("Introduce el apellido paterno: ");
    cin >> AP;
    printf("Introduce el apellido materno: ");
    cin >> AM;
    printf("Introduce la fecha de nacimiento: ");
    cin >> fe;
    int v=nombre.length(); 
    int p=0;
    AP[0]=tolower(AP[0]);
    
    for (int i = 0; i < v && p<2; i++)
    {
        if (AP[i]=='a' || AP[i]=='e' || AP[i]=='i' || AP[i]=='o' || AP[i]=='u' )
        {
            rfc=rfc+AP[i];
            p++;
        }  
    }
    AP[0]=toupper(AP[0]);

    int d1=fe.find_last_of("/");
    int d2=fe.find("/");
    rfc=rfc+AM[0]+nombre[0]+fe.substr(d1+1,4)+fe.substr(d2+1,2)+fe.substr(0,2);
    
    v=rfc.length();
    for (int i = 0; i < v; i++)
    {
        rfc[i]=toupper(rfc[i]);
    }
    cout<<"El RFC de "<< nombre <<" es: "<< rfc;
    return 0;
}