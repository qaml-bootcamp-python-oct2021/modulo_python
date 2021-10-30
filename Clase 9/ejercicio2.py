
my_agenda = {
    'agenda' : []
}

def agregar (nombre,numero,email):
    contacto = {
    'Nombre' : nombre,
    'Numero' : numero,
    'Email' : email
}
    return contacto

def guardar (contacto):
    my_agenda['agenda'].append(contacto)

def consultar(nombre):
    for contacto in my_agenda['agenda']:
        index = 0
        while index < len('agenda'):
            if contacto['Nombre'] == nombre:
                return contacto
            index +=1
        return None

#def imprimir(contacto):
#    print(my_agenda.values('Nombre'))

def opciones ():
    opcion = int(input(''' 
        1. Agregar contacto
        2. Borrar contacto
        3. Consultar
        0. Salir
        Dame una opcion: '''))
    return opcion

while opciones() != 0:
    opciones()
    print('esta es la opcion:')
    print(opciones())
    if opciones() == 1:
        print('hola')
#    elif opciones ==2:
#        print('como')
#    elif opciones ==3:
#        print('estas')
    else:
        print('Opcion incorrecta selecciona opcion')

    opciones()
    
    





#def agregar (nombre,numero,email):
#    nuevo_contacto = {
#    'Nombre' : nombre,
#    'Numero' : numero,
#    'Email' : email
#}
#    my_agenda['agenda'].append(nuevo_contacto)

#def borrar (nombre):
#    my_agenda['agenda'].pop()

#def consultar (nombre):
#    print(my_dicc.values(nombre))

