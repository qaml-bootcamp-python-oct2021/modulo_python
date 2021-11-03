import json


data = None
#contactos= {'contacto':[]}

def crear_contacto():
    nombre = input('Ingrese nombre de contacto\n')
    apellido = input('Ingrese apellido de contacto\n')
    telefono = input('Ingrese numero de contacto\n')
    email = input('Ingrese email de contacto\n')
    contacto = {
        'nombre' : nombre,
        'apellido' : apellido,
        'telefono' : telefono,
        'email' : email
    }
    return contacto


with open('./clase_10/agenda.json','r') as agenda:
    data = json.load(agenda)

data['contactos'].append(crear_contacto())
with open('./clase_10/agenda.json','w') as agenda:
    json.dump(data,agenda)

with open('./clase_10/agenda.json','r') as agenda:
     print(json.load(agenda))