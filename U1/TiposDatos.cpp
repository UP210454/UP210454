/*  Unidad 1. Tipos de datos
    Autor: Luis Fernando de la Cruz Robledo
    Fecha: 15 de septiembre de 2022
    Descripción: Muestra los diferentes tipos de datos en C++
*/

#include <iostream>
#include <stdio.h>
#define pi 3.1416
const float PI=3.1415;

using namespace std;
int main(){
    int unsigned entero=31838472;
    float flotante=31416e-4;
    double grande=2.30050301030492921;
    char caracter=72;
    cout<<"Este programa muestra los tipos de datos. \n";
    cout<<"El numero entero es: "<< entero <<endl;
    cout<<"El tamaño del numero entero es: "<< sizeof(entero)<< " bytes"<<endl;
    cout<<"El numero flotante es: "<< flotante << endl;
    cout<<"El tamaño del numero flotante es: "<< sizeof(flotante)<< " bytes"<<endl;
    cout<<"El caracter char es: "<< caracter << endl;
    cout<<"El tamaño del char es: "<< sizeof(caracter)<<endl;
    cout<<"La variable constante pi vale: "<< pi <<endl;
    cout<<"La variable constante PI vale: "<< PI <<endl;
    getchar();
    system("pause");
    return 0;

}