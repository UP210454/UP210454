from tkinter import *
from tkinter import messagebox


# Funciones

def bloquear():
    for i in range(0, 9):
        listaBotones[i].config(state="disable")


def comenzar(num):
    global turno
    if t[num] == "N" and turno == 0:
        listaBotones[num].config(text="X")
        listaBotones[num].config(bg="light green")
        t[num] = "X"
        turno = 1

    elif t[num] == "N" and turno == 1:
        listaBotones[num].config(text="O")
        listaBotones[num].config(bg="light blue")
        t[num] = "O"
        turno = 0

    listaBotones[num].config(state="disable")
    verificar()


def verificar():
    if (t[0] == "X" and t[1] == "X" and t[2] == "X") or (t[3] == "X" and t[4] == "X" and t[5] == "X") or (
            t[6] == "X" and t[7] == "X" and t[8] == "X"):
        bloquear()
        messagebox.showinfo("Ganaste", "Ganaste el juego X")
    elif (t[0] == "X" and t[3] == "X" and t[6] == "X") or (t[1] == "X" and t[4] == "X" and t[7] == "X") or (
            t[2] == "X" and t[5] == "X" and t[8] == "X"):
        bloquear()
        messagebox.showinfo("Ganaste", "Ganaste el juego X")
    elif (t[0] == "X" and t[4] == "X" and t[8] == "X") or (t[2] == "X" and t[4] == "X" and t[6] == "X"):
        bloquear()
        messagebox.showinfo("Ganaste", "Ganaste el juego X")
    elif (t[0] == "O" and t[1] == "O" and t[2] == "O") or (t[3] == "O" and t[4] == "O" and t[5] == "O") or (
            t[6] == "O" and t[7] == "O" and t[8] == "O"):
        bloquear()
        messagebox.showinfo("Ganaste", "Ganaste el juego O")
    elif (t[0] == "O" and t[3] == "O" and t[6] == "O") or (t[1] == "O" and t[4] == "O" and t[7] == "O") or (
            t[2] == "O" and t[5] == "O" and t[8] == "O"):
        bloquear()
        messagebox.showinfo("Ganaste", "Ganaste el juego O")
    elif (t[0] == "O" and t[4] == "O" and t[8] == "O") or (t[2] == "O" and t[4] == "O" and t[6] == "O"):
        bloquear()
        messagebox.showinfo("Ganaste", "Ganaste el juego O")


def reiniciar():
    for i in range(0, 9):
        listaBotones[i].config(state="normal")
        listaBotones[i].config(bg="light grey")
        listaBotones[i].config(text=" ")
        t[i] = "N"


ventana = Tk()
ventana.title("Juego del gato")
ventana.geometry("370x450")
turno = 0

listaBotones = []
t = []

for i in range(0, 9):
    t.append("N")

boton0 = Button(ventana, width=9, height=3, command=lambda: comenzar(0))
boton0.place(x=50, y=50)
listaBotones.append(boton0)

boton1 = Button(ventana, width=9, height=3, command=lambda: comenzar(1))
boton1.place(x=150, y=50)
listaBotones.append(boton1)

boton2 = Button(ventana, width=9, height=3, command=lambda: comenzar(2))
boton2.place(x=250, y=50)
listaBotones.append(boton2)

boton3 = Button(ventana, width=9, height=3, command=lambda: comenzar(3))
boton3.place(x=50, y=150)
listaBotones.append(boton3)

boton4 = Button(ventana, width=9, height=3, command=lambda: comenzar(4))
boton4.place(x=150, y=150)
listaBotones.append(boton4)

boton5 = Button(ventana, width=9, height=3, command=lambda: comenzar(5))
boton5.place(x=250, y=150)
listaBotones.append(boton5)

boton6 = Button(ventana, width=9, height=3, command=lambda: comenzar(6))
boton6.place(x=50, y=250)
listaBotones.append(boton6)

boton7 = Button(ventana, width=9, height=3, command=lambda: comenzar(7))
boton7.place(x=150, y=250)
listaBotones.append(boton7)

boton8 = Button(ventana, width=9, height=3, command=lambda: comenzar(8))
boton8.place(x=250, y=250)
listaBotones.append(boton8)

reiniciar = Button(ventana, width=9, height=3, command=reiniciar, text="Reiniciar")
reiniciar.place(x=150, y=350)


ventana.mainloop()
