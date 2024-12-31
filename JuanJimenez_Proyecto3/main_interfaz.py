import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from lectura import *
from Reportes import *
from Contactos import abri_cont
from Acerca_de import mostrar_empresa
from Facturar import facturar
from Redes import redes
from Insertar import insercion
from Busqueda import buscar
from Eliminar import eliminar
from Modificar import *
from Facturas import factura

base=base_de_datos()    

def mantenimiento(num):#2=pais #3=ciudad #4=cliente #5=mascota #6=visita #7=tratamiento #8=medicamento 
    v_mantenimiento = Toplevel(VentanaPrincipal)
    v_mantenimiento.title("Mantenimiento")
    v_mantenimiento.geometry("345x220")
    v_mantenimiento.lift()
    
    mante = Label(v_mantenimiento,text = "Que desea hacer?")               
    mante.grid(row=1, column=0)
    espacio2 = Label(v_mantenimiento,text = " ")               
    espacio2.grid(row=2, column=0)

    #Botones para abrir los mantenimiento
    r_pais=Button(v_mantenimiento, text="Insercion", width=15,command=lambda:insercion(num,base))
    r_pais.grid(row=3, column=1)
    r_ciud=Button(v_mantenimiento, text="Modificacion", width=15,command=lambda:modificar(num,base))
    r_ciud.grid(row=4, column=1)
    r_clien=Button(v_mantenimiento, text="Consulta\n(Busquedas)", width=15,command=lambda:buscar(num,base))
    r_clien.grid(row=5, column=1)
    r_masco=Button(v_mantenimiento, text="Eliminacion", width=15,command=lambda:eliminar(num,base))
    r_masco.grid(row=6, column=1)
    
    espacio1 = Label(v_mantenimiento,text = " ")               
    espacio1.grid(row=7, column=0)
    #Boton de cerrar
    cerrar=Button(v_mantenimiento, text="Cerrar", width=15,command=lambda:v_mantenimiento.destroy())
    cerrar.grid(row=8, column=1)
    v_mantenimiento.mainloop()

def barra_mant():
    pre_mant = Toplevel(VentanaPrincipal)
    pre_mant.title("Mantenimiento")
    pre_mant.geometry("345x220")
    pre_mant.lift()
    
    mante = Label(pre_mant,text = "Que desea hacer?")               
    mante.grid(row=1, column=0)
    espacio2 = Label(pre_mant,text = " ")               
    espacio2.grid(row=2, column=0)

    #Botones para abrir los mantenimiento
    r_pais=Button(pre_mant, text="Insercion", width=15,command=lambda:eleccion(1,insercion))
    r_pais.grid(row=3, column=1)
    r_ciud=Button(pre_mant, text="Modificacion", width=15,command=lambda:eleccion(1,modificar))
    r_ciud.grid(row=4, column=1)
    r_clien=Button(pre_mant, text="Consulta\n(Busquedas)", width=15,command=lambda:eleccion(1,buscar))
    r_clien.grid(row=5, column=1)
    r_masco=Button(pre_mant, text="Eliminacion", width=15,command=lambda:eleccion(1,eliminar))
    r_masco.grid(row=6, column=1)
    

    espacio1 = Label(pre_mant,text = " ")               
    espacio1.grid(row=7, column=0)
    cerrar=Button(pre_mant, text="Cerrar", width=15,command=lambda:pre_mant.destroy())
    cerrar.grid(row=8, column=1)
    pre_mant.mainloop()

def eleccion(num,donde):
    v_eleccion = Toplevel(VentanaPrincipal)
    v_eleccion.title("Mantenimiento")
    v_eleccion.geometry("370x350")
    v_eleccion.lift()

    elec = Label(v_eleccion,text = "Elija donde va a\nrelizar mantenimiento:")               
    elec.grid(row=0, column=2)
    espacio1 = Label(v_eleccion,text = " ")               
    espacio1.grid(row=1, column=0)

    if num==1:
        pais=Button(v_eleccion, text="Pais", width=15, command=lambda:donde(2,base))
        pais.grid(row=2, column=1)
        esp1 = Label(v_eleccion,text = " ")               
        esp1.grid(row=3, column=0)
        
        ciudad=Button(v_eleccion, text="Ciudad", width=15,command=lambda:donde(3,base))
        ciudad.grid(row=2, column=3)

        clientes=Button(v_eleccion, text="Clientes", width=15,command=lambda:donde(4,base))
        clientes.grid(row=4, column=1)
        esp2 = Label(v_eleccion,text = " ")               
        esp2.grid(row=5, column=0)
        
        mascotas=Button(v_eleccion, text="Mascotas", width=15,command=lambda:donde(5,base))
        mascotas.grid(row=4, column=3)
        
        visitas=Button(v_eleccion, text="Visitas", width=15,command=lambda:donde(6,base))
        visitas.grid(row=6, column=1)
        
        tratamientos=Button(v_eleccion, text="Tratamientos", width=15,command=lambda:donde(7,base))
        tratamientos.grid(row=6, column=3)
        esp4 = Label(v_eleccion,text = " ")               
        esp4.grid(row=7, column=0)
        
        medicamentos=Button(v_eleccion, text="Medicamentos", width=15,command=lambda:donde(8,base))
        medicamentos.grid(row=8, column=2)
       

    if num==2:
        pais=Button(v_eleccion, text="Pais", width=15,command=lambda:mantenimiento(2))
        pais.grid(row=3, column=1)
        i_pais = Image.open("imagenes/icon_pais.png")
        i_pais = i_pais.resize((40, 40))
        i_pais_tk = ImageTk.PhotoImage(i_pais)
        etiqueta_pais = Label(v_eleccion,image=i_pais_tk)
        etiqueta_pais.grid(row=3, column=2)
        esp1 = Label(v_eleccion,text = " ")               
        esp1.grid(row=4, column=0)
        
        ciudad=Button(v_eleccion, text="Ciudad", width=15,command=lambda:mantenimiento(3))
        ciudad.grid(row=5, column=1)
        i_ciudad = Image.open("imagenes/icon_ciudad.png")
        i_ciudad = i_ciudad.resize((40, 40))
        i_ciudad_tk = ImageTk.PhotoImage(i_ciudad)
        etiqueta_ciudad = Label(v_eleccion,image=i_ciudad_tk)
        etiqueta_ciudad.grid(row=5, column=2)
        
    elif num==3:
        clientes=Button(v_eleccion, text="Clientes", width=15,command=lambda:mantenimiento(4))
        clientes.grid(row=3, column=1)
        i_clientes = Image.open("imagenes/icon_cliente.png")
        i_clientes = i_clientes.resize((40, 40))
        i_clientes_tk = ImageTk.PhotoImage(i_clientes)
        etiqueta_clientes = Label(v_eleccion,image=i_clientes_tk)
        etiqueta_clientes.grid(row=3, column=2)
        esp2 = Label(v_eleccion,text = " ")               
        esp2.grid(row=4, column=0)
        
        mascotas=Button(v_eleccion, text="Mascotas", width=15,command=lambda:mantenimiento(5))
        mascotas.grid(row=5, column=1)
        i_mascotas = Image.open("imagenes/icon_mascota.png")
        i_mascotas = i_mascotas.resize((40, 40))
        i_mascotas_tk = ImageTk.PhotoImage(i_mascotas)
        etiqueta_mascotas = Label(v_eleccion,image=i_mascotas_tk)
        etiqueta_mascotas.grid(row=5, column=2)
        esp3 = Label(v_eleccion,text = " ")               
        esp3.grid(row=6, column=0)
        
        visitas=Button(v_eleccion, text="Visitas", width=15,command=lambda:mantenimiento(6))
        visitas.grid(row=7, column=1)
        i_visitas = Image.open("imagenes/icon_visita.png")
        i_visitas = i_visitas.resize((40, 40))
        i_visitas_tk = ImageTk.PhotoImage(i_visitas)
        etiqueta_visitas = Label(v_eleccion,image=i_visitas_tk)
        etiqueta_visitas.grid(row=7, column=2)
        
    elif num==4:
        tratamientos=Button(v_eleccion, text="Tratamientos", width=15,command=lambda:mantenimiento(7))
        tratamientos.grid(row=3, column=1)
        i_tratamientos = Image.open("imagenes/icon_tratamiento.png")
        i_tratamientos = i_tratamientos.resize((40, 40))
        i_tratamientos_tk = ImageTk.PhotoImage(i_tratamientos)
        etiqueta_tratamientos = Label(v_eleccion,image=i_tratamientos_tk)
        etiqueta_tratamientos.grid(row=3, column=2)
        esp4 = Label(v_eleccion,text = " ")               
        esp4.grid(row=4, column=0)
        
        medicamentos=Button(v_eleccion, text="Medicamentos", width=15,command=lambda:mantenimiento(8))
        medicamentos.grid(row=5, column=1)
        i_medicamentos = Image.open("imagenes/icon_medica.png")
        i_medicamentos = i_medicamentos.resize((40, 40))
        i_medicamentos_tk = ImageTk.PhotoImage(i_medicamentos)
        etiqueta_medicamentos = Label(v_eleccion,image=i_medicamentos_tk)
        etiqueta_medicamentos.grid(row=5, column=2)

    espacio2 = Label(v_eleccion,text = " ")               
    espacio2.grid(row=10, column=0)
    cerrar=Button(v_eleccion, text="Cerrar", width=15,command=lambda:v_eleccion.destroy())
    cerrar.grid(row=11, column=2)

    v_eleccion.mainloop()
    
VentanaPrincipal = Tk()#Ventana principal
VentanaPrincipal.title("Veterinaria la pulguita")
alto = 500
ancho = 500
VentanaPrincipal.geometry(str(alto)+"x"+str(ancho))
VentanaPrincipal.config(bg="#48C9B0")


    
lplace = Image.open("imagenes/lugpro.png")
lplace = lplace.resize((180, 160))
lplace_tk = ImageTk.PhotoImage(lplace)
btn_lugares = Button(VentanaPrincipal, image=lplace_tk, highlightthickness=0, highlightbackground="#48C9B0",borderwidth=2,bg="#48C9B0",fg="#48C9B0",command=lambda:eleccion(2,0))           
btn_lugares.place(x=30,y=30)
lug = Label(VentanaPrincipal,text = "Lugares")
lug.place(x= 100,y=170)
lug.config(bg="white")

persona = Image.open("imagenes/persona.png")
persona = persona.resize((180, 160))
persona_tk = ImageTk.PhotoImage(persona)
btn_clientes = Button(VentanaPrincipal,image=persona_tk, highlightthickness=0, highlightbackground="#48C9B0",borderwidth=2,bg="#48C9B0",fg="#48C9B0",command=lambda:eleccion(3,0))
btn_clientes.place(x=260,y=30)
client = Label(VentanaPrincipal,text = "Clientes")
client.place(x= 330,y=170)
client.config(bg="white")


perro = Image.open("imagenes/perro.jpg")
perro = perro.resize((180, 160))
perro_tk = ImageTk.PhotoImage(perro)
btn_clinica = Button(VentanaPrincipal,image=perro_tk, highlightthickness=0, highlightbackground="#48C9B0",borderwidth=2,bg="#48C9B0",fg="#48C9B0",command=lambda:eleccion(4,0))
btn_clinica.place(x=30,y=260)
clinic = Label(VentanaPrincipal,text = "Clinica")
clinic.place(x= 100,y=400)
clinic.config(bg="white")

pagos = Image.open("imagenes/pagos.jpg")
pagos = pagos.resize((180, 160))
pagos_tk = ImageTk.PhotoImage(pagos)
btn_clientes = Button(VentanaPrincipal,image=pagos_tk, highlightthickness=0, highlightbackground="#48C9B0",borderwidth=2,bg="#48C9B0",fg="#48C9B0",command=lambda:facturar(VentanaPrincipal,base))   
btn_clientes.place(x=260,y=260)
fact = Label(VentanaPrincipal,text = "Facturacion")
fact.place(x= 318,y=400)
fact.config(bg="white")

#Menu barra
menuV = Menu(VentanaPrincipal)
menuV.add_command(label = "Mantenimiento",command=lambda:barra_mant())
menuV.add_command(label="Registros",command=lambda:reportes(base))
menuV.add_command(label="Facturacion",command=lambda:facturar(VentanaPrincipal,base))
menuV.add_command(label="Acerca de",command=lambda:mostrar_empresa(VentanaPrincipal))
menuV.add_command(label="Contacto", command=lambda:abri_cont())

VentanaPrincipal.config(menu=menuV)

insta = Image.open("imagenes/instagram.jpg")
insta = insta.resize((30, 30))
insta_tk = ImageTk.PhotoImage(insta)
btn_insta = Button(VentanaPrincipal,image=insta_tk, highlightthickness=0, highlightbackground="#48C9B0",borderwidth=2,bg="#48C9B0",fg="#48C9B0",command=lambda:redes(VentanaPrincipal,1))#command...   
btn_insta.place(x=30,y=450)

face = Image.open("imagenes/facebook.jpg")
face = face.resize((30, 30))
face_tk = ImageTk.PhotoImage(face)
btn_face = Button(VentanaPrincipal,image=face_tk, highlightthickness=0, highlightbackground="#48C9B0",borderwidth=2,bg="#48C9B0",fg="#48C9B0",command=lambda:redes(VentanaPrincipal,2))#command...   
btn_face.place(x=80,y=450)

twitter = Image.open("imagenes/twitter.jpg")
twitter = twitter.resize((30, 30))
twitter_tk = ImageTk.PhotoImage(twitter)
btn_twitter = Button(VentanaPrincipal,image=twitter_tk,highlightthickness=0, highlightbackground="#48C9B0",borderwidth=2,bg="#48C9B0",fg="#48C9B0",command=lambda:redes(VentanaPrincipal,3))#command...   
btn_twitter.place(x=130,y=450)

def cerrartodo():
    VentanaPrincipal.destroy()
    sys.exit()
cerrar=Button(VentanaPrincipal, text="Cerrar", width=25,command=lambda:cerrartodo())
cerrar.place(x= 260,y=460)


VentanaPrincipal.mainloop()
