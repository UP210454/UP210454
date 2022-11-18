def llenarMatriz(x,y):
    valor = 0
    for i in range(x):
        matriz.append([])
        for j in range(y):
            valor = valor + 1
            matriz[i].append(valor)
    return matriz

def printMatriz(x):
    for i in x:
        print("|\t", end=" ")
        for j in i:
            print("{}\t".format(j), end=" ")
        print("|\n")
    print("\n\n")

def diagonal(x,y):
    for i in range(x):
        print("|\t", end=" ")
        for j in range(y):
            if i==j:
                print(f"{matriz[i][j]}\t", end=" ")
            else:
                print("\t", end=" ")
        print("|")
    print("\n\n")

def Traspose(matrix):
    if matrix == None or len(matrix) == 0:
        return []

    result = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]

    for i in range(len(matrix[0])):
        print("|", end= ' ')
        for j in range(len(matrix)):
            print(f"{result[i][j]}\t", end=' ')
        print("|")
        print("\n")

matriz = []

filas = 4
columnas = 4

llenarMatriz(filas, columnas)
print("MATRIZ 4X4")
printMatriz(matriz)
print("RESULTADOS DE LA DIAGONAL")
diagonal(filas, columnas)
print("MATRIZ TRASPUESTA")
Traspose(matriz)