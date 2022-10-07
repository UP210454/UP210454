numero_binario=str(input("Introduce el numero binario"))
numero_decimal=0
for posicion, digito_string in enumerate(numero_binario[::-1]):
	numero_decimal += int(digito_string) * 2 ** posicion
print(f'El número binario {numero_binario} en sistema decimal es: {numero_decimal}.')