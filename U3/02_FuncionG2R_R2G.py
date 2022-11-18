def G2R(g):
    r = g * 3.1416 / 180
    print (r)

def R2G(r):
    g = r * 180 / 3.1416
    print (g)

g = int (input("Introduce el grado que quieras convertir: "))
G2R(g)

r = int (input("Introduce los radianes que quieres convertir: "))
R2G(r)
