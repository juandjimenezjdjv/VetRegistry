from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

def mostrar_empresa(VentanaPrincipal): #Esta se encarga de mostrar la informacion de la empresa
    v_empresa = Toplevel(VentanaPrincipal)
    v_empresa.title("Veterinaria la pulguita(Info)")
    v_empresa.geometry("400x400")
    v_empresa.lift()

    #Hacer con grids y poner Slogan, despues poner la info
    slogan = Label(v_empresa,text = "Slogan: ¡Nuestro sistema de gestión de registro es la mejor\n                manera de asegurar salud y felicidad a su mascota!")
    slogan.place(x= 10,y= 10)
    empresa = Label(v_empresa,text = "La empresa está conformada por:")
    empresa.place(x= 10,y= 50)
    emp1 = Label(v_empresa,text = "Miguel Cubero\n\nEstudiante del TEC.\n\nDesarrollador de la aplicacion para\nla veterinaria la pulgita")
    emp1.place(x= 10,y= 80)
    emp2 = Label(v_empresa,text = "Juan D. Jimenez\n\nEstudiante del TEC.\n\nDesarrollador de la aplicacion para\nla veterinaria la pulgita")
    emp2.place(x= 10,y= 220)

    juan = Image.open("imagenes/juan_perfil.jpg")
    juan = juan.resize((105, 100))
    juan_tk = ImageTk.PhotoImage(juan)
    etiqueta_juan = Label(v_empresa,image=juan_tk)
    etiqueta_juan.place(x=230, y=220)

    miguel = Image.open("imagenes/miguel_perfil.jpg")
    miguel = miguel.resize((105, 100))
    miguel_tk = ImageTk.PhotoImage(miguel)
    etiqueta_miguel = Label(v_empresa,image=miguel_tk)
    etiqueta_miguel.place(x=230, y=80)

    cerrar=Button(v_empresa, text="Cerrar", width=14,command=lambda:v_empresa.destroy())
    cerrar.place(x=230,y=340)
    v_empresa.mainloop()
