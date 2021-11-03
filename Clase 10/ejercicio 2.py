import json

data = {'contactos':[]}
datos = None

def agregar ():
    nombre = input('Dame el Nombre:\n')
    apellido = input('Dame el Apellido:\n')
    email = input('Dame el Email:\n')
    numero = input('Dame el Numero:\n')
    contacto = {
        'Nombre' : nombre,
        'Apellido' : apellido,
        'Email' : email,
        'Numero' : numero
    }
    return contacto

contacto = agregar()

data['contactos'].append(contacto)

#with open ('mi_json.json','a') as file:
#    json.dump(data)