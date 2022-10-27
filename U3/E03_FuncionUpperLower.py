def upper(x):
    mayuscula = cadena.upper()
    print(mayuscula)

def lower(x):
    minuscula = cadena2.lower()
    print(minuscula)

def invertir(x):
    invertido = cadena3.swapcase()
    print(invertido)

cadena = str(input("Introduce la palabra que quieres convertir a mayuscula: "))
cadena2 = str(input("Introduce la palabra que quieres convertir a minuscula: "))
cadena3 = str(input("Introduce la palabra que quieres invertir: "))

upper(cadena)
lower(cadena2)
invertir(cadena3)