precio=1
factura=0
while precio!=0:
    precio=int(input(f"Introduce el precio del producto:\n"))
    factura=factura+precio
print(f"El total de la factura es: {factura}")