import statistics

lista = []
numeros = int(input("Cuantos numeros vas a ingresar: "))
for i in range (numeros):
    num = int(input("Introduce el numero: "))
    lista.append(num)

desviacion = statistics.pstdev(lista)
print (f'La desviacion estandar es: {desviacion}')