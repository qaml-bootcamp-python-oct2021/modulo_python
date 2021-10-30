
import _json
def introducir_contacto():
    nombre  = input("Introducir nombre")
    apellido  = input("Introducir apellido")
    numero  = input("Introducir numero")
    email  = input("Introducir email")
    guardar_contacto(nombre, apellido, numero, email)

def guardar_contacto(nombre_a, apellido_a, numero_a, email_a):
    obj_contacto = {
        'nombre': nombre_a,
        'apellido': apellido_a,
        'numero telefonico': numero_a,
        'email': email_a
    }
    archivo = open('\clase_10\agenda.json')
    objeto  = deserializar_json(archivo)
    objeto.append(obj_contacto)
    with archivo as line:
      open('\clase_10\agenda.json', 'w')

def deserializar_json(objeto):
    
