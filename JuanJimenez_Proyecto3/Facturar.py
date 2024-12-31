from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from Facturas import factura

def facturar(VentanaPrincipal,base):
    v_fact = Toplevel(VentanaPrincipal)
    v_fact.title("Facturacion")
    v_fact.geometry("345x350")
    v_fact.lift()

    elec = Label(v_fact,text = "Elija que accion\ndesea realizar:")               
    elec.grid(row=1, column=0)
    espacio1 = Label(v_fact,text = " ")               
    espacio1.grid(row=2, column=0)

    saldos=Button(v_fact, text="Saldos", width=15,command=lambda:factura(2,base))
    saldos.grid(row=3, column=1)
    i_saldos = Image.open("imagenes/icon_saldo.png")
    i_saldos = i_saldos.resize((40, 40))
    i_saldos_tk = ImageTk.PhotoImage(i_saldos)
    etiqueta_saldos = Label(v_fact,image=i_saldos_tk)
    etiqueta_saldos.grid(row=3, column=2)
    esp4 = Label(v_fact,text = " ")               
    esp4.grid(row=4, column=0)
    
    descuentos=Button(v_fact, text="Descuentos", width=15,command=lambda:factura(3,base))
    descuentos.grid(row=5, column=1)
    i_descuentos = Image.open("imagenes/icon_descu.png")
    i_descuentos = i_descuentos.resize((40, 40))
    i_descuentos_tk = ImageTk.PhotoImage(i_descuentos)
    etiqueta_descuentos = Label(v_fact,image=i_descuentos_tk)
    etiqueta_descuentos.grid(row=5, column=2)
    esp4 = Label(v_fact,text = " ")               
    esp4.grid(row=6, column=0)
        
    facturacion=Button(v_fact, text="Facturacion", width=15,command=lambda:generar_factura(base[-1]))
    facturacion.grid(row=7, column=1)
    i_facturacion = Image.open("imagenes/icon_factura.png")
    i_facturacion = i_facturacion.resize((40, 40))
    i_facturacion_tk = ImageTk.PhotoImage(i_facturacion)
    etiqueta_facturacion = Label(v_fact,image=i_facturacion_tk)
    etiqueta_facturacion.grid(row=7, column=2)
    
    espacio2 = Label(v_fact,text = " ")               
    espacio2.grid(row=11, column=1)
    cerrar=Button(v_fact, text="Cerrar", width=15,command=lambda:v_fact.destroy())
    cerrar.grid(row=12, column=1)

    v_fact.mainloop()


import tkinter as tk
from tkinter import messagebox
def generar_factura(datos):
    def mostrar_factura():
        cliente = cliente_entry.get()
        factura_index = factura_var.get()

        if not cliente:
            messagebox.showerror("Error", "Ingrese el número de cliente")
            return

        # Buscar el cliente en los datos
        cliente_encontrado = False
        for cliente_data in datos:
            if cliente_data[0][0] == cliente:
                cliente_encontrado = True
                if cliente_data[0][1]:  # Verificar si el cliente tiene facturas
                    if factura_index < len(cliente_data[1]):
                        factura = cliente_data[1][factura_index]
                        cedula = factura[0]
                        nombre = factura[1]
                        id_mascota = factura[2]
                        nombre_medi = factura[3]
                        costo = factura[4]
                        cantidad = factura[5]
                        total = factura[6]
                        id_factura = factura[7]
                        dia = factura[8]
                        fecha = factura[9]
                        anio = factura[10]

                        # Mostrar la factura en una ventana 
                        messagebox.showinfo("Factura",
                                            f"Cédula del cliente: {cedula}\n"
                                            f"Nombre: {nombre}\n"
                                            f"ID Mascota: {id_mascota}\n"
                                            f"Nombre del Medicamento: {nombre_medi}\n"
                                            f"Costo: {costo}\n"
                                            f"Cantidad: {cantidad}\n"
                                            f"Total: {total}\n"
                                            f"ID Factura: {id_factura}\n"
                                            f"Día: {dia}\n"
                                            f"Fecha: {fecha}\n"
                                            f"Año: {anio}")
                    else:
                        messagebox.showerror("Error", "La factura seleccionada no existe")
                else:
                    messagebox.showinfo("Información", "El cliente no tiene facturas")
                break

        if not cliente_encontrado:
            messagebox.showerror("Error", "El número de cliente no existe")

    # Crear la ventana principal
    window = tk.Tk()
    window.title("Generador de Facturas")

    # Etiqueta y entrada para el número de cliente
    cliente_label = tk.Label(window, text="Número de cliente:")
    cliente_label.pack()
    cliente_entry = tk.Entry(window)
    cliente_entry.pack()

    # Buscar el cliente en los datos
    def buscar_cliente():
        cliente = cliente_entry.get()

        if not cliente:
            messagebox.showerror("Error", "Ingrese el número de cliente")
            return

        # Buscar el cliente en los datos
        cliente_encontrado = False
        cliente_facturas = None
        for cliente_data in datos:
            if cliente_data[0][0] == cliente:
                cliente_encontrado = True
                cliente_facturas = cliente_data[1]
                break

        if cliente_encontrado:
            if cliente_facturas:
                factura_dropdown['menu'].delete(0, 'end')  # Limpiar opciones anteriores

                for index, factura in enumerate(cliente_facturas):
                    id_factura = factura[7]
                    factura_dropdown['menu'].add_command(label=f"Factura {id_factura}", command=tk._setit(factura_var, index))
                
                factura_var.set(0)  
                factura_dropdown.configure(state='normal')
                generar_button.configure(state='normal')
            else:
                messagebox.showinfo("Información", "El cliente no tiene facturas")
                factura_dropdown.configure(state='disabled')
                generar_button.configure(state='disabled')
        else:
            messagebox.showerror("Error", "El número de cliente no existe")

    # Botón para buscar el cliente
    buscar_button = tk.Button(window, text="Buscar cliente", command=buscar_cliente)
    buscar_button.pack()

    # Lista desplegable para seleccionar la factura
    factura_label = tk.Label(window, text="Seleccionar factura:")
    factura_label.pack()
    factura_var = tk.IntVar()
    factura_dropdown = tk.OptionMenu(window, factura_var, "")
    factura_dropdown.pack()
    factura_dropdown.configure(state='disabled')

    # Botón para mostrar la factura
    generar_button = tk.Button(window, text="Generar factura", command=mostrar_factura)
    generar_button.pack()
    generar_button.configure(state='disabled')

    window.mainloop()
