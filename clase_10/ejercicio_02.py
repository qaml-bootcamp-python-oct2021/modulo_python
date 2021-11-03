import json

contactos = None

def crear_contacto():
    nombre = input('Ingrese el nombre:\n')
    apellido = input('Ingrese el apellido:\n')
    email = input('Ingrese el email:\n')
    numero = input('Ingrese el numero:\n')

    contacto = {
        'nombre' : nombre,
        'apellido' : apellido,
        'email' : email,
        'numero' : numero
    }

    return contacto

def agregar_contacto(contacto):
    with open('./clase_10/agenda.json', 'r') as agenda:
        contactos = json.load(agenda)
    
    contactos['contactos'].append(contacto)

    with open('./clase_10/agenda.json', 'w') as agenda:
        json.dump(contactos,agenda)

contacto = crear_contacto()
agregar_contacto(contacto)