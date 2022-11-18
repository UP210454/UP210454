texto = []
cadena=str(input("Introduce la palabra: "))
longitud = len(cadena)
for i in range(longitud):
    texto.append(cadena[i])
print(texto)

texto2 = []
for i in range(longitud):
    if cadena[i]!='a' and cadena[i]!='e' and cadena[i]!='i' and cadena[i]!='o' and cadena[i]!='u':
        texto2.append(cadena[i])
print(texto2)

for i in range(longitud):
    mayus = texto2[i].upper()
    print(mayus)