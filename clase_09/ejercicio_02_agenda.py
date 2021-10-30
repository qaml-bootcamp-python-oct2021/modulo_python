agenda={'contacto':[]}

def guardar_contacto(contacto):
    agenda.get('contacto').append(contacto)

def crear_contacto():
    print('--Ingrese datos de contacto a crear----')
    nombre=input('Nombre: ')
    telefono= input('Telefono: ')
    email = input('Email: ')
    return 

def visualizar_agenda():
    for contacto in agenda.get('contacto'):
         print(f'Contacto:::  {contacto}')

def buscar_contacto(nombre):
    indice = 0
    lista_contactos=agenda.get('contacto')
    while indice< len(lista_contactos):
        if lista_contactos[indice].get('nombre')== nombre:
           return {
               'indice': indice,
                'contacto':lista_contactos[indice]
                }
           
        indice+=1
    return None

def eliminar_contacto(nombre):
    contacto_eliminar= buscar_contacto(nombre)
    if contacto_eliminar is not None:
        agenda.get('contacto').pop(contacto_eliminar.get('indice'))
        print("Contacto eliminado")
    else:
        print("Contacto no existente")

def iniciar_busqueda():
    contacto_buscar =input('Ingrese el nombre del contacto a buscar:: ')
    resultado_busqueda= buscar_contacto(contacto_buscar)
    if resultado_busqueda == None:
        print('El contacto no existe')
    else:
        print(resultado_busqueda.get('contacto'))

def iniciar_eliminacion():
    contacto_eliminar =input('Ingrese el nombre del contacto a Eliminar:: ')
    eliminar_contacto(contacto_eliminar)

def pedir_opcion():
    return  int(input('''
    1- Crear contacto
    2- Visualizar agenda
    3- Buscar contacto
    4- Eliminar contacto
    0 - Salir
    '''))  


def iniciar_agenda():
    opcion_menu=pedir_opcion()
    while opcion_menu != 0:
        if opcion_menu == 1:
            guardar_contacto(crear_contacto())
        elif opcion_menu == 2:
            visualizar_agenda()
        elif opcion_menu == 3:
           iniciar_busqueda()
        elif opcion_menu == 4: 
            iniciar_eliminacion()
        else:
            print('opcion inexistente')
        opcion_menu=pedir_opcion()

    
iniciar_agenda()

     



