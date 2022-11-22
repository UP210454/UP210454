n = int(input("Cuantos numeros vas a meter en el vector: "))
vector = []
for i in range(1,n+1):
    num = int(input(f"Introduce el {i} numero: "))
    vector.append(num)
vector = sorted(vector)

print("El vector ordenado es: ", vector)