op=1
while op==1:
    numero = int(input("Cuál tabla quieres saber? "))
    for i in range (1,11):
        multiplicacion=numero*i
        print(f'{numero} * {i} = {multiplicacion}')
    op=int(input("Quieres otra tabla? \n 1.-Si \n 2.-No \n"))