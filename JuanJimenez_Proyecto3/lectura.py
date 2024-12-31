def base_de_datos():
    a = [abre_validado_pais(), abre_validado_ciudad(),abre_validado_clientes(), abre_validado_mascotas(), abre_validado_fechas_nacimiento(),abre_validado_tratamientos(), abre_validado_medicacion(),abre_facturas(abre_validado_clientes(),abre_validado_medicacion(),abre_validado_mascotas())]
    return a

def abrir():#Solo lee archivos y retorna
    valid = True
    while valid:
        nombre = input("Nombre del archivo que desea abrir: ").lower()
        try:
            with open(f"{nombre}.txt", "r") as file:
                file=file.read()
                datos=file.split('\n')
                data=[]
                i=0
                while i < len(datos):
                    if datos[i] != '':
                        data+=[datos[i].split(";")]
                    i+=1
                return [data,nombre]
            valid=False
        except FileNotFoundError:
            print("El archivo no existe, verifique que el archivo está en el mismo directorio que el programa, y omita su extensión")


def abre_validado_pais():
    with open("Archivos/paises.txt", "r") as file:
        file=file.read()
        datos=file.split('\n')
        data=[]
        i=0
        while i < len(datos):
            if datos[i] != '':
                data+=[datos[i].split(";")]
            i+=1
        valida = valida_repetidos(data,"paises")
        return valida #Estos son los datos de pais que se van a usar para validar las demas listas

def abre_validado_ciudad():
    with open("Archivos/ciudades.txt", "r") as file:
        file=file.read()
        datos=file.split('\n')
        data=[]
        i=0
        while i < len(datos):
            if datos[i] != '':
                data+=[datos[i].split(";")]
            i+=1
        valida = valida_repetidos(data,"ciudades")
        p_valid = abre_validado_pais()
        lista_temp=[]
        for i in range(len(valida)):
            for j in range(len(p_valid)):
                if valida[i][0] not in p_valid[j][0]:
                    pass
                else:
                    lista_temp+=[valida[i]]
        valida = lista_temp
        return valida
            
def abre_validado_clientes():
    with open("Archivos/Clientes.txt", "r") as file:
                file=file.read()
                datos=file.split('\n')
                data=[]
                i=0
                while i < len(datos):
                    if datos[i] != '':
                        data+=[datos[i].split(";")]
                    i+=1
    valida = valida_repetidos(data,"clientes")
    c_valido = abre_validado_ciudad()
    temp2=[]
    for i in range(len(valida)):
        for j in range(len(c_valido)):
                if valida[i][3] == c_valido[j][0] and valida[i][4]==c_valido[j][1]:
                    temp2+=[valida[i]]
    valida = temp2
    valida = valida_fechas(valida, "clientes")    
    return valida

def abre_validado_mascotas():
    with open("Archivos/mascotas.txt", "r") as file:
                file=file.read()
                datos=file.split('\n')
                data=[]
                i=0
                while i < len(datos):
                    if datos[i] != '':
                        data+=[datos[i].split(";")]
                    i+=1
    valida=[]
    c_valido = abre_validado_clientes()
    for i in range(len(data)):
        for j in range(len(c_valido)):
            if data[i][0] == c_valido[j][0]:
                    valida+=[data[i]]
    valida = valida_repetidos(valida, "mascotas")
    valida = valida_fechas(valida, "mascotas")
    valida = valida_fecha_animal_ultima(valida)
    return valida

def valida_fecha_animal_ultima(data):
    v_mascota=[]
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                if data[i][7] < data[j][13]:
                    v_mascota+=[data[i]]
                elif data[i][7] == data[j][13] and data[i][6] < data[j][12]:
                    v_mascota+=[data[i]]
                elif data[i][6] == data[j][12] and data[i][5] <= data[j][11]:
                    v_mascota+=[data[i]]
                else:
                    pass
    return v_mascota

def abre_validado_visitas():
    with open("Archivos/visitas.txt", "r") as file:
                file=file.read()
                datos=file.split('\n')
                data=[]
                i=0
                while i < len(datos):
                    if datos[i] != '':
                        data+=[datos[i].split(";")]
                    i+=1
    data = valida_repetidos(data, "visitas")
    m_valido = abre_validado_mascotas()
    valida = []
    for i in range(len(data)):
        for j in range(len(m_valido)):
            if data[i][1] == m_valido[j][1]:
                valida+=[data[i]]
    valida = valida_fechas(valida, "visitas")    
    return valida

def abre_validado_tratamientos():
    with open("Archivos/tratamiento.txt", "r") as file:
                file=file.read()
                datos=file.split('\n')
                data=[]
                i=0
                while i < len(datos):
                    if datos[i] != '':
                        data+=[datos[i].split(";")]
                    i+=1
    valido = valida_repetidos(data,"tratamiento")    
    return valido

def abre_validado_medicacion():
    with open("Archivos/medicacion.txt", "r") as file:
                file=file.read()
                datos=file.split('\n')
                data=[]
                i=0
                while i < len(datos):
                    if datos[i] != '':
                        data+=[datos[i].split(";")]
                    i+=1
    data = valida_repetidos(data,"medicacion")
    m_valido = abre_validado_mascotas()
    valida=[]
    for i in range(len(data)):
        for j in range(len(m_valido)):
            if data[i][0]==m_valido[j][1]:
                valida+=[data[i]]
    t_valido = abre_validado_tratamientos()
    v_lida=[]
    for i in range(len(valida)):
        for j in range(len(t_valido)):
            if valida[i][5]==t_valido[j][0]:
                v_lida+=[valida[i]]
    valida=v_lida
    valida = valida_fechas(valida, "visitas")    
    return valida    

def valida_repetidos(data,nombre): #Este sirve para hacer validaciones de repetidos para las primeras 7 validaciones
    lista_temp=[]
    valida=[]
    if nombre == "paises" or nombre == "visitas" or nombre == "tratamiento":
        for i in range(len(data)):
            if i in lista_temp:
                pass
            else:
                for j in range(len(data)):
                    if i == j:
                        pass
                    elif data[i][0] == data[j][0]:
                        a=0
                        while a<len(data):
                            if data[a]==data[j]:
                                lista_temp+=[a]
                            a+=1
                valida+=[data[i]]
    elif nombre == "ciudades" : #Quita los codigos iguales de ciudad iguales en el mismo pais
        for i in range(len(data)):
            if i in lista_temp:
                pass
            else:
                for j in range(len(data)):
                    if i == j:
                        pass
                    elif data[i][1] == data[j][1] and data[i][0]!=data[j][0]:
                        pass
                    elif data[i][1] == data[j][1] and data[i][0]==data[j][0]:
                        a=0
                        while a<len(data):
                            if data[a]==data[j]:
                                lista_temp+=[a]
                            a+=1
                valida+=[data[i]]
    elif nombre == "clientes":
        for i in range(len(data)):
            if i in lista_temp:
                pass
            else:
                for j in range(len(data)):
                    if i == j:
                        pass
                    elif data[i][0] == data[j][0]:
                        a=0
                        while a<len(data):
                            if data[a]==data[j]:
                                lista_temp+=[a]
                            a+=1
                valida+=[data[i]]      
    elif nombre == "mascotas":
        for i in range(len(data)):
            if i in lista_temp:
                pass
            else:
                for j in range(len(data)):
                    if i == j:
                        pass
                    elif data[i][1] == data[j][1]:
                        a=0
                        while a<len(data):
                            if data[a]==data[j]:
                                lista_temp+=[a]
                            a+=1
                valida+=[data[i]]
    elif nombre == "medicacion":
        for i in range(len(data)):
            if i in lista_temp:
                pass
            else:
                for j in range(len(data)):
                    if i == j:
                        pass
                    elif data[i][1] == data[j][1] and data[i][0]==data[j][0]:
                        if data[i][2] == data[j][2] and data[i][3] == data[j][3] and data[i][4] == data[j][4]:
                            a=0
                            while a<len(data):
                                if data[a]==data[j]:
                                    lista_temp+=[a]
                                a+=1
                valida+=[data[i]]
    return valida

#Esta hace que la fechaultimavisita debe ser posterior a fecha de nacimiento.
def abre_validado_fechas_nacimiento():
    f_visitas = abre_validado_visitas()
    f_nacimiento = abre_validado_mascotas()
    v_visita=[]
    v_animal=[]
    for i in range(len(f_visitas)):
        for j in range(len(f_nacimiento)):
            if f_visitas[i][1] == f_nacimiento[j][1]:
                if f_visitas[i][4] > f_nacimiento[j][7]:
                    v_visita+=[f_visitas[i]]
                elif f_visitas[i][4] == f_nacimiento[j][7]:
                    if f_visitas[i][3] > f_nacimiento[j][6]:
                        v_visita+=[f_visitas[i]]
                    elif f_visitas[i][3] == f_nacimiento[j][6]:
                        if f_visitas[i][2] > f_nacimiento[j][5]:
                            v_visita+=[f_visitas[i]]
                    else:
                        pass
    return v_visita
   
def abre_validacion_11_tratamiento():
    lista_temp=[]
    u_medicamento = abre_validado_medicacion()
    u_mascota = abre_validado_mascotas()
    for i in range(len(u_mascota)):
        for j in range(len(u_medicamento)):
            if u_mascota[i][1] == u_medicamento[j][0]:
                if u_mascota[i][11] == u_medicamento[j][2] and u_mascota[i][12] == u_medicamento[j][3] and u_mascota[i][13] == u_medicamento[j][4]:
                    lista_temp+=[u_medicamento[j]]#Aqui poner u_mascota[i] o u_medicamento[j] depende de lo que se pida.
    valida = lista_temp
    return valida
                
#Este solo muestra las personas que pagan con credito pero no trabaja con todos los datos,
#solo trabaja con los datos de validaciones hechas anteriormente.
def abre_validado_pago(): 
    p_mascotas = abre_validado_mascotas()
    p_visitas = abre_validado_fechas_nacimiento()
    p_cliente = abre_validado_clientes()
    valida=[]
    descuento=[]
    for i in range(len(p_visitas)):
        for j in range(len(p_mascotas)):
            if p_visitas[i][1] == p_mascotas[j][1]:
                if p_visitas[i][6] == '02':
                    asdf = 0
                    while asdf<len(p_cliente):
                        if p_mascotas[i][0] == p_cliente[asdf][0]:
                            valida += [p_cliente[i]]
                        asdf+=1
    return valida

def valida_fechas(datos, nombre):
    valida = []
    if nombre == "clientes":
        for i in range(len(datos)):
            if 0<int(datos[i][6])<32 and 0<int(datos[i][7])<13:
                valida+=[datos[i]]
    elif nombre == "mascotas":
        for i in range(len(datos)):
            if 0<int(datos[i][5])<32 and 0<int(datos[i][6])<13:
                if 0<int(datos[i][11])<32 and 0<int(datos[i][12])<13:
                    valida+=[datos[i]]
    elif nombre == "visitas" or nombre == "medicacion":
        for i in range(len(datos)):
            if 0<int(datos[i][2])<32 and 0<int(datos[i][3])<13:
                valida+=[datos[i]]
    return valida

def abre_facturas(clientes, medicacion, mascotas):
    contador = 1
    facturas = []
    #estructura de facturas [[[cliente,Estado],[factura1,factura2]],[otro]]   factura1 = [Cédula del cliente(0), Nombre(1), Id Mascota(2), NombreMedi(3), costo(4), cantidad(5), total(6), id factura(7),dia,fecha,año]
    
    #incluimos a todos los clientes a las facturas
    for i in range(len(clientes)):
        facturas = facturas + [[[clientes[i][0],False],[]]]
    
    for i in range(len(medicacion)):
        ide = medicacion[i][0]
        for j in range(len(mascotas)):
            if ide == mascotas[j][1]:
                id_cliente = mascotas[j][0]
                nombre = mascotas[j][2]
        for k in range(len(facturas)):           
            if facturas[k][0][0]==id_cliente:
                facturas[k][0][1] = True
                temp = [id_cliente,nombre,ide,medicacion[i][5],medicacion[i][6],medicacion[i][7],medicacion[i][8],contador,medicacion[i][2],medicacion[i][3],medicacion[i][4]]
                facturas[k][1] = facturas[k][1] + [temp]
                contador+=1
    return facturas
