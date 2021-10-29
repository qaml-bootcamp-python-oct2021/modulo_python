agenda  = {
    'contactos': []
}

def solicitar_contacto():
    nombre_persona = input("Ingresar Nombre: ")
    numero_tel_persona = input("Ingresar Telefono: ")
    email_persona = input("Ingresar Email: ")
    return {
        'nombre': nombre_persona,
        'numero telefonico': numero_tel_persona,
        'email persona': email_persona
    }
def almacenar_contacto():
    contacto_a = solicitar_contacto()
    agenda['contactos'].append(contacto_a)
    print("Contacto Almacenado")
    print(f''' La agenda ahora cuenta con este contacto:  
               Nombre: {contacto_a['nombre']}
               Telefono: {contacto_a['numero telefonico']}
               Email: {contacto_a['email persona']} ''')


def visualizar_agenda():
    index = 1
    if len(agenda['contactos']) > 0:
        for value in agenda['contactos']:
            print(f'--------------Contacto {index} --------------')
            for key, item in value.items():
                print(f'{key} : {item}')
            index+=1
    else: print(f'Sin contactos en la agenda.....')

def buscar_contacto():
    index = 0
    flag = False
    nombre_usuario = input('Introduzca el nombre: ')
    objeto_encontrado = -1
    while index < len(agenda['contactos']):
        if nombre_usuario == agenda['contactos'][index]['nombre']:
            flag = True
            objeto_encontrado = index
            break
        index +=1
    return {
        'flag': flag,
        'index borrar': objeto_encontrado,
        'nombre usuario': nombre_usuario
    }

def nombre_fue_encontrado():
    respuesta_buscar_contacto = buscar_contacto()
    flag = respuesta_buscar_contacto['flag']
    nombre_usuario = respuesta_buscar_contacto['nombre usuario']
    if flag:
        print(f'Nombre encontrado:  {nombre_usuario}')
    else:  print(f'''El Nombre "{nombre_usuario}" no esta en la agenda ''')

def eliminar_contacto():
    respuesta_buscar_contacto = buscar_contacto()
    flag = respuesta_buscar_contacto['flag']
    objeto = respuesta_buscar_contacto['index borrar']
    nombre_usuario = respuesta_buscar_contacto['nombre usuario']
   
    if flag:
        print(f'El Nombre que fue borrado es: {nombre_usuario}')
        agenda['contactos'].pop(objeto) # 'Error en borrar'
    else:  print(f'''El Nombre "{nombre_usuario}" no esta en la agenda ''')
# visualizar_agenda()

def construir_menu():
    opcion = int(input('''
      1 - Para Crear Contacto
      2 - Para visualizar Agenda
      3 - Para buscar contacto
      4 - Para eliminar contacto
      0 - Para Salir
    '''))
    return opcion
def salida():
    print('Numero no permitido.....')

def solicitar_usuario_menu():
    switch_menu = {
        1: almacenar_contacto,
        2: visualizar_agenda,
        3: nombre_fue_encontrado,
        4: eliminar_contacto
    }
    opcion = construir_menu()

    while opcion != 0:
       switch_menu.get(opcion, salida)()
       opcion = construir_menu()
    print('Adios.....')
solicitar_usuario_menu()
# almacenar_contacto()