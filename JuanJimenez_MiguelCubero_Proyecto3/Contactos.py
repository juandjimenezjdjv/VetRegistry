from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def abri_cont(): #Esta funcion se encarga del apartado de contacto
    v_contacto = Tk()#Falta hacer que se guarde en un lista en memoria (pero ya se hace el .txt)
    v_contacto.title("Informacion de contacto.")
    v_contacto.geometry("400x200")
    v_contacto.lift()
    
    def save(): #Esta se encarga de guardar los datos de contacto en un .txt
        v_contacto.lift()
        nombre = nombre_entry.get()
        correo = correo_entry.get()
        hola=True
        while hola:
            try:
                telefono = telefono_entry.get()
                telefono= int(telefono)
                hola=False
            except ValueError:
                messagebox.showerror(title="Ooops", message="Asegurese de que agregar un telefono correcto")
                v_contacto.destroy()
                abri_cont()
        if len(nombre)==0 or len(correo)==0:
            messagebox.showerror(title="Ooops", message="Asegurese de llenar todos los campos")
            v_contacto.lift()
        elif "@" not in correo:
            messagebox.showerror(title="Ooops", message="Asegurese de que agregar un correo correcto")
            v_contacto.lift()
        else:
            is_ok = messagebox.askokcancel(title="Esta seguro de agregar los datos?", message=f"Estos fueron los datos de contacto dados: \nNombre: {nombre} \nEmail/Correo: {correo}\nTelefono: {telefono} \nLos va salvar?")
            if is_ok:
                with open("Contactos.txt", "a") as data_file:
                    data_file.write(f"{nombre} | {correo} | {telefono}\n")
                    nombre_entry.delete(0, END)
                    correo_entry.delete(0, END)
                    telefono_entry.delete(0, END)
                v_contacto.destroy()
    
    Agregar_label = Label(v_contacto,text="Agregue su informacion de contacto")
    Agregar_label.grid(row=0, column=1)
    #Labels contacto
    nombre_label = Label(v_contacto,text="Nombre:")
    nombre_label.grid(row=1, column=0)
    correo_label = Label(v_contacto,text="Email/Correo:")
    correo_label.grid(row=2,column=0)
    telefono_label = Label(v_contacto,text="Telefono:")
    telefono_label.grid(row=3,column=0)
    #Entrys contacto
    nombre_entry=Entry(v_contacto,width=35)
    nombre_entry.grid(row=1,column=1,columnspan=2)
    nombre_entry.focus()
    correo_entry=Entry(v_contacto,width=35)
    correo_entry.grid(row=2,column=1,columnspan=2)
    correo_entry.insert(0, "example@e-mail.com")
    telefono_entry=Entry(v_contacto,width=35)
    telefono_entry.grid(row=3,column=1)
    #Buttons contacto
    add=Button(v_contacto, text="Agregar", width=35,command=lambda:save())
    add.grid(row=5,column=1)
    cerrar=Button(v_contacto, text="Cerrar", width=35,command=lambda:v_contacto.destroy())
    cerrar.grid(row=6,column=1)
    
    v_contacto.mainloop()
