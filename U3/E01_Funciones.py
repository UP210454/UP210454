def doble(x):
    doble = num1+num1
    print (doble)

def sumatoria():
    sumatoria = 0
    for i in range (1,11):
        sumatoria = sumatoria + i
    print(sumatoria)

num1 = int(input("Dame un numero que quieras saber su doble: "))
doble(num1)

sumatoria()