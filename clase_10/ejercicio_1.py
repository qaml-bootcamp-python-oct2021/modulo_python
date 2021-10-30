def introducir_contacto():
    nombre  = input("Introducir nombre")
    apellido  = input("Introducir apellido")
    numero  = input("Introducir numero")
    guardar_contacto(nombre, apellido, numero)

def guardar_contacto(nombre_a, apellido_a, numero_a):
    archivo = open('agenda.txt')
    
