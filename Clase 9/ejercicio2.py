
my_agenda = {
    'agenda' : []
}

def opciones ():
    opcion = int(input(''' 
        1. Agregar contacto
        2. Borrar contacto
        3. Consultar
        0. Salir
        Dame una opcion: '''))
    return opcion

def agregar ():
    nombre = str(input('Dame el nombre:\n'))
    numero = int(input('Dame el numero:\n'))
    email = str(input('Dame el email:\n'))
    contacto = {
        'Nombre' : nombre,
        'Numero' : numero,
        'Email' : email
    }
    return contacto

def guardar (contacto):
    my_agenda['agenda'].append(contacto)

def buscar ():
    nombre = input('Dame el nombre:\n')
    return nombre

def consultar(opcion, nombre):
        index = 0
        while index < len(my_agenda['agenda']):
            agenda = my_agenda['agenda'] 
            contacto = agenda[index]
            if contacto['Nombre'] == nombre:
                if opcion == 2:
                    return index
                elif opcion == 3:
                    return contacto
            index +=1
        return None

def imprimir(opcion, contacto):
    if opcion == 1:
        print('Contacto:\n')
        imprimir_valores(contacto)
    elif opcion == 2 :
        print('Agnda de contactos:\n')
        for contacto in my_agenda['agenda']:
            imprimir_valores(contacto)

def imprimir_valores (contacto):
    for key , value in contacto.items():
        print(f'{key} - {value}')
    print('-----')

def consulta ():
    consulta = int(input(''' 
        1. Consultar Contacto:
        2. Consultar Agenda:
        0. Regresar al menu anterior
        Dame una opcion: '''))
    return consulta

def borrar (index):
        agenda = my_agenda['agenda']
        agenda.pop(index)

operador = opciones()

while operador != 0:
    if operador == 1:
        #agregar contato
        contacto = agregar()
        guardar(contacto)
    elif operador == 2:
        #borrar contacto
        nombre = buscar()
        index = consultar(operador, nombre)
        borrar(index)
    elif operador == 3:
        #consultas
        operador2 = consulta()
        while operador2 != 0:
            if operador2 == 1:
                #Consultar contacto
                nombre = buscar()
                contacto = consultar(operador, nombre)
                if contacto is not None:
                    imprimir(operador2,contacto)
                else:
                    print('Contacto no existe, intente de nuevo')
            elif operador2 == 2:
                #Consultar Agenda               
                imprimir(operador2, None)
            else:
               print('Opcion incorrecta selecciona opcion') 

            operador2 = consulta()

    else:
        print('Opcion incorrecta selecciona opcion')

    operador = opciones()

