print("Introduce la edad")
edad=int(input(""))
if edad>0 and edad<=30:
    print("Primera edad")
elif edad>30 and edad<60:
    print("Segunda edad")
elif edad>60 and edad<90:
    print("Tercera edad")
else:
    print ("Horas extras")