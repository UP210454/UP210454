def bisiesto(año):
    r = bool
    r = año % 400 == 0 or año % 4 == 0 and año % 100 != 0
    if r == True :
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")

año = int (input("Introduce el año que quieras saber: "))

bisiesto(año)
