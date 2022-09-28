print("¿Cual es tu renta mensual?")
renta=int(input(""))
if renta<=10000:
    impuesto=0.05
elif renta>10000 and renta<=20000:
    impuesto=0.15
elif renta>20000 and renta<=35000:
    impuesto=0.20
elif renta>35000 and renta<=60000:
    impuesto=0.30
elif renta>60000:
    impuesto=0.45
total=renta*impuesto
sumatotal=total+renta
porcentaje = impuesto*100
print(f"El impuesto fue de: {porcentaje}%")
print(f"El total de impuestos es: {total}")
print(f"La suma total es: {sumatotal}")