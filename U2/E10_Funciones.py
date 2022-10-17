def alcuadrado():
    cuadrado=i**2
    print(f'El cuadrado de {i} es {cuadrado}')
def alcubo():
    cubo=(i**3)
    print(f'El cubo de {i} es {cubo}')

i=int(input("Introduce el numero que quieras saber su cuadrado: "))
alcuadrado()
alcubo()

def sumatoria():
    i = 1
    sumatoria = 0
    while i != 11:
        sumatoria = sumatoria + i
        i += 1
    print(f"La sumatoria es: {sumatoria}")
sumatoria()

def factorial():
    from math import factorial
    numero = int(input("Dame el numero del factorial que quieres saber:\n"))
    print(f"El factorial de {numero} es:", factorial(numero))
factorial()