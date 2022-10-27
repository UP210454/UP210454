from math import *
def fact(n):
    return 1 if (n==0 or n==1) else n * factorial(n-1)

def permutacion(n,r):
    permutacion=0
    permutacion=(fact(n))/(fact(n-r))
    return permutacion

def combinacion(n,r):
    combinacion=0
    combinacion=(permutacion(n,r))/fact(r)
    return combinacion

def euler():
    euler=0.0
    for i in range (0,30):
        euler=euler+(1.0/factorial(i))
    return euler

## numero =int(input("Introduce el numero"))
## print(f"El factorial del numero {numero} es ",factorial(numero))
print(f"El total de permutaciones de 5 y 2 es ",permutacion(5,2))
print(f'El total de combinaciones de 5 y 2 es ',combinacion(5,2))
print(f'El numero de euler es ',euler())