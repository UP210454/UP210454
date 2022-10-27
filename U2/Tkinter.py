import tkinter

ventana = tkinter.Tk() #Crear la ventana
ventana.geometry("300x300") #Tamaño de la ventana

def saludo(nombre):
    print("Hola " + nombre)

def texto():
    textoimpreso=caja.get()
    etiqueta2["text"]=textoimpreso

etiqueta=tkinter.Label(ventana,text="Hola mundo",background="blue") #Creacion de una etiqueta
etiqueta.pack() #Poner la etiqueta en la ventana SIDE=Acomodar la etiqueta FILL=Completar el eje y o x

boton1=tkinter.Button(ventana,text="Presiona",padx=40, command=lambda: saludo("python"))
boton1.pack()

caja=tkinter.Entry(ventana)
caja.pack()

boton2=tkinter.Button(ventana,text="Click",command=texto)
boton2.pack()

etiqueta2=tkinter.Label(ventana)
etiqueta2.pack()

ventana.mainloop()