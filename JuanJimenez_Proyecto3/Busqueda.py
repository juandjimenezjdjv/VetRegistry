from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import simpledialog
from tkinter import messagebox
from Funciones import *

def buscar(bscr,base):
    if bscr == 2:
        band = 0
        b_pais = base[0]
        a = True
        while a:
            cod_p = simpledialog.askfloat("Buscar Pais", "Por favor, ingresa un codigo de pais:")
            if type(cod_p)==float:
                cod = int(cod_p)
                a=False
            else:
                messagebox.showinfo("Error", "Debe escribir un codigo correcto.")
        for i in range(len(b_pais)):
            if cod == int(b_pais[i][0]):
                band = 1
                messagebox.showinfo("Buscar Pais", f"El codigo '{cod}' pertenece a {b_pais[i][1]}.")
        if band == 0:
            messagebox.showinfo("Error", f"El codigo '{cod}' no esta en lista de paises.")
    elif bscr == 3:
        band = 0
        b_ciudad = base[1]
        b_pais = base[0]
        a = True
        while a:
            cod_p = simpledialog.askfloat("Buscar Pais", "Por favor, ingresa un codigo de pais:")
            if type(cod_p)==float:
                cod_p = int(cod_p)
                a=False
            else:
                messagebox.showinfo("Error", "Debe escribir un codigo correcto.")
        a = True
        while a:
            cod = simpledialog.askfloat("Buscar Ciudad", "Por favor, ingresa un codigo de Ciudad:")
            if type(cod)==float:
                cod = int(cod)
                a=False
            else:
                messagebox.showinfo("Error", "Debe escribir un codigo correcto.")
        for i in range(len(b_ciudad)):
            for j in range(len(b_pais)):
                if b_ciudad[i][0]==b_pais[j][0]:
                    if cod == int(b_ciudad[i][1]) and cod_p==int(b_pais[j][0]):
                        band = 1
                        messagebox.showinfo("Buscar Ciudad", f"El codigo '{cod}' pertenece a {b_ciudad[i][2]}, {b_pais[j][1]}.")
        if band == 0:
            messagebox.showinfo("Error", f"El codigo '{cod}' no esta en lista de ciudades de {b_pais[j][1]}.")
    elif bscr == 4:
        band = 0
        b_clientes = base[2]
        a = True
        while a:
            cod = simpledialog.askfloat("Buscar cliente", "Por favor, ingresa un codigo de cliente:")
            if type(cod)==float:
                cod = int(cod)
                a=False
            else:
                messagebox.showinfo("Error", "Debe escribir un codigo correcto.")
        for i in range(len(b_clientes)):
            if cod == int(b_clientes[i][0]):
                band = 1
                messagebox.showinfo("Buscar cliente", f"El codigo '{cod}' pertenece a {b_clientes[i][1]}.")
        if band == 0:
            messagebox.showinfo("Error", f"El codigo '{cod}' no esta en lista de clientes.")

    elif bscr == 5 or bscr == 8:
        band = 0
        b_mascotas = base[3]
        a = True
        while a:
            cod = simpledialog.askfloat("Buscar mascota", "Por favor, ingresa un codigo de mascotas:")
            if type(cod)==float:
                cod = int(cod)
                a=False
            else:
                messagebox.showinfo("Error", "Debe escribir un codigo correcto.")
        for i in range(len(b_mascotas)):
            if cod == int(b_mascotas[i][1]):
                band = 1
                masc = b_mascotas[i][1]
                messagebox.showinfo("Buscar Mascotas", f"El codigo '{cod}' pertenece a {b_mascotas[i][2]}, un(a) {b_mascotas[i][3]}.")
        if band == 0:
            messagebox.showinfo("Error", f"El codigo '{cod}' no esta en lista de mascotas.")
        tiene = 0
        comparacion = []
        if bscr == 8 and band == 1: 
            b_medicacion = base[6]
            for i in range(len(b_medicacion)):
                if masc == b_medicacion[i][0]: 
                    comparacion+=[b_medicacion[i]]
                    tiene = 1
            if tiene == 1:
                otra1=0
                otra2=0
                otra3=0
                medica = []
                for i in range(len(comparacion)):
                    if int(comparacion[i][4]) > otra1:
                        otra1 = int(comparacion[i][4])
                        otra2 = int(comparacion[i][3])
                        otra3 = int(comparacion[i][2])
                    elif int(comparacion[i][4]) == otra1:
                        for i in range(len(comparacion)):
                            if int(comparacion[i][3]) > otra2:
                                otra2 = int(comparacion[i][3])
                                otra3 = int(comparacion[i][2])
                            elif int(comparacion[i][3]) == otra2:
                                for i in range(len(comparacion)):
                                    if int(comparacion[i][2]) >= otra3:
                                        otra3 = int(comparacion[i][2])
                for i in range(len(comparacion)):
                    if int(comparacion[i][4]) == otra1:
                        if int(comparacion[i][3]) == otra2:
                            if int(comparacion[i][2]) == otra3:
                                medica += [comparacion[i]]
                if len(medica)<1:
                    print(medica)
                else:
                    ultima=[]
                    for i in range(len(medica)):
                        messagebox.showinfo("Ultima medicacion", f"La ultima medicacion de dicha mascota fue:\n{medica[i]}")
                        for j in range(len(medica)):
                            if i!=j:
                                if medica[i][4]>medica[j][4]:
                                    ultima=medica[i]
                                elif medica[i][4]==medica[j][4]:
                                    if medica[i][3]>medica[j][4]:
                                        ultima=medica[i]
                                    elif medica[i][3]==medica[j][3]:
                                        if medica[i][2]>medica[j][2]:
                                            ultima=medica[i]                    
            elif tiene == 0:
                messagebox.showinfo("Error", f"Esta mascota no presenta medicacion.")
    elif bscr == 6:
        band = 0
        b_visitas = base[4]
        v_mascotas = base[3]
        a = True
        while a:
            cod = simpledialog.askfloat("Buscar Visitas", "Por favor, ingresa un codigo de visita:")
            if type(cod)==float:
                cod = int(cod)
                a=False
            else:
                messagebox.showinfo("Error", "Debe escribir un codigo correcto.")
        for i in range(len(b_visitas)):
            if cod == int(b_visitas[i][0]):
                band = 1
                for j in range(len(v_mascotas)):
                    if v_mascotas[j][1] == b_visitas[i][1]:
                        messagebox.showinfo("Buscar Visita", f"El codigo de visita: '{cod}' pertenece a {v_mascotas[j][2]}, {v_mascotas[j][3]},\nY la ultima fecha de visita fue: {v_mascotas[j][11]}/{v_mascotas[j][12]}/{v_mascotas[j][13]}.")
        if band == 0:
            messagebox.showinfo("Error", f"El codigo '{cod}' no esta en lista de visitas.")    

    elif bscr == 7:
        band = 0
        b_tratamiento = base[5]
        a = True
        while a:
            cod = simpledialog.askfloat("Buscar tratamiento", "Por favor, ingresa un codigo de tratamiento:")
            if type(cod)==float:
                cod = int(cod)
                a=False
            else:
                messagebox.showinfo("Error", "Debe escribir un codigo correcto.")
        for i in range(len(b_tratamiento)):
            if cod == int(b_tratamiento[i][0]):
                band = 1
                messagebox.showinfo("Buscar Visitas", f"El codigo '{cod}' pertenece al tratamiento:\nCodigo: {b_tratamiento[i][0]}\nNombre: {b_tratamiento[i][1]}\nValor Unitario: {b_tratamiento[i][2]}.")
        if band == 0:
            messagebox.showinfo("Error", f"El codigo '{cod}' no esta en lista de tratamientos.")
    
