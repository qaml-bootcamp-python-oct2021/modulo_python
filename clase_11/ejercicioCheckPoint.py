import json
data = None




def nuevo_curso():
    nombre = input("Nombre de curso: ")
    cantidad_alumnos = input("¿Cuántos alumnos hay?: ")
    estado = input("Estado del curso: ")
    cantidad_clases = input("¿Cuántas clases tiene?: ")

    return {
        'nombre':nombre,
        'cantidad_alumnos':cantidad_alumnos,
        'estado':estado,
        'cantidad_clases':cantidad_clases
    }

def buscar_curso():
    for curso in agenda['contacto']:
        print('---- contacto ----')
        for key,value in contacto.items():
            print(f'{key}:{value}')


def guardar_curso():
    with open('./clase_11/QA_minds_cursos.json','w') as json_file:
        data['cursos'].append(nuevo_curso())
        json.dump(data,json_file)
        #data = json.load(json_file)
        json_file.close()

def load_data():
    with open('./clase_11/QA_minds_cursos.json','r') as json_file:
        data = json.load(json_file)

def run_program():
    accion = ''

    while accion != '0':  
        if accion == '1': #Agregar curso
            guardar_curso()
        elif accion == '2': #Buscar curso
            guardar_curso()
        accion = input('''Elige la acción deseada
        1. Crear curso
        0. Salir
        ''')

run_program()