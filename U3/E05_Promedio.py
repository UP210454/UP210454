promedio = []
n=int(input("Introduce el total de calificaciones: "))
for i in range(1, n+1):
    calificacion = int(input(f"Introduce la calificación {i}: "))
    promedio.append(calificacion)
promedio = sum(promedio)
promediofinal = promedio/n
print(f'El promedio es {promediofinal}')
