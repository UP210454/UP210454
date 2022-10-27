from tkinter import *

ventana1=Tk()
ventana1.title("Iniciar sesión")
ventana1.geometry("400x600")

nombre=Label(ventana1,text="Nombre de usuario",font="Calibri 15")
nombre.grid(row=0,column=0)

e_nombre=Entry(ventana1,font="Calibri 15")
e_nombre.grid(row=1,column=0)

contraseña=Label(ventana1,text="Contraseña",font="Calibri 15")
contraseña.grid(row=2,column=0)

e_contraseña=Entry(ventana1,font="Calibri 15")
e_contraseña.grid(row=3,column=0)

boton1=Button(ventana1,text="Iniciar sesión",font="Calibri 15")
boton1.grid(row=4,column=0)

ventana1.mainloop()