temperaturas=[]
for i in range (1,7):
    temperatura=int(input(f"Dame la temperatura {i}\n"))
    temperaturas.append(temperatura)
temperaturas=sorted(temperaturas) #Se acomoda la lista

maximo=max(temperaturas)
minimo=min(temperaturas)
suma=sum(temperaturas)
promedio=suma/i

print (f'La temperatura minima es {minimo} y la temperatura maxima es {maximo}. El promedio de las temperaturas es: {promedio}')