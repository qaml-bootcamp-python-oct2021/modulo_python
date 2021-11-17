#Construye un script que permita a un usuario almacenar un contacto en una agenda, visualizar la agenda completa, buscar contactos por su nombre, eliminar un contacto o salirse de la agenda.
#Los datos que componen la agenda son:nombre, número telefónico y email.
#Para realizar este script será necesario utilizar el comando input para ingresar los datos por la consola.

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
    return input('Ingrese nombre del contacto a buscar\n')

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
            print('Contacto eliminado exitosamente')
        index += 1
    if not result:
        print('No existe un contacto con el nombre ingresado, intente nuevamente')

opcion = int(input('''
1 - Crear contacto
2 - Visualizar Agenda
3 - Buscar contacto
4 - Eliminar contacto
0 - Salir de la agenda
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
            print('El contacto ingresado no existe, intente nuevamente')
    elif opcion == 4:
        nombre = get_contacto_a_buscar()
        eliminar_contacto(nombre)
    else:
        print('Opción invalida, intente nuevamente')

    opcion = int(input('''
1 - Crear contacto
2 - Visualizar Agenda
3 - Buscar contacto
4 - Eliminar contacto
0 - Salir de la agenda
'''))