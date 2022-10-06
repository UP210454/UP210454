/*  Unidad 1. Ciclos
    Autor: Luis Fernando de la Cruz Robledo
    Fecha: 20 de septiembre de 2022
    Descripción: Muestra la suma de numeros pares e impares
*/

#include <iostream>
#include <stdio.h>

using namespace std;
int main()
{
    int n = 10;
    int par=0;
    int impar=0;
    int suma = 0;

    /*for (int i = 1; i <= n; i++)
    {
        if (i != 3)
        {
            printf("Contador %d \n", i);
        }
        suma = suma + i;
    }
    printf("El resultado de la suma es %d", suma); */


    for (int j = 1; j<=n ; j++)
    {
        if (j%2==0){
            par=par+j;
        }
        else {
            impar=impar+j;
        }
    }

    printf("La suma de pares es: %d \n",par);
    printf("La suma de los impares es: %d \n",impar);
    int suma_total=par+impar;
    printf("La suma total es: %d \n", suma_total);
    return 0;
}