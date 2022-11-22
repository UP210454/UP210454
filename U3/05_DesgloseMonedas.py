dinero = int(input("Introduce el total de dinero\n"))
lista = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
for i in lista:
    if dinero >= i:
        restante = dinero//i
        print(str(restante) + (' billete' if dinero >= 20 else ' moneda') + ('s' if restante > 1 else ' ') + " de " + str(i) + " pesos")
        dinero = dinero % i