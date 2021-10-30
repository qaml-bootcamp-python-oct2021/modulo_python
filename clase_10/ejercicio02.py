import json
data = None

with open('./clase_10/my_file.json','r') as json_file:
    data = json.load(json_file)

nuevo_contacto = {
    'nombre':'pepito',
    'apellido':'muñoz',
    'telefono':'3987876',
    'email':'pepe@correo.com'
}

data['contactos'].append(nuevo_contacto)

with open('./clase_10/my_file.json','r') as json_file:  
    json.dump(nuevo_contacto,json_file)