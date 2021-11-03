import json



sistema_qaminds  = {
    'cursos': []
}

def dar_alta_curso():
    nombre_curso = input("Ingresar el nombre del curso: ")
    cantidad_alumnos = input("Ingresar la cantidad de alumnos: ")
    estado = input("Ingresar el estado: ")
    cantidad_clases = input("Ingresar la cantidad de clases: ")
    return {
        'nombre': nombre_curso,
        'cantidad_alumnos': cantidad_alumnos,
        'estado': estado,
        'cantidad_clases': cantidad_clases
    }

def leer_file_json():
    
    with open('cursos.json') as file:
         sistema_qaminds = json.load(file)
    return sistema_qaminds

def mostrar_cursos():
    index = 1
    sistema_qaminds = leer_file_json()
    print(f''' El sistema cuenta con los cursos: ''')
    for curso in sistema_qaminds['cursos']:
        print(f'--------------Curso {index} --------------')
        print(f''' 
               Nombre Curso: {curso['nombre']}
               Cantidad Alumnos: {curso['cantidad_alumnos']}
               Estado: {curso['estado']}
               Cantidad Clases: {curso['cantidad_clases']} 
        ''') 
        index+=1

def guardar_curso_en_archivo():

    sistema_qaminds = leer_file_json()
    curso = dar_alta_curso()
    sistema_qaminds['cursos'].append(curso)
    print("----La informacion se ha guardado--------")
    print(f''' El sistema ahora cuenta con el curso:  
               Nombre Curso: {curso['nombre']}
               Cantidad Alumnos: {curso['cantidad_alumnos']}
               Estado: {curso['estado']}
               Cantidad Clases: {curso['cantidad_clases']} ''')
    escribir_archivo(sistema_qaminds)


def buscar_curso():
    index = 0
    flag = False
    sistema_qaminds = leer_file_json()
    nombre_curso = input('Introduzca el curso: ')
    while index < len(sistema_qaminds['cursos']):
        if nombre_curso == sistema_qaminds['cursos'][index]['nombre']:
            flag = True
            break
        index +=1
    if flag:
        print(f'Curso encontrado:  {nombre_curso}')
        modificar_estado_curso(sistema_qaminds, index)
    else:  print(f'''El Curso: "{nombre_curso}" no esta en el sistema ''')

def modificar_estado_curso(objeto,index):
    opcion_usuario = int(input("Desea cambiar el estado de este curso? 1 = Y, 2 = N "))
    if opcion_usuario == 1:
       estado_curso = input('Introduzca el nuevo estado: ')
       objeto['cursos'][index]['estado'] = estado_curso
       escribir_archivo(objeto)
       print(f"El estado del curso: {objeto['cursos'][index]['nombre']} se ha modificado de {objeto['cursos'][index]['estado']} a {estado_curso}")
    else: print("No modificado")


def escribir_archivo(objeto):
    with open('cursos.json', 'w+') as file:
        json.dump(objeto,file, indent=4)

def construir_menu():
    opcion = int(input('''
      1 - Para Crear Curso
      2 - Buscar Curso y Modificar Estado
      3 - Mostrar todos los cursos
      0 - Para Salir
    '''))
    return opcion

def salida():
    print('Numero no permitido.....')

def solicitar_usuario_menu():
    switch_menu = {
        1: guardar_curso_en_archivo,
        2: buscar_curso,
        3: mostrar_cursos,
    }
    opcion = construir_menu()

    while opcion != 0:
       switch_menu.get(opcion, salida)()
       opcion = construir_menu()
    print('Adios.....')
solicitar_usuario_menu()

