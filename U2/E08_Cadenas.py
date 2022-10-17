cadena=str(input("Introduce la palabra que quieres deletrear: "))
contadori=0
contadorvocal=0
for i in cadena:
    print(i,end="\n")
    if i=="i":
        contadori=contadori+1
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        contadorvocal=contadorvocal+1

print(f'La palabra {cadena} tiene {contadori} i.')
print(f'La palabra {cadena} tiene {contadorvocal} vocal(es)')

texto = []
cadena2=str(input("Introduce la segunda palabra"))
longitud = len(cadena2)
for i in range(longitud):
    texto.append(cadena2[i])
print(texto)