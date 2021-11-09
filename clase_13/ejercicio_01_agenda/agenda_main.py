import json
import archivo_util
import util
from alumno import Alumno
from estado_enum import Estado

lista_alumnos=[]

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
        opcion_estado = int(input(get_estado_opcion()))
        if validar_estado_opcion(opcion_estado)!= None:
            alumno.set_estado(Estado(opcion_estado).name)
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
    
def mostrar_alumnos(lista_alumnos_buscar):
    for alumno in lista_alumnos_buscar:
        alumno:Alumno
        print('::: Alumno :::')
        print(alumno.get_info())
    if(len(lista_alumnos_buscar)==0):
        print('::: No hay registros :::')

def mostrar_alumnos_estado():
    opcion_estado = int(input(get_estado_opcion()))
    if validar_estado_opcion(opcion_estado)!= None:
        lista_alumnos_estado=[]
        for alumno in lista_alumnos:
            if alumno.get_estado() == Estado(opcion_estado).name:
                lista_alumnos_estado.append(alumno)
        mostrar_alumnos(lista_alumnos_estado)   
    
def get_estado_opcion():
    opcion_estado='Ingrese::::\n'
    for estado in Estado:
        opcion_estado+= f'{estado.value} - Para {estado.name} \n'
    return opcion_estado

def validar_estado_opcion(opcion_estado):
        try:
            return Estado(opcion_estado)
        except ValueError:
            print('Opción invalida, intente de nuevo.') 
            return None

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
        print('-----Creando nuevo alumno-----')
        crear_alumno()
    if opcion == 2:
        print('-----Buscar por Nombre-----')
        alumno_buscar = buscar_alumno()
        if alumno_buscar != None:
            print(alumno_buscar.get_info())
        else:
            print('Alumno no localizado')
    if opcion == 3:
        print('-----Editar Estado-----')
        alumno_editar = buscar_alumno()
        if alumno_editar != None:
            editar_estado_alumno(alumno_editar)
        else:
            print('Alumno no localizado')
    if opcion == 4:
        print('-----Mostrando todos los alumnos-----')
        mostrar_alumnos(lista_alumnos)
    if opcion == 5:
        print('-----Mostrando alumnos por Estado-----')
        mostrar_alumnos_estado()
    else:
        print('-----Opción invalida-----')
    opcion = menu_opcion()