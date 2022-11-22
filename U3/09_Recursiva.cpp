#include <iostream>
using namespace std;

double factorial(int numero){
    if (numero == 1){
        return 1;
    }else{
        return numero*factorial(numero-1);
    }
}

int main(){
    int num, fact;
    printf ("Introduce el numero que quieras saber su factorial:\n");
    cin >> num;
    fact=factorial(num);
    cout<<"El factorial de " <<num<< " es " << fact;
}