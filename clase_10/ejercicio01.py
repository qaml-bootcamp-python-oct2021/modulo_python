my_file = open('agendas.txt','a')

def crear_contacto():
    nombre = input("Nombre de contacto:")
    apellido = input("Apellido de contacto:")
    numero = input("Número de contacto:")
    return str(f'{nombre},{apellido},{numero}⁄n')  
    

def guardar_contacto():
    my_file.write(crear_contacto())
    print("--------Contacto guardado--------")

guardar_contacto()
