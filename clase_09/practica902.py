'''
agenda = {
    'contactos' : []
}

def ingresarContacto(nombre,telefono,email):
    nombre = input('Ingresa nombre del contacto: ')
    telefono = input('Ingresa numero telefonico del contacto: ')
    contacto = {
        'nombre' : nombre,
        'numeroTelefonico' : telefono,
        'email' : email
    }

def guardarContacto(contacto):
    agenda['contactos'].append(contacto)

def buscarContacto(nombre):
   if agenda.get('nombre') is not None:
        print(agenda.get('nombre'))

def borrarContacto(nombre):
    agenda.pop('nombre','Ese contacto no existe en la agenda')

#def verContacto():


menu = int(input('''
#    1. Crear contacto
#    2. Ver agenda
#    3. Buscar contacto
#    4. Borrar contacto
#    0. Salir    
'''))

while menu != 0:
    if menu == 1:
        ingresarContacto()
    if menu == 2:
        verContacto('nombre','telefono','email')
    if menu == 3:
        buscarContacto()
    if menu == 4:
        borrarContacto()
    else:
        print('Ingrese una opcion valida')
        print(menu)
    break
'''

###########PROGRAMA###########

agenda = {
    'contactos' : []
}

def crear_contacto():
    nombre = input('Ingrese nombre de contacto\n')
    telefono = input('Ingrese numero de telefono de contacto\n')
    email = input('Ingrese email de contacto\n')
    contacto = {
        'nombre' : nombre,
        'telefono' : telefono,
        'email' : email
    }
    return contacto

def guardar_contacto(contacto):
    agenda['contactos'].append(contacto)

def mostrar_agenda():
    for contacto in agenda['contactos']:
        mostrar_contacto(contacto)

def get_contacto_a_buscar():
    return input('Ingrese nombre de contacto a buscar\n')

def buscar_contacto(nombre):
    index = 0
    while index < len(agenda['contactos']):
        contactos = agenda['contactos'] 
        contacto = contactos[index]
        if contacto['nombre'] == nombre:
            return contacto
        index += 1
    return None

def mostrar_contacto(contacto : dict):
    for key, value in contacto.items():
        print(f'{key} - {value}')

def eliminar_contacto(nombre):
    index = 0
    result = False
    while index < len(agenda['contactos']) and not result:
        contactos = agenda['contactos'] 
        contacto = contactos[index]
        if contacto['nombre'] == nombre:
            contactos.pop(index)
            result = True
            print('Contacto eliminado')
        index += 1
    if not result:
        print('No existe un contacto con el nombre ingresado. Intente de nuevo')

opcion = int(input('''
1 - Para crear contacto
2 - Para visualizar Agenda
3 - Para buscar contacto
4 - Para eliminar contacto
0 - Para salir
'''))

while opcion != 0:
    if opcion == 1:
        contacto = crear_contacto()
        guardar_contacto(contacto)
    elif opcion == 2:
        mostrar_agenda()
    elif opcion == 3:
        nombre = get_contacto_a_buscar()
        contacto = buscar_contacto(nombre)
        if contacto is not None:
            mostrar_contacto(contacto)
        else:
            print('El contacto ingresado no existe. Intente de nuevo')
    elif opcion == 4:
        nombre = get_contacto_a_buscar()
        eliminar_contacto(nombre)
    else:
        print('opcion errada, intente de nuevo')

    opcion = int(input('''
1 - Para crear contacto
2 - Para visualizar Agenda
3 - Para buscar contacto
4 - Para eliminar contacto
0 - Para salir
'''))