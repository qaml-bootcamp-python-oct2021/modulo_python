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
    curso_a_buscar = input("Nombre de curso: ")
    nuevo_estado = input("Nuevo estado: ")

    data = load_data()
    for curso in data['cursos']:
        for key,value in curso.items():
            if key == "nombre" and value == curso_a_buscar:
                curso['estado'] = nuevo_estado
                break
    save_file(data)

def mostrar_cursos():
    data = load_data()
     
    for curso in data['cursos']:
        print(curso)
    
        

def save_file(data):
    with open('./clase_11/QA_minds_cursos.json','w') as json_file:
        json.dump(data,json_file)
        json_file.close()


def guardar_curso():
    data = load_data()
    data['cursos'].append(nuevo_curso())
    save_file(data)
        #data = json.load(json_file)
        

def load_data():
    with open('./clase_11/QA_minds_cursos.json','r') as json_file:
        data = json.load(json_file)
        return data

def run_program():
    accion = ''

    while accion != '0':  
        if accion == '1': #Agregar curso
            guardar_curso()
        elif accion == '2': #Buscar curso
            buscar_curso()
        elif accion == '3': #Buscar curso
            mostrar_cursos()
        accion = input('''Elige la acción deseada
        1. Crear curso
        2. Cambiar status de curso
        3. Mostrar todos los cursos
        0. Salir
        ''')

run_program()