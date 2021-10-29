agenda = {
    'contactos' : [
        {
        'nombre' : 'nombre 1',
        'numero_telf' : 123,
        'email' : 'email@1'
        },
        {
        'nombre' : 'nombre 2',
        'numero_telf' : 456,
        'email' : 'email@2'
        },
        {
        'nombre' : 'nombre 3',
        'numero_telf' : 789,
        'email' : 'email@3'
        },
    ]
}

contacto = {}

def crear_contacto():
    nombre = str(input('ingrese el nombre del contacto:\n'))
    num_telf = int(input('ingrese el telefono del contacto:\n'))
    email = str(input('ingrese el email del contacto:\n'))

    return {
        'nombre' : nombre,
        'numero_telf' : num_telf,
        'email' : email
    }

def agregar_contacto(contacto):
    agenda['contactos'].append(contacto)

def visualizar_agenda(agenda):
    for contacto in agenda['contactos']:
        print(contacto)

def get_nombre_contacto():
    return input('ingrese nombre del contacto\n')

def buscar_contacto(nombre):
    index = 0
    while index < len(agenda['contactos']):
        contactos = agenda['contactos']
        contacto = contactos[index]
        if contacto['nombre'] == nombre:
            return contacto
        index += 1
    return None

def mostrar_contacto(contacto):
    for key, value in contacto.items():
        print(f'{key} - {value}')

def eliminar_contacto(nombre):
    index = 0
    while index < len(agenda['contactos']):
        contactos = agenda['contactos']
        contacto = contactos[index]
        if contacto['nombre'] == nombre:
            contactos.pop(index)
            print(f'el contacto {contacto} fue eliminado')
            return
        index += 1
    print(f'el contacto con el nombre {nombre} no existe')

opcion = int(input('''
1 - Para crear contacto
2 - Para visualizar Agenda
3 - Para buscar contacto
4 - Para eliminar contacto
0 - Para salir
'''))

while opcion != 0:
    if opcion == 1:
        #crear contacto
        contacto = crear_contacto()
        agregar_contacto(contacto)
    elif opcion == 2:
        #vizualizar agenda
        visualizar_agenda(agenda)
    elif opcion == 3:
        #buscar contacto
        nombre = get_nombre_contacto()
        contacto = buscar_contacto(nombre)
        if contacto is not None:
            mostrar_contacto(contacto)
        else:
            print('contacto ingresado no existe')
    elif opcion == 4:
        #eliminar contacto
        nombre = get_nombre_contacto()
        eliminar_contacto(nombre)
    else:
        print('valor erroneo')
    
    opcion = int(input('''
1 - Para crear contacto
2 - Para visualizar Agenda
3 - Para buscar contacto
4 - Para eliminar contacto
0 - Para salir
'''))