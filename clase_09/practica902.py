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
    1. Crear contacto
    2. Ver agenda
    3. Buscar contacto
    4. Borrar contacto
    0. Salir    
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
