from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import simpledialog
from tkinter import messagebox
from Funciones import *
from lectura import abre_facturas

def modificar(bscr,base):
    if bscr == 2:#Pais
        band = 0
        b_pais = base[0]
        cod = cod_modif("pais")
        for i in range(len(b_pais)):
            if cod == int(b_pais[i][0]):
                band = 1
                messagebox.showinfo("Modificar Pais", f"El codigo '{cod}' del nombre a modificar pertenece a {b_pais[i][1]}.")
                op=0
                a = True
                while a:
                    valido = True
                    nombre = simpledialog.askstring("Ingresar nombre", "Por favor, ingrese el nuevo nombre de pais:")
                    for i in range(len(b_pais)):
                        if b_pais[i][1]==nombre:
                            valido = False
                            messagebox.showinfo("Error", "Código ya en uso.")
                    if valido:
                        op=1
                        a = False
                if op == 1:
                    for i in range(len(b_pais)):
                        if cod == int(b_pais[i][0]):
                            b_pais[i][1]=nombre
                            messagebox.showinfo("Modificar Pais", f"El codigo '{cod}' ahora pertenece a {b_pais[i][1]}.")
        if band == 0:
            messagebox.showinfo("Modificar Pais", f"El codigo '{cod}' no esta en lista de paises.")
  
    elif bscr == 3:#Ciudad
        band = 0
        band_2 = 0
        temp=[]
        b_ciudad = base[1]
        cod = cod_modif("pais")
        for i in range(len(b_ciudad)):
            if str(cod) == b_ciudad[i][0]:
                band = 1
                temp+=[b_ciudad[i]]
                messagebox.showinfo("Modificar Ciudad", f"El codigo '{cod}' pertenece a {b_ciudad[i][2]}({b_ciudad[i][1]}).")
        if band == 0:
            messagebox.showinfo("Modificar Ciudad", f"El codigo '{cod}' no esta asociado a ningun pais.")
            return base
        cod_c = cod_modif("ciudad")
        for i in range(len(b_ciudad)):
            for j in range(len(temp)):
                if b_ciudad[i][0]==temp[j][0]:
                    if cod_c == int(b_ciudad[i][1]):
                        band_2 = 1
                        messagebox.showinfo("Modificar Ciudad", f"El codigo '{cod_c}' pertenece a {b_ciudad[i][2]}.")
                        hold = b_ciudad[i]
                        break
        if band_2 ==1:
            op=0
            a = True
            valido = True
            while a:
                nombre = simpledialog.askstring("Ingresar nombre", "Ingrese el nuevo nombre de la ciudad:")
                for i in range(len(b_ciudad)):
                    if b_ciudad[i][2]==nombre:
                        valido = False
                        messagebox.showinfo("Error", "Nombre ya en uso.")
                if valido:
                    op=1
                    a = False
            if op == 1:
                for i in range(len(b_ciudad)):
                    if b_ciudad[i]==hold:
                        b_ciudad[i][2]=nombre
                        messagebox.showinfo("Modificar Ciudad", f"El codigo '{cod_c}' ahora pertenece a {b_ciudad[i][2]}.")
        if band_2 == 0:
            messagebox.showinfo("Modificar Ciudad", f"El codigo '{cod_c}' no esta asociado a ninguna ciudad.")


    elif bscr == 4:#Cliente
        band = 0
        ubicacion = base[1]
        b_clientes = base[2]
        cod = cod_modif("cliente")
        for i in range(len(b_clientes)):
            if cod == int(b_clientes[i][0]):
                band = 1
                nombre = messagebox.askquestion("Nombre", f"El codigo '{cod}' pertenece a {b_clientes[i][1]}.\nDesea Cambiar el nombre?")
                if nombre == 'yes':
                    b_clientes[i][1] = simpledialog.askstring("Ingresar nombre", "Ingrese el nuevo nombre de cliente:")
                direccion = messagebox.askquestion("Direccion", "Desea cambiar la direccion?")
                if direccion == 'yes':
                    b_clientes[i][2] = simpledialog.askstring("Direccion", "Ingrese la nueva direccion:")
                codpais = messagebox.askquestion("Nombre", "Desea cambiar el codigo de pais y codigo de ciudad?")
                if codpais == 'yes':
                    op=0
                    a = True
                    while a:
                        valido = False
                        codpais = str(cod_modif("nuevo de pais"))
                        for j in range(len(ubicacion)):
                            if codpais == ubicacion[j][0]:
                                valido = True
                        if valido:
                            op=1
                            a = False
                        else:
                            messagebox.showinfo("Error", "Código de país inexistente.")
                    a = True
                    ap = 0
                    while a:
                        valido = False
                        codciudad = cod_modif("nuevo de ciudad")
                        for j in range(len(ubicacion)):
                            if ubicacion[j][0]==codpais and ubicacion[j][1]==str(codciudad):
                                valido = True
                                ap=1
                            if valido:
                                a = False
                        if ap==0:
                            messagebox.showinfo("Error", "La ciudad en el país indicado, no existe.")
                    if op==1 and ap==1:
                        b_clientes[i][3]=str(codpais)
                        b_clientes[i][4]=str(codciudad)
                telefono = messagebox.askquestion("Telefono", "Desea cambiar el numero de telefono?")
                if telefono == 'yes':
                    b_clientes[i][5]=cod_modif("telefono")
                hold_cliente = b_clientes[i]
        if band ==1:
            messagebox.showinfo("Datos actualizados", f"ahora los datos en lista quedarian de la siguiete manera:\n{hold_cliente}")
            base[-1] = abre_facturas(base[2],base[6],base[3])
        if band == 0:
            messagebox.showinfo("Error", f"El codigo '{cod}' no esta en lista de clientes.")


    elif bscr == 5:#Mascotas
        band = 0
        band_2 = 0
        temp=[]
        b_mascotas = base[3]
        cod = cod_modif("Digite el numero de cliente para buscar las mascotas a su nombre:")
        for i in range(len(b_mascotas)):
            if cod == int(b_mascotas[i][0]):
                band = 1
                temp+=[b_mascotas[i]]
        if band == 0:
            messagebox.showinfo("Error", f"El codigo cliente '{cod}' no existe o no tiene mascotas.")
        m_cod = cod_modif("mascota")
        for i in range(len(b_mascotas)):
            for j in range(len(temp)):
                if b_mascotas[i][0]==temp[j][0]:
                    if m_cod == int(b_mascotas[i][1]):
                        band_2 = 1
                        messagebox.showinfo("Modificar mascotas", f"El codigo '{m_cod}' pertenece a {b_mascotas[i][2]}.")
                        hold = b_mascotas[i]
                        hold_mascota = b_mascotas[i]
                        break
        if band_2 ==1:
            mascota = messagebox.askquestion("Mascota", "Desea cambiar el nombre a la mascota?")
            if mascota == 'yes':
                for i in range(len(b_mascotas)):
                        if b_mascotas[i]==hold:
                            b_mascotas[i][2] = simpledialog.askstring("Ingresar nombre", "Ingrese el nuevo nombre de mascota:")
            if hold[10]=='si':
                messagebox.showinfo("Modificar mascotas", "La mascota ya esta castrada.")
            else:
                castrar = messagebox.askquestion("Mascota", "Desea cambiar el nombre a la mascota?")
                if castrar == 'yes':
                    for i in range(len(b_mascotas)):
                        if b_mascotas[i]==hold:
                            b_mascotas[i][10]='si'
                            messagebox.showinfo("Modificar mascotas", "La mascota se castrara, por lo que aparecera castrada en el futuro.")
        if band==1 and band_2==1:
            messagebox.showinfo("Modificar mascotas", f"Algunos datos pudieron ser actualizados de la mascota, ahora los datos en lista quedarian de la siguiete manera:\n{hold_mascota}")
            base[-1] = abre_facturas(base[2],base[6],base[3])
        if band_2==0 and band==1:
            messagebox.showinfo("Modificar mascotas", f"El codigo '{m_cod}' no pertenece a ninguna mascota.")

    elif bscr == 6:#Visitas
        band = 0
        b_visitas = base[4]
        v_mascotas = base[3]
        cod = cod_modif("visitas")
        for i in range(len(b_visitas)):
            if cod == int(b_visitas[i][0]):
                band = 1
                for j in range(len(v_mascotas)):
                    if v_mascotas[j][1] == b_visitas[i][1]:
                        messagebox.showinfo("Modificar visita", f"El codigo de visita: '{cod}' pertenece a {v_mascotas[j][2]}, {v_mascotas[j][3]},\nY la ultima fecha de visita fue: {b_visitas[i][2]}/{b_visitas[i][3]}/{b_visitas[i][4]}.")
                        pago = messagebox.askquestion("Visita", "Desea cambiar la forma de pago?")
                        hold_visita = b_visitas[i]
                        if pago == 'yes':
                            a = True
                            while a:
                                formadepago=cod_modif("A que desea cambiar: Contado('01') o Crédito('02'): ")
                                if formadepago == 1:
                                    if b_visitas[i][6]=='01':
                                        messagebox.showinfo("Modificar visita", "Su forma de pago es la misma a la anterior")
                                    else:
                                        b_visitas[i][6]='01'
                                        messagebox.showinfo("Modificar visita", "Su forma de pago se ha cambiado a contado")
                                    a = False
                                elif formadepago == 2:
                                    if b_visitas[i][6]=='02':
                                        messagebox.showinfo("Modificar visita", "Su forma de pago es la misma a la anterior")
                                    else:
                                        b_visitas[i][6]='02'
                                        messagebox.showinfo("Modificar visita", "Su forma de pago se ha cambiado a credito")
                                    a = False  
                                else:
                                    messagebox.showinfo("Error", "Método de pago inválido.")
        if pago == 'yes':
            messagebox.showinfo("Modificar visita", f"Algunos datos de visitas fueron actualizados, ahora los datos en lista quedarian de la siguiete manera:\n{hold_visita}")
        if band == 0:
            messagebox.showinfo("Modificar visita", f"El codigo '{cod}' no esta en lista de visitas.")


    elif bscr == 7:#Tratamiento
        band = 0
        b_tratamiento = base[5]
        cod = cod_modif("tratamiento")
        for i in range(len(b_tratamiento)):
            if cod == int(b_tratamiento[i][0]):
                band = 1
                messagebox.showinfo("Modificar Tratamiento", f"El codigo '{cod}' pertenece al tratamiento:\nCodigo: {b_tratamiento[i][0]}\nNombre: {b_tratamiento[i][1]}\nValor Unitario: {b_tratamiento[i][2]}.")
                pago = messagebox.askquestion("Tratamiento", "Desea cambiar precio unitario del tratamiento?")
                if pago == 'yes':
                    precio = cod_modif("Ingrese el nuevo precio unitario.")
                    b_tratamiento[i][2]=precio
                    hold_tratamiento = b_tratamiento[i]
        if band==1 and pago=='yes':
            messagebox.showinfo("Modificar Tratamiento", f"Algunos datos de visitas fueron actualizados, ahora los datos en lista quedarian de la siguiete manera:\n{hold_tratamiento}")
        else:
            messagebox.showinfo("Modificar Tratamiento", "Los datos de tratamiento quedaron igual.")
        if band == 0:
            messagebox.showinfo("Modificar Tratamiento", f"El codigo '{cod}' no esta en lista de tratamientos.")

    elif bscr == 8:#Medicamento
        band = 0
        band_2 = 0
        medi =[]
        b_mascotas = base[3]
        b_medicacion = base[6]
        cod = cod_modif("mascotas (para buscar medicamentos)")
        for i in range(len(b_mascotas)):
            if cod == int(b_mascotas[i][1]):
                band = 1
                masc = b_mascotas[i][1]
                messagebox.showinfo("Modificar Medicamento", f"El codigo '{cod}' pertenece a {b_mascotas[i][2]}, un(a) {b_mascotas[i][3]}.")
        if band==1:
            for j in range(len(b_medicacion)):
                if masc == b_medicacion[j][0]:
                    medi+=[b_medicacion[j]]
            temp=[]
            cod_m = cod_modif("medicacion")
            for i in range(len(medi)):
                if str(cod_m) == medi[i][1]:
                    band_2=1
                    temp=medi[i]
                    break         
            if band==1 and band_2==1:
                op=0
                ap=0
                canti = messagebox.askquestion("Tratamiento", "Desea cambiar cantidad de medicacion?")
                if canti == 'yes':
                    cantidad = cod_modif("Ingrese la cantidad de medicacion. ")
                    op=1
                pumed = messagebox.askquestion("Tratamiento", "Desea cambiar el precio unitario de medicacion?")
                if pumed == 'yes':
                    precio = cod_modif("Ingrese precio unitario de medicacion. ")
                    ap=1
                if op==0 and ap==0:
                    pass
                else:
                    for i in range(len(b_medicacion)):
                        if b_medicacion[i] == temp:
                            if op == 1 and ap==0:
                                b_medicacion[i][7]=str(cantidad)
                                b_medicacion[i][8]=str(int(b_medicacion[i][6])*cantidad)
                                messagebox.showinfo("Modificar Medicamento", f"El precio total es {b_medicacion[i][8]}.")
                            elif op==0 and ap==1:
                                b_medicacion[i][6]=str(precio)
                                b_medicacion[i][8]=str(int(b_medicacion[i][7])*precio)
                                messagebox.showinfo("Modificar Medicamento", f"El precio total es {b_medicacion[i][8]}.")
                            else:
                                b_medicacion[i][6]=str(precio)
                                b_medicacion[i][7]=str(cantidad)
                                b_medicacion[i][8]=str(cantidad*precio)
                            temp = b_medicacion[i]
        if band==1 and band_2==1:
            messagebox.showinfo("Modificar Medicamento", f"Algunos datos de medicacion fueron actualizados, ahora los datos en lista quedarian de la siguiete manera:\n{temp}")
            base[-1] = abre_facturas(base[2],base[6],base[3])
        if band == 0:
            messagebox.showinfo("Modificar Medicamento", f"El codigo '{cod}' no esta en lista de mascotas.")
        if band == 1 and band_2 == 0:
            messagebox.showinfo("Modificar Medicamento", f"El codigo '{cod_m}' no esta en lista de medicacion.")


def cod_modif(asdf):
    aprob = True
    while aprob:
        try:
            if asdf=="Ingrese el nuevo precio unitario.":
                cod = simpledialog.askfloat("Ingresar Precio", "Ingrese el nuevo precio unitario.")
                if type(cod)==float:
                    cod = int(cod)                
            elif asdf =="Digite el numero de cliente para buscar las mascotas a su nombre:":
                cod = simpledialog.askfloat("Ingresar Numero", "Digite el numero de cliente para\nbuscar las mascotas  a su nombre.")
                if type(cod)==float:
                    cod = int(cod)                
            elif asdf=="A que desea cambiar: Contado('01') o Crédito('02')":
                cod = simpledialog.askfloat("Forma de pago", "A que desea cambiar: Contado('01') o Crédito('02'):")
                if type(cod)==float:
                    cod = int(cod)               
            elif asdf=="Ingrese la cantidad de medicacion. ":
                cod = simpledialog.askfloat("Ingresar Cantidad", "Ingrese la cantidad de medicacion:")
                if type(cod)==float:
                    cod = int(cod)                
            elif asdf == "Ingrese precio unitario de medicacion. ":
                cod = simpledialog.askfloat("Ingresar Precio", "Ingrese precio unitario de medicacion:")
                if type(cod)==float:
                    cod = int(cod)              
            else:
                cod = simpledialog.askfloat("Ingresar Codigo", f"Digite el codigo o numero de {asdf} que desea buscar:")
                if type(cod)==float:
                    cod = int(cod)
            aprob = False
        except ValueError:
            print("Debe escribir un codigo, numero o id apropiado.")
    return cod

def posiacaso():
    sigue=True
    while sigue:
        sino=input().lower()
        if sino == "si":
            sigue=False
            return "si"
        elif sino == "no":
            sigue=False
            return "no"
        else:
            print("De decir 'si' o 'no'.")
            
