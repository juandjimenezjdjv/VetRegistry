def descuento(precio):
    if precio<100000:
        desc = (precio*3) /100
    if precio>=100000 and precio<101000:
        desc = (precio*5) /100
    if precio>=101000:
        desc = (precio*10) /100
    return desc
    
def numero(argumento):
    a = True
    while a:
        try:
            num = int(input(argumento))
            return str(num)
        except ValueError:
            print("Ingrese un valor numérico válido.")

def numero_mate(argumento):
    a = True
    while a:
        try:
            num = int(input(argumento))
            return (num)
        except ValueError:
            print("Ingrese un valor numérico válido.")




def actualizar(archivo, lista):    
    data_str = []

    for sublist in lista:
        sublist_str = ','.join(sublist)  
        sublist_str = sublist_str.replace(',', ';') 
        data_str.append(sublist_str)

    with open(f"{archivo}.txt", 'w') as f:
        f.write('\n'.join(data_str))
    
def numero_dia(argumento):
    a = True
    while a:
        try:
            num = int(input(argumento))
            if num>0 and num<=31:
             return str(num)
            
            else:
                print("Ingrese un día válido.")
        except ValueError:
            print("Ingrese un valor numérico válido.")
            

def numero_mes(argumento):
    a = True
    while a:
        try:
            num = int(input(argumento))
            if num>0 and num<=12:
                return str(num)
            else:
                print("Ingrese un mes válido.")
        except ValueError:
            print("Ingrese un valor numérico válido.")
            

def numero_año(argumento):
    a = True
    while a:
        try:
            num = int(input(argumento))
            if num>=1990 and num<=2023:
                return str(num)
            else:
                print("Ingrese un año válido.")
        except ValueError:
            print("Ingrese un valor numérico válido.")