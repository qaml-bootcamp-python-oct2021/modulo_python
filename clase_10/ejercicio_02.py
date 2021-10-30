import json

contactos={'contactos':[]}
def crear_contacto():
    print('--Ingrese datos de contacto a agregar----')
    nombre=input('Nombre: ')
    apellido= input('Apellido: ')
    email= input('Email: ')
    numero = input('Número: ')
    return {
        'nombre':nombre,
        'apellido':apellido,
        'email':email,
        'numero':numero
    }

def agregar_contacto(contacto):
    contactos['contactos'].append(contacto)
    with open('./clase_10/agenda_json.json','w') as archivo:
        json.dump(contactos,archivo)
    

agregar_contacto(crear_contacto())