from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
from Funciones import *
from collections import Counter
from tkinter import simpledialog
    
def reportes(base): #Este se encarga de mostrar la ventana de reportes
    def b(base): #Solicita el código de un país para imprimir la lista de ciudades en ese pais
        a = True
        cp=0
        with open("Reportes/Reporte - Ciudades", "w") as f:
            f.write("Las ciudades registradas son: \n")
            while a:
                c_pais = simpledialog.askfloat("Ingresar codigo", "Por favor, ingresa un codigo de pais:")
                cod_pais = str(int(c_pais))
                for i in range(len(base[1])):
                    if base[1][i][0]==cod_pais:
                        a = False
                        f.write(f"{base[1][i][1]} - {base[1][i][2]}\n")
                        cp=1
                if a:
                    ok = messagebox.askokcancel("Operación cancelada", "No se encontro ningun ciudad con ese codigo\no el pais no existe.\nDesea probar otro codigo?")
                    if not ok:
                        a=False
                        v_reportes.lift()
        if cp==1:
            messagebox.showinfo("Reporte de ciudades por codigo pais", "El reporte se genero exitosamente")
            v_reportes.lift()

    def d(base):#Solicita el código de un cliente para imprimir la lista de mascotas del cliente
        mp=0
        a = True
        while a:
            valido = False
            identificacion = simpledialog.askfloat("Ingresar codigo","Ingrese el código del cliente.")
            identificacion = str(int(identificacion))
            for i in range(len(base[2])):
                if base[2][i][0]==identificacion:
                    valido = True
                    id_cliente = i
            if valido:
                a = False
                mp=1
            else:
                ok = messagebox.askokcancel("Operación cancelada", "No se encontro ningun mascota con ese codigo o el cliente no existe.\nDesea probar otro codigo?")
                if not ok:
                    a=False
                    v_reportes.lift()
        if mp==1:
            with open("Reportes/Reporte - Mascotas", "w") as f:
                f.write(f"Las mascotas registradas al cliente {base[2][id_cliente][1]} son: \n")
                for k in range(len(base[3])):
                    if base[3][k][0] == base[2][id_cliente][0]:
                        f.write(f"{base[3][k][1]} - {base[3][k][2]}\n")
        if mp==1:
            messagebox.showinfo("Reporte de mascota por codigo cliente", "El reporte se genero exitosamente")
            v_reportes.lift()

    def e(base):
        a = True
        op=0
        while a:#Imprime visitas de una mascota
            carne = simpledialog.askfloat("Ingresar codigo","Ingrese el ID del animal.")
            carne = str(int(carne))
            for i in range(len(base[3])):
                if base[3][i][1]==carne:
                    a = False
                    with open("Reportes/Reporte - Visitas", "w") as f:
                        f.write(f"Las visitas registradas a la mascota {base[3][i][2]} son: \n")
                        for k in range(len(base[4])):
                            if base[4][k][1] == base[3][i][1]:
                                op=1
                                f.write(f"La visita {base[4][k][0]} \n")
            if a:
                ok = messagebox.askokcancel("Operación cancelada", "No se encontro ningun Id asociado.\nDesea probar otro codigo?")
                if not ok:
                    a=False
                    v_reportes.lift()
        if op==1:
            messagebox.showinfo("Reporte de visitas de una mascota", "El reporte se genero exitosamente")
            v_reportes.lift()

    def g(base):#Imprime Tratamiento de una mascota
        a = True
        ap=0
        while a:
            identificacion = simpledialog.askfloat("Ingresar codigo","Ingrese el Id mascota.")
            identificacion = str(int(identificacion))
            for i in range(len(base[3])):
                if base[3][i][1]==identificacion:
                    a = False
                    
                    id_cliente = i
                    ap=1
            if a:
                ok = messagebox.askokcancel("Operación cancelada", "No se encontro ningun Id asociado.\nDesea probar otro codigo?")
                if not ok:
                    a=False
                    v_reportes.lift()
        if ap==1:
            for j in range(len(base[6])):
                if base[6][j][0] == identificacion:
                    with open("Reportes/Reporte - Tratamiento de una mascota", "w") as f:
                        f.write(f"Los medicamentos de {base[3][id_cliente][2]}: \n")
                        f.write(f"Código de medicación: {base[6][j][1]}\n")
                        f.write(f"Lista de medicamentos: {base[6][j][5]}")
        if ap==1:
            messagebox.showinfo("Reporte de Tratamiento de mascota", "El reporte se genero exitosamente")
            v_reportes.lift()

    v_reportes = Tk()
    v_reportes.title("Reportes solicitados")
    v_reportes.geometry("440x450")
    v_reportes.lift()

    repo = Label(v_reportes,text = "Seleccione el reporte\n que desea abrir:")
    repo.grid(row=1, column=2)

    ecio1 = Label(v_reportes,text = "  ")
    ecio1.grid(row=2, column=0)

    #Botones para abrir los reportes y registros
    def a(base): #Toda la lista de Paises
        is_ok = messagebox.askokcancel(title="Esta seguro de relizar el reporte?", message="El reporte de paises esta listo.\nDesea hacer el registro?")
        if is_ok:
            with open("Reportes/Reporte - Paises", "w") as f:
                f.write("Los paises registrados son:\n")
                for i in range(len(base[0])):
                    f.write(f"{base[0][i][0]} - {base[0][i][1]}\n")
            v_reportes.lift()
    r_pais=Button(v_reportes, text="Reporte\nPais", width=20,command=lambda:a(base))
    r_pais.grid(row=3, column=1)
        
    r_ciud=Button(v_reportes, text="Reporte\nCiudades de un pais", width=20,command=lambda:b(base))
    r_ciud.grid(row=4, column=1)
    
    def c(base): #Imprime toda la lista de clientes
        is_ok = messagebox.askokcancel(title="Esta seguro de relizar el reporte?", message="El reporte de clientes esta listo.\nDesea hacer el registro?")
        if is_ok:
            with open("Reportes/Reporte - Clientes", "w") as f:
                f.write("Los clientes registrados son:\n")
                for i in range(len(base[2])):
                    f.write(f"{base[2][i][0]} - {base[2][i][1]}\n")
        v_reportes.lift()
    r_clien=Button(v_reportes, text="Reporte\nClientes", width=20,command=lambda:c(base))
    r_clien.grid(row=5, column=1)

    r_masco=Button(v_reportes, text="Reporte\nMascota de un cliente", width=20,command=lambda:d(base))
    r_masco.grid(row=6, column=1)

    r_visi=Button(v_reportes, text="Reporte\nVisitas de una mascota", width=20,command=lambda:e(base))
    r_visi.grid(row=7, column=1)

    def f(base):#Imprime los reportes de tratamientos
        is_ok = messagebox.askokcancel(title="Esta seguro de relizar el reporte?", message="El reporte de los tratamientos\nesta listo.\nDesea hacer el registro?")
        if is_ok:
            with open("Reportes/Reporte - Tratamientos", "w") as f:
                f.write("Los tratamientos en la veterinaria son: \n")
                for i in range(len(base[5])):
                    f.write(f"{base[5][i][0]} - {base[5][i][1]} - {base[5][i][2]}  \n")
        v_reportes.lift()
    r_trat=Button(v_reportes, text="Reporte\nTratamientos", width=20,command=lambda:f(base))
    r_trat.grid(row=8, column=1)

    r_tratmasc=Button(v_reportes, text="Reporte\nTratamiento de una\nmascota", width=20,command=lambda:g(base))#
    r_tratmasc.grid(row=9, column=1)

    def h(base):#Imprime el cliente con mayor saldo
        is_ok = messagebox.askokcancel(title="Esta seguro de relizar el reporte?", message="El reporte de cliente con mas\nsaldo esta listo.\nDesea hacer el registro?")
        if is_ok:
            saldo = 0
            ubicacion = 0
            for i in range(len(base[2])):
                if int(base[2][i][-1])>saldo:
                    saldo = int(base[2][i][-1])
                    ubicacion = i
            with open("Reportes/Reporte - Mayor saldo", "w") as f:
                f.write(f"El cliente con mayor saldo es {base[2][ubicacion][1]} - ID: {base[2][ubicacion][0]} con {saldo}")
        v_reportes.lift()
    r_massueldo=Button(v_reportes, text="Reporte\nCliente con mas sueldo", width=20,command=lambda:h(base))
    r_massueldo.grid(row=3, column=3)

    def i(base):#Imprime clientes con crédito
        is_ok = messagebox.askokcancel(title="Esta seguro de relizar el reporte?", message="El reporte de cliente de credito \nesta listo.\nDesea hacer el registro?")
        if is_ok:
            with open("Reportes/Reporte - Crédito", "w") as f:
                f.write("Los clientes con crédito son: \n")
                for i in range(len(base[2])):
                    if int(base[2][i][-1])>0:
                        f.write(f"{base[2][i][1]} - ID: {base[2][i][0]} con {int(base[2][i][-1])} \n")
        v_reportes.lift()               
    r_credito=Button(v_reportes, text="Reporte\nCliente de credito", width=20,command=lambda:i(base))
    r_credito.grid(row=4, column=3)

    def j(base):#Imprime cliente con mayor descuento
        is_ok = messagebox.askokcancel(title="Esta seguro de relizar el reporte?", message="El reporte de cliente con mayor \ndescuento esta listo.\nDesea hacer el registro?")
        if is_ok:
            descuento = 0
            ubicacion = 0
            for i in range(len(base[2])):
                if int(base[2][i][-2])>descuento:
                    descuento = int(base[2][i][-2])
                    ubicacion = i
            with open("Reportes/Reporte - Mayor descuento", "w") as f:
                        f.write(f"El cliente con mayor descuento es {base[2][ubicacion][1]} - ID: {base[2][ubicacion][0]} con {descuento} %")
        v_reportes.lift()
    r_masdesc=Button(v_reportes, text="Reporte\nCliente con mas descuento", width=20,command=lambda:j(base))
    r_masdesc.grid(row=5, column=3)
    
    def k(base):#Imprime el último tratamiento añadido
        is_ok = messagebox.askokcancel(title="Esta seguro de relizar el reporte?", message="El reporte de ultimo tratamiento \nañadido esta listo.\nDesea hacer el registro?")
        if is_ok:
            for i in range(len(base[5])):
                with open("Reportes/Reporte - Útimo tratamiento", "w") as f:
                    f.write("El último tratamiento añadido fue: \n") 
                    f.write(f" {base[5][i][0]} - {base[5][i][1]} - {base[5][i][2]}  \n")
        v_reportes.lift()
    r_ultimo=Button(v_reportes, text="Reporte\nUltimo tratamiento", width=20,command=lambda:k(base))
    r_ultimo.grid(row=6, column=3)

    def l(base):
        is_ok = messagebox.askokcancel(title="Esta seguro de relizar el reporte?", message="El reporte de tratamiento mas\nutilizado esta listo.\nDesea hacer el registro?")
        if is_ok:
            elementos_comunes = []
            lista = base[6]
            for sublist in lista:
                elemento = sublist[5]
                elementos_comunes.append(elemento)

            elemento_mas_usado = Counter(elementos_comunes).most_common(1)[0][0]
            with open("Reportes/Reporte - Medicamento más usado", "w") as f:
                f.write(f"El codigo de medicamento más usado fue: {elemento_mas_usado}")
        v_reportes.lift()
    r_tratmasutil=Button(v_reportes, text="Reporte\nTratamiento mas utilizado", width=20,command=lambda:l(base))
    r_tratmasutil.grid(row=7, column=3)
    
    r_masfact=Button(v_reportes, text="Reporte\nCliente que mas facturo", width=20,command=lambda:reporte_factura(base))
    r_masfact.grid(row=8, column=3)

    ecio2 = Label(v_reportes,text = " ")
    ecio2.grid(row=10, column=0)



    def reporte_factura(base):
        facturas = base[-1]
        #determinar la factura más alta:
        alto = facturas[0][1][0]
        for i in range(len(facturas)):
            for k in range(len(facturas[i][1])):
                if facturas[i][1][k][-2]>alto[-2]:
                    alto = facturas[i][1][k]

        is_ok = messagebox.askokcancel(title="Esta seguro de relizar el reporte?", message="El reporte de Mayor Factura \nestá listo.\nDesea hacer el registro?")
        if is_ok: #factura1 = [Cédula del cliente(0), Nombre(1), Id Mascota(2), NombreMedi(3), costo(4), cantidad(5), total(6), id factura(7)]
            with open("Reportes/Reporte - Mayor Factura", "w") as f:
                f.write(f"Factura: {alto[7]} \n")
                f.write(f"Fecha: {alto[8]}/{alto[9]}/{alto[10]} \n")
                f.write(f"Cédula del cliente: {alto[0]} \n")
                f.write(f"Nombre del la mascota: {alto[1]} \n")
                f.write(f"Id de la mascota: {alto[2]} \n")
                f.write(f"Nombre de la medicina: {alto[3]} \n")
                f.write(f"Costo Unitario: {alto[4]} \n")
                f.write(f"Unidades compradas: {alto[5]} \n")
                f.write(f"Total a cancelar: {alto[6]}")
        v_reportes.lift()


    
    cerrar=Button(v_reportes, text="Cerrar", width=15,command=lambda:v_reportes.destroy())
    cerrar.grid(row=11, column=2)
    v_reportes.mainloop()


