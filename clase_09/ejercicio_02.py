agenda = {
    'contacto': []
}

def crear_contacto():
    nombre = input("Nombre de contacto:")
    numero = input("Número telefónico de contacto:")
    email = input("Email de contacto:")
    return{
        'nombre':nombre,
        'numero':numero,
        'email':email
    }

def guardar_contacto():
    agenda['contacto'].append(crear_contacto())
    print("--------Contacto guardado--------")
   




def ver_agenda():
    if len(agenda['contacto']) == 0:
        print("No hay contactos")

    for contacto in agenda['contacto']:
        print('---- contacto ----')
        for key,value in contacto.items():
            print(f'{key}:{value}')

def buscar_nombre():
    nombre = input("¿Qué contacto desea buscar?")
    index=0
    while index < len(agenda['contacto']):
        for contacto in agenda['contacto']:
            if contacto['nombre'] == nombre:
                return contacto
            else :
                return None
        index += 1

def buscar_contacto():
    result = buscar_nombre()
    if result is not None:
        print(result)
    else:
        print("no hay resultados")

def borrar_contacto():
    result = buscar_nombre()
    if result is not None:
        agenda['contacto'].pop(result)
    else:
        print("no hay resultados")


accion = ''

while accion != '0':  
    if accion == '1': #Agregar contacto
        guardar_contacto()
    elif accion == '2': #Ver Agenda
        ver_agenda()
    elif accion == '3':
        buscar_contacto()
    elif accion == '4':
        borrar_contacto()
    accion = input('''Elige la acción deseada
    1. Crear contacto
    2. Ver agenda
    3. Buscar contacto
    4. Borrar contacto
    0. Salir
    ''')