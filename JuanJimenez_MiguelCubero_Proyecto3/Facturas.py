from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import simpledialog
from tkinter import messagebox
from Funciones import *
from lectura import abre_facturas 

def factura(bscr,base):
    if bscr == 2:
        band = 0
        b_clientes = base[2]
        a = True
        while a:
            cod = simpledialog.askfloat("Saldo cliente", "Por favor, ingresa un codigo de cliente,\npara manejo de saldo\n(se ocupa cliente presente):")
            if type(cod)==float:
                cod = int(cod)
                a=False
            else:
                messagebox.showinfo("Error", "Debe escribir un codigo correcto.")
        for i in range(len(b_clientes)): 
            if cod == int(b_clientes[i][0]):
                band = 1
                num=i
                cliente=b_clientes[i]
                ask = messagebox.askquestion("Saldo cliente", f"El codigo '{cod}' pertenece a {b_clientes[i][1]}\nDesea cambiar el saldo?")
        if band == 0:
            messagebox.showinfo("Error", f"El codigo '{cod}' no esta en lista de clientes.")
        if band==1:
            if ask=='yes':
                a = True
                while a:
                    saldo = simpledialog.askfloat("Saldo cliente", "Por favor, ingrese cuanto,\ndeseea agregar o restar:")
                    if type(saldo)==float:
                        saldo = int(saldo)
                        a=False
                    else:
                       messagebox.showinfo("Error", "Parametro incorrecto")
                if (int(cliente[10])+saldo)>=0:
                    cliente[10]=str(int(cliente[10])+saldo)
                    if int(cliente[10])<99999:
                        cliente[9]='3'
                    elif 100000<int(cliente[10])<101000:
                        cliente[9]='5'
                    elif int(cliente[10])==101000 or int(cliente[10])>101000:
                        cliente[9]='10'
                    b_clientes[num][10]=cliente[10]#Falta hacer que el dato cambie en la factura
                    b_clientes[num][9]=cliente[9]#Falta hacer que el dato cambie en la factura
                    messagebox.showinfo("Saldo Cliente", f"El nuevo saldo es: {cliente[10]}\nEl descuento quedo segun el saldo en: {cliente[9]}\nPor la informacion queda:\n{cliente}")
                else:
                    ala=int(cliente[10])+saldo
                    messagebox.showinfo("Saldo cliente", f"El saldo se mantiene como estaba.\nDebido a que el saldo quedaria {ala}.")
                    base[-1]=abre_facturas(base[2],base[6],base[3])
            else:
                messagebox.showinfo("Saldo cliente", "El saldo se mantiene como estaba.")

    elif bscr == 3:
        band = 0
        b_clientes = base[2]
        a = True
        while a:
            cod = simpledialog.askfloat("Descuentos cliente", "Por favor, ingresa un codigo de cliente,\npara manejo de descuentos\n(se ocupa cliente presente):")
            if type(cod)==float:
                cod = int(cod)
                a=False
            else:
                messagebox.showinfo("Error", "Debe escribir un codigo correcto.")
        for i in range(len(b_clientes)):
            if cod == int(b_clientes[i][0]):
                band = 1
                cliente=b_clientes[i]
                num=i
                messagebox.showinfo("Descuentos cliente", f"El codigo '{cod}' pertenece a {b_clientes[i][1]}.")
        if band == 0:
            messagebox.showinfo("Error", f"El codigo '{cod}' no esta en lista de clientes.")
        if band==1 and int(cliente[10])>5000:
            a = True
            while a:
                descu = simpledialog.askfloat("Descuentos cliente", "Por favor, ingrese el descuento que quiere aplicar\n(3,5,10):")
                if type(descu)==float:
                    descu = int(descu)
                    if descu==3 or descu==5 or descu==10:
                        a=False
                    else:
                       messagebox.showinfo("Error", "Parametro incorrecto")
                else:
                   messagebox.showinfo("Error", "Parametro incorrecto")
            if int(cliente[10])>5000:
                cliente[10]=(int(cliente[10])/100*(100-descu))
                b_clientes[num][10]=str(int(cliente[10]))#Falta hacer que el dato cambie en la factura
                b_clientes[num][9]=str(descu)#Falta hacer que el dato cambie en la factura
                messagebox.showinfo("Descuento cliente", f"El descuento de {descu}% ahora hace que el saldo sea {cliente[10]}.")
                base[-1]=abre_facturas(base[2],base[6],base[3])
            else:
                messagebox.showinfo("Descuento cliente", "El descuento se mantiene como estaba debido a que el saldo es menor a 5000.")
        else:
            messagebox.showinfo("Descuento cliente", "El descuento se mantiene como estaba debido a que el saldo es menor a 5000.")

##    elif bscr == 4:
##        facturas = base[-1]
##        b_clientes = base[2]
##        a = True
##        while a:
##            cod = simpledialog.askfloat("Facturar cliente", "Por favor, ingresa un codigo de cliente,\npara ver la factura:")
##            if type(cod)==float:
##                cod = int(cod)
##                a=False
##            else:
##                messagebox.showinfo("Error", "Debe escribir un codigo correcto.")
##        for i in range(len(b_clientes)):
##            if cod == int(b_clientes[i][0]):
##                band = 1
##                cliente=b_clientes[i]
##                num=i
##                messagebox.showinfo("Facturar cliente", f"El codigo '{cod}' pertenece a {b_clientes[i][1]}.")
##        if band == 0:
##            messagebox.showinfo("Error", f"El codigo '{cod}' no esta en lista de clientes.")
##        if band==1:
##            for i in range(len(facturas)):
##                if facturas[i][0][0]== cliente[0]:
##                    ffact=facturas[i][1][0]
##                    messagebox.showinfo("Fatura", f"Factura: {ffact[7]}\nFecha: {ffact[8]}/{ffact[9]}/{ffact[10]}\nCedula cliente: {ffact[0]}\nNombre del la mascota: {ffact[1]}\nId de la mascota: {ffact[2]}\nNombre de la medicina: {ffact[3]}\nCosto Unitario: {ffact[4]}\nUnidades compradas: {ffact[5]}\nTotal a cancelar: {ffact[6]}")






