from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import simpledialog
from tkinter import messagebox
from Funciones import *
from lectura import abre_facturas

def insercion(num,base_de_datos):
    if num ==2: #2 = pais
        base = base_de_datos[0]
        x=0
        a = True
        while a:
            valido = True
            cod_p = simpledialog.askfloat("Ingresar codigo", "Por favor, ingresa un codigo de pais:")
            if type(cod_p)==float:
                cod = str(int(cod_p))
                for i in range(len(base)):
                    if base[i][0]==cod:
                        valido = False
                        ok = messagebox.askokcancel("Operación cancelada", "Ya hay un pais con ese codigo.\nDesea probar otro codigo?")
                        if not ok:
                            a=False
                if valido:
                    x=1
                    a = False
        o=0
        if x==1:     
            a = True
            while a:
                valido = True
                nombre = simpledialog.askstring("Ingresar nombre", "Por favor, ingresa un nombre de pais:")
                if type(nombre)==str:
                    for i in range(len(base)):
                        if base[i][1]==nombre:
                            valido = False
                            ok = messagebox.askokcancel("Operación cancelada", "Ya hay un pais con ese nombre.\nDesea probar otro nombre?")
                            if not ok:
                                a=False
                    if valido:
                        o=1
                        a = False
                else:
                    a=False
        if o==1 and x==1:
            messagebox.showinfo("Nuevo Pais", f"El pais se agegró exitosamente:\n[{cod},{nombre}]")
            base.append([cod,nombre])
            base_de_datos[0]=base

    elif num==3: #Ciudad
        base = base_de_datos[1]
        base_p = base_de_datos[0]
        x=0
        a = True
        while a:
            valido = False
            cod_pais_p = simpledialog.askfloat("Ingresar codigo", "Por favor, ingresa un codigo de pais:")
            if type(cod_pais_p)==float:
                cod_pais = str(int(cod_pais_p))
                for i in range(len(base_p)):
                    if base_p[i][0]==cod_pais:
                        valido = True
                if not valido:
                    ok = messagebox.askokcancel("Operación cancelada", "Código de país inexistente.\nDesea probar otro codigo?")
                    if not ok:
                        a=False
                else:
                    x=1
                    a = False
        y=0
        if x==1:
            a = True
            while a:
                valido = True
                cod_c = simpledialog.askfloat("Ingresar codigo", "Por favor, ingrese el codigo de la ciudad:")
                if type(cod_c)==float:
                    cod = str(int(cod_c))
                    for i in range(len(base)):
                        if base[i][1]==cod:
                            valido = False
                            messagebox.showinfo("Operación cancelada", "Código de país inexistente.")
                            break
                    if valido:
                        y=1
                        a = False
            z=0
            if y==1:
                a = True
                valido = True
                while a:
                    nombre= simpledialog.askstring("Ingresar nombre", "Por favor, ingresa un nombre de ciudad:")
                    for i in range(len(base)):
                        if base[i][2]==nombre:
                            valido = False
                            messagebox.showinfo("Operación cancelada", "Nombre de ciudad en uso.")
                    if valido:
                        z=1
                        a = False
        if x==1 and y==1 and z==1:
            messagebox.showinfo("Nueva Ciudad", f"La ciudad se agegró exitosamente:\n[{cod_pais},{cod},{nombre}]")
            base.append([cod_pais,cod,nombre])
            base_de_datos[1] = base
    elif num==4: #clientes
        base = base_de_datos[2]
        x=0
        a = True
        while a:
            valido = True
            identificacion = simpledialog.askfloat("Ingresar codigo", "Por favor, ingrese el código del cliente:")
            if type(identificacion)==float:
                identificacion = str(int(identificacion))
                for i in range(len(base)):
                    if base[i][0]==identificacion:
                        valido = False
                        messagebox.showinfo("Error", "El código ya esta en uso")
                if valido:
                    x=1
                    a = False                     
        y=0
        z=0
        if x==1:
            nombre = simpledialog.askstring("Ingresar nombre", "Por favor, ingrese el nombre del cliente:")
            direccion = simpledialog.askstring("Ingresar direccion", "Por favor, ingrese la dirección:")
            ubicacion = base_de_datos[1]
            a = True
            while a:
                valido = False
                codpais = simpledialog.askfloat("Ingresar codigo", "Por favor, ingrese el código del país:")
                if type(codpais)==float:
                    codpais = str(int(codpais))
                    for i in range(len(ubicacion)):
                        if codpais == ubicacion[i][0]:
                            valido = True
                    if valido:
                        y=1
                        a = False
                    else:
                        messagebox.showinfo("Error", "El código pais no existe.")
            if y==1:
                a = True
                while a:
                    valido = False
                    codciudad = simpledialog.askfloat("Ingresar codigo", "Por favor, ingrese el código de ciudad:")
                    if type(codciudad)==float:
                        codciudad = str(int(codciudad))
                        for i in range(len(ubicacion)):
                            if ubicacion[i][0]==codpais and ubicacion[i][1]==codciudad:
                                valido = True
                        if valido:
                            z=1
                            a = False
                        else:
                            messagebox.showinfo("Error", "La ciudad en el país indicado, no existe.")
                a=True
                while a:
                    telefono = simpledialog.askfloat("Ingresar numero", "Por favor, ingrese el número telefónico:")
                    if type(telefono)==float:
                        telefono = str(int(telefono))
                        a=False
                    else:
                        messagebox.showinfo("Error", "Ingrese un numero apropiado.")
                a=True
                while a:
                    dia = simpledialog.askfloat("Ingresar", "Por favor, ingrese el dia:")
                    if type(dia)==float:
                        dia = int(dia)
                        if 0<dia<30:
                            dia=str(dia)
                            a=False
                        else:
                            messagebox.showinfo("Error", "Ingrese un dia correcto.")
                    else:
                        messagebox.showinfo("Error", "Ingrese un dia correcto.")
                a=True
                while a:
                    mes = simpledialog.askfloat("Ingresar", "Por favor, ingrese el mes:")
                    if type(mes)==float:
                        mes = int(mes)
                        if 0<mes<13:
                            mes=str(mes)
                            a=False
                        else:
                            messagebox.showinfo("Error", "Ingrese un mes correcto.")
                    else:
                        messagebox.showinfo("Error", "Ingrese un mes correcto.")
                a=True
                while a:
                    año = simpledialog.askfloat("Ingresar", "Por favor, ingrese el año:")
                    if type(año)==float:
                        año = int(año)
                        if 1990<año<2050:
                            año=str(año)
                            a=False
                        else:
                            messagebox.showinfo("Error", "Ingrese un año correcto.")
                    else:
                        messagebox.showinfo("Error", "Ingrese un año correcto.")
        if x==1 and y==1 and z==1:
            messagebox.showinfo("Nuevo Cliente", f"El cliente se agegró exitosamente:\n[{identificacion},{nombre},{direccion},{codpais},{codciudad},{telefono},{dia},{mes},{año},0,0]")
            base.append([identificacion,nombre,direccion,codpais,codciudad,telefono,dia,mes,año,0,0])
            base_de_datos[2] = base
            base_de_datos[-1] = abre_facturas(base_de_datos[2],base_de_datos[6],base_de_datos[3])

    elif num==5: #mascota
        base = base_de_datos[3]
        clientes = base_de_datos[2]
        x=0
        a = True
        while a:
            valido = False
            identificacion = simpledialog.askfloat("Ingresar codigo", "Por favor, ingrese el código del cliente:")
            if type(identificacion)==float:
                identificacion = str(int(identificacion))
                for i in range(len(clientes)):
                    if clientes[i][0]==identificacion:
                        valido = True
                        id_cliente = i
                if valido:
                    x=1
                    a = False
                else:
                    messagebox.showinfo("Error", "Id de cliente no existente.")
        y=0
        if x==1:
            a = True
            while a:
                valido = True
                carne = simpledialog.askfloat("Ingresar ID", "Por favor, ingrese el ID del animal:")
                if type(carne)==float:
                    carne = str(int(carne))
                    for i in range(len(base)):
                        if base[i][1]==carne:
                            valido = False
                            messagebox.showinfo("Error", "Código ya en uso.")
                    if valido:
                        y=1
                        a = False
            if y==1:
                nombre = simpledialog.askstring("Ingresar nombre", "Por favor, ingrese el nombre de animal:")
                tipo = simpledialog.askstring("Ingresar tipo", "Por favor, ingrese el tipo de animal\n(perro,gato,...):")
                raza = simpledialog.askstring("Ingresar raza", "Por favor, ingrese la raza:")
                a=True
                while a:
                    dia = simpledialog.askfloat("Ingresar", "Por favor, ingrese el dia:")
                    if type(dia)==float:
                        dia = int(dia)
                        if 0<dia<31:
                            dia=str(dia)
                            a=False
                        else:
                            messagebox.showinfo("Error", "Ingrese un dia correcto.")
                    else:
                        messagebox.showinfo("Error", "Ingrese un dia correcto.")
                a=True
                while a:
                    mes = simpledialog.askfloat("Ingresar", "Por favor, ingrese el mes:")
                    if type(mes)==float:
                        mes = int(mes)
                        if 0<mes<13:
                            mes=str(mes)
                            a=False
                        else:
                            messagebox.showinfo("Error", "Ingrese un mes correcto.")
                    else:
                        messagebox.showinfo("Error", "Ingrese un mes correcto.")
                a=True
                while a:
                    año = simpledialog.askfloat("Ingresar", "Por favor, ingrese el año:")
                    if type(año)==float:
                        año = int(año)
                        if 1990<año<2050:
                            año=str(año)
                            a=False
                        else:
                            messagebox.showinfo("Error", "Ingrese un año correcto.")
                    else:
                        messagebox.showinfo("Error", "Ingrese un año correcto.")
                sexo = simpledialog.askstring("Ingresar sexo", "Por favor, ingrese el sexo del animal:")
                color = simpledialog.askstring("Ingresar color", "Por favor, ingrese el color del animal:")
                castrado = messagebox.askquestion("¿Castrado?", "Esta castrada la mascota")
                if castrado == "yes":
                    castrado = 'si'
                else:
                    castrado = 'no'
                a=True
                while a:
                    dia2 = simpledialog.askfloat("Ingresar", "Por favor, ingrese el dia:")
                    if type(dia2)==float:
                        dia2 = int(dia2)
                        if 0<dia2<31:
                            dia2=str(dia2)
                            a=False
                        else:
                            messagebox.showinfo("Error", "Ingrese un dia correcto.")
                    else:
                        messagebox.showinfo("Error", "Ingrese un dia correcto.")
                a=True
                while a:
                    mes2 = simpledialog.askfloat("Ingresar", "Por favor, ingrese el mes:")
                    if type(mes2)==float:
                        mes2 = int(mes2)
                        if 0<mes2<13:
                            mes2=str(mes2)
                            a=False
                        else:
                            messagebox.showinfo("Error", "Ingrese un mes correcto.")
                    else:
                        messagebox.showinfo("Error", "Ingrese un mes correcto.")
                a=True
                while a:
                    año2 = simpledialog.askfloat("Ingresar", "Por favor, ingrese el año:")
                    if type(año2)==float:
                        año2 = int(año2)
                        if 1990<año2<2050 and año2>=int(año):
                            año2=str(año2)
                            a=False
                        else:
                            messagebox.showinfo("Error", "Ingrese un año correcto.")
                    else:
                        messagebox.showinfo("Error", "Ingrese un año correcto.")
                base_de_datos[2][id_cliente][6] = dia2
                base_de_datos[2][id_cliente][7] = mes2
                base_de_datos[2][id_cliente][8] = año2   
        if x==1 and y==1:
            messagebox.showinfo("Nueva mascota", f"La mascota se agegró exitosamente:\n[{identificacion},{carne},{nombre},{tipo},{raza},{dia},{mes},{año},{sexo},{color},{castrado},{dia2},{mes2},{año2}]")
            base.append([identificacion,carne,nombre,tipo,raza,dia,mes,año,sexo,color,castrado,dia2,mes2,año2])
            base_de_datos[3] = base
            base_de_datos[-1] = abre_facturas(base_de_datos[2],base_de_datos[6],base_de_datos[3])


    elif num==6: #Visita
        base = base_de_datos[4]
        fs=0
        st=0
        a = True
        while a:
            codvisita = simpledialog.askfloat("Ingresar codigo", "Por favor, ingrese el código de visita:")
            if type(codvisita)==float:
                codvisita = str(int(codvisita))
                valido = True
                for i in range(len(base)):
                    if base[i][0] == codvisita:
                        valido = False
                        messagebox.showinfo("Error", "El código ya está en uso.")
                if valido:
                    fs=1
                    a = False
        if fs==1:
            a = True
            while a:
                idanimal = simpledialog.askfloat("Ingresar codigo", "Por favor, ingrese el id de la mascota:")
                if type(idanimal)==float:
                    idanimal = str(int(idanimal))
                    valido = False
                    for i in range(len(base_de_datos[3])):
                        if base_de_datos[3][i][1] == idanimal:
                            valido = True
                            fecha_masco = base_de_datos[3][i]
                            id_mascota = i
                            id_cliente = base_de_datos[3][i][0] 
                    if valido:
                        st=1
                        a = False
                    else:
                        messagebox.showinfo("Error", "No hay ninguna mascota registrada con ese id.")
            if st==1:
                a = True
                while a:
                    for i in range(len(base_de_datos[2])):
                        if base_de_datos[2][i][0]==id_cliente:
                            id_cliente = i
                            a = False

                d_val = int(fecha_masco[5])
                m_val = int(fecha_masco[6])
                a_val = int(fecha_masco[7])
                b = True
                x=0
                while b:
                    a=True
                    while a:
                        año = simpledialog.askfloat("Ingresar", "Por favor, ingrese el año:")
                        if type(año)==float:
                            año = int(año)
                            if 1990<año<2050:
                                año=str(año)
                                a=False
                            else:
                                messagebox.showinfo("Error", "Ingrese un año correcto.")
                        else:
                            messagebox.showinfo("Error", "Ingrese un año correcto.")
                    año = int(año)
                    if año>a_val:
                        año = str(año)
                        x=1
                        b=False
                    elif año==a_val:
                        año = str(año)
                        b=False
                    else:
                        messagebox.showinfo("Error", "Esta fecha no coincide con los datos de la mascota.")
                y=0
                b = True
                while b:
                    a=True
                    while a:
                        mes = simpledialog.askfloat("Ingresar", "Por favor, ingrese el mes:")
                        if type(mes)==float:
                            mes = int(mes)
                            if 0<mes<13:
                                mes=str(mes)
                                a=False
                            else:
                                messagebox.showinfo("Error", "Ingrese un mes correcto.")
                        else:
                            messagebox.showinfo("Error", "Ingrese un mes correcto.")
                    mes = int(mes)
                    if x==1:
                        mes = str(mes)
                        b=False
                    elif mes>m_val:
                        mes = str(mes)
                        y=1
                        b=False
                    elif mes==m_val:
                        mes = str(mes)
                        b=False
                    else:
                        messagebox.showinfo("Error", "Esta fecha no coincide con los datos de la mascota.")
                
                b = True
                while b:
                    a=True
                    while a:
                        dia = simpledialog.askfloat("Ingresar", "Por favor, ingrese el dia:")
                        if type(dia)==float:
                            dia = int(dia)
                            if 0<dia<31:
                                dia=str(dia)
                                a=False
                            else:
                                messagebox.showinfo("Error", "Ingrese un dia correcto.")
                        else:
                            messagebox.showinfo("Error", "Ingrese un dia correcto.")
                    dia = int(dia)
                    if x==1 or y==1:
                        dia = str(dia)
                        b=False
                    elif dia>d_val:
                        dia = str(dia)
                        b=False
                    else:
                        messagebox.showinfo("Error", "Esta fecha no coincide con los datos de la mascota.")
                
                
                a=True
                while a:
                    totalfactura = simpledialog.askfloat("Ingresar monto", "Por favor, ingrese el monto a pagar:")
                    if type(totalfactura)==float:
                        totalfactura = str(int(totalfactura))
                        a=False
                    else:
                        messagebox.showinfo("Error", "Escriba un monto correcto.")
                a = True
                while a:
                    formadepago = simpledialog.askfloat("Ingresar forma de pago", "Por favor, ingrese: 01- Contado ; 02 - Crédito.")
                    if type(formadepago)==float:
                        formadepago = str(int(formadepago))
                        if formadepago == "01" or "02":
                            a = False
                    elif a =="02":
                        base_de_datos[2][id_cliente][10]+=int(base_de_datos[2][id_cliente][10])
                        base_de_datos[2][id_cliente][10]+=totalfactura
                        base_de_datos[2][id_cliente][9] = descuento(int(base_de_datos[2][id_cliente][10]))    
                    else:
                        messagebox.showinfo("Error", "Método de pago inválido.")
                base_de_datos[3][id_mascota][11] = dia
                base_de_datos[3][id_mascota][12] = mes
                base_de_datos[3][id_mascota][13] = año
                base_de_datos[2][id_cliente][6] = dia
                base_de_datos[2][id_cliente][7] = mes
                base_de_datos[2][id_cliente][8] = año
        if fs==1 and st==1:
            messagebox.showinfo("Nueva visita", f"La visita se agegró exitosamente:\n[{codvisita},{idanimal},{dia},{mes},{año},{totalfactura},{formadepago}]")
            base.append([codvisita,idanimal,dia,mes,año,totalfactura,formadepago])
            base_de_datos[4] = base
    elif num==7: #tratamiento
        base = base_de_datos[5]
        x=0
        a = True
        while a:
            valido=True
            cod_c = simpledialog.askfloat("Ingresar codigo", "Por favor, ingrese el codigo de tratamiento:")
            if type(cod_c)==float:
                cod = str(int(cod_c))
                for i in range(len(base)):
                    if cod == base[i][0]:
                        valido=False
                        messagebox.showerror("Error", "Código ya en uso")
                if valido:
                    a = False
                    x=1
        nombre = simpledialog.askstring("Ingresar nombre", "Por favor, Ingrese el nombre del medicamento.")
        y=0
        a=True
        while a:
            precio = simpledialog.askfloat("Ingresar codigo", "Por favor, ingrese el precio unitario.")
            if type(precio)==float:
                y=1
                precio = str(int(precio))
                a=False
            else:
                messagebox.showerror("Error", "Ingrese un precio apropiado")
        z=0
        a=True
        while a:
            cantidad = simpledialog.askfloat("Ingresar codigo", "Por favor, ingrese la cantidad de medicamento en el almacen.")
            if type(cantidad)==float:
                z=1
                cantidad = str(int(cantidad))
                a=False
            else:
                messagebox.showerror("Error", "Ingrese un dato correcto.")
        if x==1 and y==1 and z==1:
            messagebox.showinfo("Nuevo Tratamiento", f"El tratamiento se agegró exitosamente:\n[{cod},{nombre},{precio},{cantidad}]")
            base.append([cod,nombre,precio,cantidad])
            base_de_datos[5] = base

    elif num==8: #medicacion
        base = base_de_datos[6]
        ad=0
        sf=0
        a = True
        while a:
            valido = False
            idanimal = simpledialog.askfloat("Ingresar Id", "Ingrese el id del animal:")
            if type(idanimal)==float:
                idanimal = str(int(idanimal))
                for i in range(len(base_de_datos[3])):
                    if idanimal == base_de_datos[3][i][1]:
                        valido = True
                        a = False
                        id_mascota = i
                        id_cliente = base_de_datos[3][i][0]
                        sf=1
                    if not valido:
                        messagebox.showinfo("Error", "No se encontró el id del animal.")
        if sf==1:
            for i in range(len(base_de_datos[2])):
                    if base_de_datos[2][i][0]==id_cliente:
                        id_cliente = i
                        a = False
            o=0
            a = True
            while a:
                o=0
                med = simpledialog.askfloat("Ingresar codigo", "Ingrese el código del medicamento:")
                if type(med)==float:
                    med = str(int(med))
                    for i in range(len(base_de_datos[6])):
                        if med == base_de_datos[6][i][1]:
                            o=1
                            messagebox.showinfo("Error", "No se puede repetir el codigo del medicamento.")
                if a and o==0:
                    a=False     
            visita=True
            while visita:
                a=True
                while a:
                    dia = simpledialog.askfloat("Ingresar", "Por favor, ingrese el dia de la visita:")
                    if type(dia)==float:
                        dia = int(dia)
                        if 0<dia<31:
                            dia=str(dia)
                            a=False
                        else:
                            messagebox.showinfo("Error", "Ingrese un dia correcto.")
                    else:
                        messagebox.showinfo("Error", "Ingrese un dia correcto.")
                a=True
                while a:
                    mes = simpledialog.askfloat("Ingresar", "Por favor, ingrese el mes de visita:")
                    if type(mes)==float:
                        mes = int(mes)
                        if 0<mes<13:
                            mes=str(mes)
                            a=False
                        else:
                            messagebox.showinfo("Error", "Ingrese un mes correcto.")
                    else:
                        messagebox.showinfo("Error", "Ingrese un mes correcto.")
                a=True
                while a:
                    año = simpledialog.askfloat("Ingresar", "Por favor, ingrese el año de la visita:")
                    if type(año)==float:
                        año = int(año)
                        if 1990<año<2050:
                            año=str(año)
                            a=False
                        else:
                            messagebox.showinfo("Error", "Ingrese un año correcto.")
                    else:
                        messagebox.showinfo("Error", "Ingrese un año correcto.")
                if int(base_de_datos[3][id_mascota][13]) < int(año):
                    base_de_datos[3][id_mascota][11] = dia
                    base_de_datos[3][id_mascota][12] = mes
                    base_de_datos[3][id_mascota][13] = año
                    base_de_datos[2][id_cliente][6] = dia
                    base_de_datos[2][id_cliente][7] = mes
                    base_de_datos[2][id_cliente][8] = año
                    visita=False
                elif int(base_de_datos[3][id_mascota][13]) == int(año):
                    if int(base_de_datos[3][id_mascota][12]) < int(mes):
                        base_de_datos[3][id_mascota][11] = dia
                        base_de_datos[3][id_mascota][12] = mes
                        base_de_datos[3][id_mascota][13] = año
                        base_de_datos[2][id_cliente][6] = dia
                        base_de_datos[2][id_cliente][7] = mes
                        base_de_datos[2][id_cliente][8] = año
                        visita=False
                    elif int(base_de_datos[3][id_mascota][12]) == int(mes):
                        base_de_datos[3][id_mascota][11] = dia
                        base_de_datos[3][id_mascota][12] = mes
                        base_de_datos[3][id_mascota][13] = año
                        base_de_datos[2][id_cliente][6] = dia
                        base_de_datos[2][id_cliente][7] = mes
                        base_de_datos[2][id_cliente][8] = año
                        visita=False
                    else:
                        messagebox.showinfo("Error", "La fecha no es valida")
                else:
                    messagebox.showinfo("Error", "La fecha no es valida")
            a = True
            while a:
                cod = simpledialog.askfloat("Ingresar codigo", "Ingrese el código del tratamiento:")
                if type(cod)==float:
                    cod = str(int(cod))
                    for i in range(len(base_de_datos[5])):
                        if cod == base_de_datos[5][i][0]:
                            a = False
                            medicamento = base_de_datos[5][i][1]
                            costo = int(base_de_datos[5][i][2])
                            valida_cantidad = base_de_datos[5][i]
                    if a:
                        messagebox.showinfo("Error", "No se encontró el codigo del tratamiento.")                         
            disponible=int(valida_cantidad[3])
            if disponible == 0:
                messagebox.showinfo("Error", "No quedan mas medicamentos de este tipo en el almacen")
            else:
                a=True
                while a:
                    cantidad = simpledialog.askfloat("Ingresar cantidad", "Ingrese la cantidad de medicamentos deseados:")
                    if type(cantidad)==float:
                        cantidad = int(cantidad)
                        if cantidad > disponible:
                            messagebox.showinfo("Error", f"No hay suficientes medicamentos, solo quedan {disponible} disponibles.")
                        else:
                            a=False
                            ad=1
                            disponible = disponible - cantidad
                            for i in range(len(base_de_datos[5])):
                                if base_de_datos[5][i]==valida_cantidad:
                                    base_de_datos[5][i][3]=str(disponible)
        if sf==1 and ad==1:
            plata=(costo*cantidad)
            messagebox.showinfo("Nueva medicacion", f"La medicacion se agegró exitosamente:\n[{idanimal},{med},{dia},{mes},{año},{cod},{costo},{cantidad},{plata}]")
            base.append([idanimal,med,dia,mes,año,cod,costo,cantidad, (costo*cantidad)])
            base_de_datos[6] = base
            base_de_datos[-1] = abre_facturas(base_de_datos[2],base_de_datos[6],base_de_datos[3])





