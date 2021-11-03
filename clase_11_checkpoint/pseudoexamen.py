#Sistema QA Minds de administración de cursos

#archivos - añadir registros en agenda JSON
import os
import json

catalogo = {
    "Cursos" : []
}

def generar_path():
    separador = os.path.sep
    path_archivo = f'.{separador}clase_11_checkpoint{separador}mi_catalogo_cursos.json'

    return path_archivo

def agregar_catalogo_en_archivo(dict_catalogo):
    
    path_archivo = generar_path()

    with open(path_archivo,'w') as mi_json:
        json.dump(dict_catalogo,mi_json)


def obtener_catalogo_de_archivo():

    path_archivo = generar_path()

    with open(path_archivo,'r') as mi_json:
        nvo_catalogo = json.load(mi_json)

    return nvo_catalogo

def checar_archivo(path_archivo):
    
    if os.path.exists(path_archivo):
        return True
    else:
        return False


def generar_curso(dict_catalogo):
    nombre = input('Digite nombre del curso: ')
    alumnos = input("Digite número de alumnos: ")
    clases = input('Digite número de clases: ')
    
    curso = {
        'Nombre': nombre,
        'Estado': "No Iniciado",
        'Alumnos': alumnos,
        'Clases': clases
    }

    dict_catalogo['Cursos'].append(curso)

    return dict_catalogo
    

def imprimir_catalogo(dict_catalogo):
    print(f"*******Total de cursos: {len(dict_catalogo['Cursos']) }*****")
    for curso in dict_catalogo['Cursos']:
        print('------------')
        for key, value in curso.items():
            print(f"{key}: {value}.")
    print('*********************************************')

def imprimir_curso(mi_curso):
    print("********Curso********")
    for key, value in mi_curso.items():
        print(f"{key}: {value}.\n")


def buscar_curso(dict_catalogo, nombre_curso, opcion):

    size = len(dict_catalogo['Cursos'])
    no_elemento = 0 
    found = False

    for curso in dict_catalogo['Cursos']:
        if(curso.get('Nombre') != nombre_curso):
            no_elemento += 1
        else:
            found = True
            if (opcion == "2"):
                curso['Estado'] = 'Activo'
            elif (opcion == "3"):
                curso['Estado'] = 'Terminado'
            else:
                imprimir_curso(curso)

    if(not found):
        print("El curso no se encuentra registrado...")

    return dict_catalogo

def opciones():
    opcion = input("""Bienvenido al Catálogo de cursos QA Minds - Seleccione una opción:
            * 1. Alta de Curso
            * 2. Iniciar Curso
            * 3. Terminar Curso
            * 4. Ver Todos los Cursos
            * 5. Buscar Curso
            * 6. Salir
            --> """)
    return opcion


def inicio(dict_catalogo):

    seleccion = "0"
    vacio = True

    if (checar_archivo(generar_path())):
        vacio = False
        dict_catalogo = obtener_catalogo_de_archivo()
    else:
        vacio = True

    while seleccion != "6":
        seleccion = opciones()
 
 
        if (seleccion == "1"):
            dict_catalogo = generar_curso(dict_catalogo)
            agregar_catalogo_en_archivo(dict_catalogo)
            seleccion = "0"
            vacio = False
        elif (seleccion == "2" or seleccion == "3" or seleccion == "5"):
            if (vacio):
                print("Catálogo vacio.. Por favor agregue un curso antes de proceder.")
            else:
                nombre_curso = input("Digite nombre de curso a buscar: ")
                dict_catalogo = buscar_curso(dict_catalogo,nombre_curso,seleccion)
            
            seleccion = "0"
        elif (seleccion == "4"):
            if (vacio):
                print("Catálogo vacio.. Por favor agregue un curso antes de proceder.")
            else:
                imprimir_catalogo(dict_catalogo)

            seleccion = "0"
        elif (seleccion == "6"):
            print("************¡Hasta luego!************")

            if (not vacio):
                agregar_catalogo_en_archivo(dict_catalogo)
        else:
            print("Opcion incorrecta, seleccione una opción válida...")
            seleccion = "0"

inicio(catalogo)