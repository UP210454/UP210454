numero=int(input("Que tabla vas a querer? \n"))

print("Tabla en forma creciente")

for f in range(1, 11):
	multiplicacion = numero * f
	print(f'{numero} x {f} = {multiplicacion}')

print("Tabla en forma decreciente")

for f in range(10, 0, -1):
	multiplicacion=numero * f
	print(f'{numero} x {f} = {multiplicacion}')

print("Tabla usando while creciente")

m=1
while m<=10:
	multiplicacion=numero*m
	print(f'{numero} x {m} = {multiplicacion}')
	m+=1

print("Tabla usando while decreciente")

n=10
while n>=1:
	multiplicacion=numero*n
	print(f'{numero} x {n} = {multiplicacion}')
	n-=1