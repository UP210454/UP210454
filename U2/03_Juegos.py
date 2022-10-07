edad=int(input("Introduce tu edad para saber el precio: "))
if edad>0 and edad<4:
    print ("Entrada gratis")
elif edad>=4 and edad<=18:
    print ("Entrada $5")
elif edad>18:
    print ("Entrada $10")
else:
    print ("Edad no válida")