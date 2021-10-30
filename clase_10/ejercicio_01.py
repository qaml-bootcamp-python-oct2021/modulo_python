def crear_contacto():
    print('--Ingrese datos de contacto a agregar----')
    nombre=input('Nombre: ')
    apellido= input('Apellido: ')
    numero = input('Número: ')
    return {
        'nombre':nombre,
        'apellido':apellido,
        'numero':numero
    }

def agregar_contacto():
    contacto=crear_contacto()
    archivo= open('./clase_10/agenda.txt','a')
    archivo.write(f'{contacto.get("nombre") },{contacto.get("apellido") },{contacto.get("numero") } \n')
    archivo.close()

agregar_contacto()