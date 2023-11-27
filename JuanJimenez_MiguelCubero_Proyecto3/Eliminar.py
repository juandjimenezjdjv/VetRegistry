from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import simpledialog
from tkinter import messagebox
from Funciones import *
from lectura import abre_facturas

def eliminar(num,base):
    if num==2:#pais
        a = True
        while a:
            cod = simpledialog.askfloat("Ingresar codigo", "Por favor, ingresa un codigo de pais a eliminar:")
            if type(cod)==float:
                cod = str(int(cod))
                for i in range(len(base[0])):
                    if base[0][i][0]==cod:
                        messagebox.showinfo("Eliminar Pais", f"Se eliminarán los datos relacionados a {base[0][i][1]}")
                        a = False
                if a:
                    messagebox.showinfo("Eliminar Pais", "No se encontró el código de país.")
            else:
                messagebox.showerror("Eliminar Pais", "Debe ingresar un codigo apropiado")
        #borremos el pais
        for i in range(len(base[1])-1, -1, -1):
            if base[0][i][0] == cod:
                del(base[0][i])
        #borremos ciudad
        for i in range(len(base[1])-1, -1, -1):
            if base[1][i][0] == cod:
                del(base[1][i])
        #borremos clientes, mascota y visita
        for i in range(len(base[2])-1, -1, -1):
            if base[2][i][3] == cod:
                for j in range(len(base[3])-1, -1, -1):
                    if base[3][j][0] == base[2][i][0]:
                        for k in range(len(base[4])-1, -1, -1):
                            if base[4][k][1] == base[3][j][1]:
                                del(base[4][k])
                        for k in range(len(base[5])-1, -1, -1):
                            if base[5][k][0] == base[3][j][1]:
                                del(base[5][k])
                        for k in range(len(base[6])-1, -1, -1):
                            if base[6][k][0] == base[3][j][1]:
                                del(base[6][k])
                        del(base[3][j])
                del(base[2][i])
    elif num==3:#ciudad
        a = True
        while a:
            cod = simpledialog.askfloat("Ingresar codigo", "Por favor, ingresa un código de la ciudad a eliminar:")
            if type(cod)==float:
                cod = str(int(cod))
                for i in range(len(base[1])):
                    if base[1][i][1]==cod:
                        messagebox.showinfo("Eliminar Ciudad", f"Se eliminarán los datos relacionados a {base[1][i][1]}")
                        a = False
                if a:
                    messagebox.showinfo("Eliminar ciudad", "No se encontró el código de ciudad.")
            else:
                messagebox.showerror("Eliminar Ciudad", "Debe ingresar un codigo apropiado")
        #borra la ciudad.
        for i in range(len(base[1])-1, -1, -1):
            if base[1][i][1] == cod:
                del(base[1][i])
        #borremos clientes, mascota y visita
        for i in range(len(base[2])-1, -1, -1):
            if base[2][i][4] == cod:
                for j in range(len(base[3])-1, -1, -1):
                    if base[3][j][0] == base[2][i][0]:
                        for k in range(len(base[4])-1, -1, -1):
                            if base[4][k][1] == base[3][j][1]:
                                del(base[4][k])
                        for k in range(len(base[5])-1, -1, -1):
                            if base[5][k][0] == base[3][j][1]:
                                del(base[5][k])
                        for k in range(len(base[6])-1, -1, -1):
                            if base[6][k][0] == base[3][j][1]:
                                del(base[6][k])
                        del(base[3][j])
                del(base[2][i])

    elif num==4:#cliente
        a = True
        while a:
            cod = simpledialog.askfloat("Ingresar codigo", "Por favor, ingresa un código de cliente a eliminar:")
            if type(cod)==float:
                cod = str(int(cod))
                for i in range(len(base[2])):
                    if base[2][i][0]==cod:
                        messagebox.showinfo("Eliminar cliente", f"Se eliminarán los datos relacionados a {base[2][i][1]}")
                        a = False
                if a:
                    messagebox.showinfo("Eliminar cliente", "No se encontró el código de cliente.")
            else:
                messagebox.showerror("Eliminar cliente", "Debe ingresar un codigo apropiado")
        for i in range(len(base[2])-1, -1, -1):
            if base[2][i][0] == cod:
                for j in range(len(base[3])-1, -1, -1):
                    if base[3][j][0] == base[2][i][0]:
                        for k in range(len(base[4])-1, -1, -1):
                            if base[4][k][1] == base[3][j][1]:
                                del(base[4][k])
                        for k in range(len(base[5])-1, -1, -1):
                            if base[5][k][0] == base[3][j][1]:
                                del(base[5][k])
                        for k in range(len(base[6])-1, -1, -1):
                            if base[6][k][0] == base[3][j][1]:
                                del(base[6][k])
                        del(base[3][j])
                del(base[2][i])
                base[-1]=abre_facturas(base[2],base[6],base[3])

    elif num==5:#mascota
        a = True
        while a:
            cod = simpledialog.askfloat("Ingresar codigo", "Por favor, ingresa un código de mascota a eliminar:")
            if type(cod)==float:
                cod = str(int(cod))
                for i in range(len(base[3])):
                    if base[3][i][1]==cod:
                        messagebox.showinfo("Eliminar mascota", f"Se eliminarán los datos relacionados a {base[3][i][2]}")
                        a = False
                if a:
                    messagebox.showinfo("Eliminar mascota", "No se encontró el código de mascota.")
            else:
                messagebox.showerror("Eliminar mascota", "Debe ingresar un codigo apropiado")
        for i in range(len(base[3])-1, -1, -1):
            if base[3][i][1] == cod:
                del(base[3][i])
        for k in range(len(base[4])-1, -1, -1):
            if base[4][k][1] == cod:
                del(base[4][k])
        for k in range(len(base[5])-1, -1, -1):
            if base[5][k][0] == cod:
                del(base[5][k])
        for k in range(len(base[6])-1, -1, -1):
            if base[6][k][0] == cod:
                del(base[6][k])
        base[-1]=abre_facturas(base[2],base[6],base[3])
            
    elif num==6:#visita
        a = True
        while a:
            cod = simpledialog.askfloat("Ingresar codigo", "Por favor, ingresa un código de visita a eliminar:")
            if type(cod)==float:
                cod = str(int(cod))
                for i in range(len(base[4])):
                    if base[4][i][0]==cod:
                        messagebox.showinfo("Eliminar visita", f"Se eliminará la visita:\n{base[4][i]}")
                        a = False
                if a:
                    messagebox.showinfo("Eliminar visita", "No se encontró el código de visita.")
            else:
                messagebox.showerror("Eliminar visita", "Debe ingresar un codigo apropiado")
        for i in range(len(base[4])-1, -1, -1):
            if base[4][i][0] == cod:
                del(base[4][i])

    elif num==7:#tratamiento
        a = True
        while a:
            cod = simpledialog.askfloat("Ingresar codigo", "Por favor, ingresa un código de tratamiento a eliminar:")
            if type(cod)==float:
                cod = str(int(cod))
                for i in range(len(base[5])):
                    if base[5][i][0]==cod:
                        messagebox.showinfo("Eliminar tratamiento", f"Se eliminará el tratamiento:\n{base[5][i]}")
                        a = False
                if a:
                    messagebox.showinfo("Eliminar tratamiento", "No se encontró el código de tratamiento.")
            else:
                messagebox.showerror("Eliminar tratamiento", "Debe ingresar un codigo apropiado")
        for i in range(len(base[5])-1, -1, -1):
            if base[5][i][0] == cod:
                del(base[5][i])
    elif num==8:
        messagebox.showinfo("No se puede eliminar", "La medicacion no se puede eliminar\n(enunciado proyecto).")











        
        
