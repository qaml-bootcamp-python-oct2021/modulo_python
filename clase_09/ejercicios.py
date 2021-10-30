# ''' Libreria '''

# libreria = {
#     'libros' : []
# }

# def crear_libro(titulo,autor,genero):
#     return {
#         'titulo' : titulo,
#         'autor' : autor,
#         'genero' : genero
#     }

# def guardar_libro(libro):
#     libreria['libros'].append(libro)

# def print_libros():
#     for libro in libreria['libros']:
#         print(libro)



# libro = crear_libro('Mujeres','Charles Bukowski','relato')
# guardar_libro(libro)
# libro = crear_libro('El Cartero','Charles Bukowski','relato')
# guardar_libro(libro)
# print_libros()


''' Agenda '''

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

