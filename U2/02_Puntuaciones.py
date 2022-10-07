multiplicacion=float
nivel=str
puntuacion=float(input("Introduce la puntuación del empleado: "))
if puntuacion==0.0:
    multiplicacion=2400*0.0
    nivel='Inaceptable'
    print(f'El empleado recibirá ${multiplicacion} y su nivel es {nivel}.')
elif puntuacion==0.4:
    multiplicacion=2400*0.4
    nivel='Aceptable'
    print(f'El empleado recibirá ${multiplicacion} y su nivel es {nivel}.')
elif puntuacion>=0.6:
    multiplicacion=2400*0.6
    nivel='Meritorio'
    print(f'El empleado recibirá ${multiplicacion} y su nivel es {nivel}.')
else:
    print("Valor no válido")