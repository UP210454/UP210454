from math import factorial
numero=int(input("Dame el numero del factorial que quieres saber:\n"))
print(f"El factorial de {numero} es:", factorial(numero))

def fact(n):
    return 1 if (n==0 or n==1) else n * factorial(n-1)

print(f'El factorial de {numero} es ', fact(numero))