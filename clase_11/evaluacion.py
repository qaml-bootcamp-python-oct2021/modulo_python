import json


estado_activo="Activo"
estado_inactivo="No iniciado"
ruta_archivo="./clase_11/archivo_cursos.json"

def crear_curso():
    nombre=input('Nombre: ')
    cant_alumnos= input('Cantidad de alumnos: ')
    estado = input('Estado(Activo/No iniciado): ')
    cant_clases = input('Cantidad de clases: ')
    return {
        "nombre":nombre,
        "cantidad_alumnos":cant_alumnos,
        "estado":estado,
        "cantidad_clases":cant_clases
    }

def buscar_curso(lista_cursos, nombre_curso):
    indice = 0
    while indice< len(lista_cursos):
        if lista_cursos[indice].get('nombre')== nombre_curso:
           return  lista_cursos[indice]
        indice+=1
    return None

def iniciar_busqueda_curso(lista_cursos):
    curso_buscar =input('Ingrese el nombre del curso a buscar:: ')
    resultado_busqueda= buscar_curso(lista_cursos,curso_buscar)
    if resultado_busqueda == None:
        print('El curso no existe')
    else:
        print(resultado_busqueda)

def modificar_estado_curso(lista_curso,curso):
    print(f'Curso en estatus: {curso["estado"]}')
    if curso["estado"] == estado_activo:
        curso["estado"] = estado_inactivo
    else:
       curso["estado"] = estado_activo
    print(f'Curso actualizado a  estatus: {curso["estado"]}')
    guardar_en_archivo(lista_curso)

def inciar_modificacion_curso(lista_cursos):
    curso_buscar =input('Ingrese el nombre del curso a modificar:: ')
    resultado_busqueda= buscar_curso(lista_cursos,curso_buscar)
    if resultado_busqueda == None:
        print('El curso no existe')
    else:
        modificar_estado_curso(lista_cursos,resultado_busqueda)

def mostrar_cursos(lista_cursos):
    for curso in lista_cursos:
        print("::::::Mostrando curso::::::")
        for key, value in curso.items():#Obtener items completos de un diccionario
            print(f' {key} = {value}')

def guardar_curso(lista_curso,curso):
    lista_curso.append(curso)
    guardar_en_archivo(lista_curso)
     
def leer_archivo():
    try:
        with open(ruta_archivo,'r') as archivo:
            return json.load(archivo)
          
    except FileNotFoundError as error:
        print("Se crea archivo")
        file=open(ruta_archivo,'w')
        file.close
        return {'cursos':[]}
  
 
def guardar_en_archivo(lista_cursos):
    with open(ruta_archivo,'w') as archivo:
        qa_minds={"cursos":lista_cursos}
        json.dump(qa_minds,archivo)  

def pedir_opcion():
    return  int(input('''
    1- Alta curso
    2- Buscar curso
    3- Modificar estado de  curso
    4- Mostrar cursos
    0 - Salir
    '''))  

def iniciar_sistema():
    lista_cursos=leer_archivo().get('cursos')
    opcion_menu=pedir_opcion()
    while opcion_menu != 0:
        if opcion_menu == 1:
            guardar_curso(lista_cursos,crear_curso())
        elif opcion_menu == 2:
           iniciar_busqueda_curso(lista_cursos)
        elif opcion_menu == 3:
           inciar_modificacion_curso(lista_cursos)
        elif opcion_menu == 4: 
            mostrar_cursos(lista_cursos)
        else:
            print('Opcion No existente')
        opcion_menu=pedir_opcion()

iniciar_sistema()

