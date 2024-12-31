from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

def redes(VentanaPrincipal,num):
    social = Toplevel(VentanaPrincipal)#Ventana principal
    social.title("Veterinaria la pulguita (Redes)")
    social.geometry("400x200")
    social.lift()
    
    esp = Label(social,text="  ")
    esp.grid(row=1, column=0)
    
    if num==1:
        label1 = Label(social,text="Elija el instagram:")
        label1.grid(row=0, column=2)
        ig_jd = Label(social,text="Juan D. Jimenez -->")
        ig_jd.grid(row=2, column=1)
        b_igjd = Button(social, text="Instagram", width=15,command=lambda:webbrowser.open("https://www.instagram.com/juan_d_jv/"))
        b_igjd.grid(row=2, column=2)
        
        esp2 = Label(social,text="  ")
        esp2.grid(row=3, column=0)
        ig_mc = Label(social,text="Miguel Cubero   -->")
        ig_mc.grid(row=4, column=1)
        b_igmc = Button(social, text="Instagram", width=15,command=lambda:webbrowser.open("https://www.instagram.com/migue.cubero/"))
        b_igmc.grid(row=4, column=2)

        
    elif num==2:
        label2 = Label(social,text="Elija el Facebook:")
        label2.grid(row=0, column=2)
        fc_jd = Label(social,text="Juan D. Jimenez -->")
        fc_jd.grid(row=2, column=1)
        b_fcjd = Button(social, text="Facebook", width=15,command=lambda:webbrowser.open("https://www.facebook.com/profile.php?id=100007053911546"))
        b_fcjd.grid(row=2, column=2)
        
        esp2 = Label(social,text="  ")
        esp2.grid(row=3, column=0)
        fc_mc = Label(social,text="Miguel Cubero   -->")
        fc_mc.grid(row=4, column=1)
        b_fcmc = Button(social, text="Facebook", width=15,command=lambda:messagebox.showinfo("Facebook","No posee Facebook."))
        b_fcmc.grid(row=4, column=2)
        
    else:
        label3 = Label(social,text="Elija el Twitter:")
        label3.grid(row=0, column=2)
        t_jd = Label(social,text="Juan D. Jimenez -->")
        t_jd.grid(row=2, column=1)
        b_tjd = Button(social, text="Twitter", width=15,command=lambda:webbrowser.open("https://twitter.com/JuanDiegoJimne1"))
        b_tjd.grid(row=2, column=2)
        
        esp2 = Label(social,text="  ")
        esp2.grid(row=3, column=0)
        t_mc = Label(social,text="Miguel Cubero   -->")
        t_mc.grid(row=4, column=1)
        b_tmc = Button(social, text="Twitter", width=15,command=lambda:webbrowser.open("https://twitter.com/cubero1412"))
        b_tmc.grid(row=4, column=2)

    espac = Label(social,text="  ")
    espac.grid(row=6, column=0)
    cerrar = Button(social, text="Cerrar", width=15,command=lambda:social.destroy())
    cerrar.grid(row=7,column=2)


    social.mainloop()
