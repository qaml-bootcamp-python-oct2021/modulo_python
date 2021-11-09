import json
import archivo_util
import util
from alumno import Alumno
from estado_enum import Estado

lista_alumnos=[]
def editar_estado_alumno(alumno: Alumno):
    pass

def crear_alumno():
    nombre = input('Ingrese un nombre de Alumno\n')
    apellido = input('Ingrese un apellido de Alumno\n')
    email = input('Ingrese un mail de Alumno\n')
    alumno_nuevo = Alumno(nombre,apellido,email)
    lista_alumnos.append(alumno_nuevo)
    guardar_alumnos()

def buscar_alumno():
    nombre_alumno = input('Ingrese el nombre de Alumno  \n')
    indice = 0
    while indice< len(lista_alumnos):
        if lista_alumnos[indice].get_nombre()== nombre_alumno:
           return  lista_alumnos[indice]
        indice+=1
    return None
    
def editar_estado_alumno(alumno : Alumno):
    print(f'El estado actual de {alumno.get_nombre()} es: {alumno.get_estado()}')
    opcion = input('Desea modificar el estado? Y/N\n')
    if opcion == 'Y':
        opcion_estado = int(input(f'''
        1 - Para {Estado.ACTIVO.name}
        2 - Para {Estado.MORA.name}
        3 - Para {Estado.RETIRADO.name}
        4 - Para {Estado.EGRESADO.name}
        5 - Para {Estado.CERTIFICADO.name}
        '''))
        guardar = True

        if opcion_estado == 1:
            alumno.set_estado(Estado.ACTIVO.value)
        elif opcion_estado == 2:
            alumno.set_estado(Estado.MORA.value)
        elif opcion_estado == 3:
            alumno.set_estado(Estado.RETIRADO.value)
        elif opcion_estado == 4:
            alumno.set_estado(Estado.EGRESADO.value)
        elif opcion_estado == 5:
            alumno.set_estado(Estado.CERTIFICADO.value)
        else:
            print('Opcion invalida, intente de nuevo.')
            guardar = False

        if guardar:
          guardar_alumnos()
           
def guardar_alumnos():
    agenda = {
        "alumnos" : []
    }
    for alumno in lista_alumnos:
        alumno:Alumno
        alumno_dicc=util.alumno_to_diccionario(alumno)
        agenda['alumnos'].append(alumno_dicc)
    archivo_util.guardar_agenda(agenda)
    
def mostrar_alumnos():
    for alumno in lista_alumnos:
        alumno:Alumno
        print('---- Alumno ----')
        print(alumno.get_info())

def mostrar_alumno_estado(estado):
    pass

def menu_opcion():
    return int(input('''
    1 - Crear un Alumno
    2 - Buscar un Alumno
    3 - Editar estado de Alumno
    4 - Mostrar Alumnos
    5 - Mostrar Alumnos por estado
    0 - Salir
    '''))

 
opcion = menu_opcion()
lista_alumnos_archivo = archivo_util.leer_agenda().get('alumnos')
if len(lista_alumnos_archivo)> 0:
    lista_alumnos= util.diccionario_to_alumno(lista_alumnos_archivo)
while opcion != 0 :

    if opcion == 1:
        crear_alumno()
    if opcion == 2:
        alumno_buscar = buscar_alumno()
        if alumno_buscar != None:
            print(alumno_buscar.get_info())
        else:
            print('Alumno no localizado')
       
    if opcion == 3:
        alumno_editar = buscar_alumno()
        if alumno_editar != None:
            editar_estado_alumno(alumno_editar)
        else:
            print('Alumno no localizado')
    if opcion == 4:
        mostrar_alumnos()
    if opcion == 5:
        pass
      

    opcion = menu_opcion()