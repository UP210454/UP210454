respuesta=1
while respuesta!=2:
    opcion=int(input("Que operacion quieres realizar?\n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division\n5.-Salir\n"))
    if opcion==1:
        num1=int(input("Introduce el primero numero: "))
        num2=int(input("Introduce el segundo numero: "))
        resultado=num1+num2
        print(f"{num1} + {num2} = {resultado}")
        respuesta = int(input("Quieres volver a realizar una operacion?\n1.-Si\n2.-No\n"))
    if opcion==2:
        num1 = int(input("Introduce el primero numero: "))
        num2 = int(input("Introduce el segundo numero: "))
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
        respuesta = int(input("Quieres volver a realizar una operacion?\n1.-Si\n2.-No\n"))
    if opcion==3:
        num1 = int(input("Introduce el primero numero: "))
        num2 = int(input("Introduce el segundo numero: "))
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
        respuesta = int(input("Quieres volver a realizar una operacion?\n1.-Si\n2.-No\n"))
    if opcion==4:
        num1 = int(input("Introduce el primero numero: "))
        num2 = int(input("Introduce el segundo numero: "))
        if num2!=0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
            respuesta = int(input("Quieres volver a realizar una operacion?\n1.-Si\n2.-No\n"))
        else:
            print("No se puede dividir entre 0")
    elif opcion==5:
        print("Gracias, vuelva pronto")
        break