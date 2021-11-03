
mis_cursos = {
    'mis_cursos' : []
}

def opciones ():
    opcion = int(input(''' 
        1. Alta de Curso
        2. Modificar Curso
        3. Consultar
        0. Salir
        Dame una opcion: '''))
    return opcion

def agregar ():
    nombre_curso = input('Dame el Nombre del Curso:\n')
    cantidad_alumnos = input('Dame el Numero total de alumnos:\n')
    estado = input('Dame el Estado (Activo, Inactivo):\n')
    cantidad_clases = input('Dame el Numero de clases:\n')
    curso = {
        'Curso' : nombre_curso,
        'Alumnos' : cantidad_alumnos,
        'Estado' : estado,
        'Clases' : cantidad_clases
    }
    return curso

def alta (curso):
    file = open('cursos_qaminds.txt','a')
    file.write(f"{curso}\n")
    file.close

def buscar ():
    nom_curso = input('Dame el nombre del curso:\n')
    return nom_curso

def consultar(opcion, nom_curso):
        index = 0
        file = open('cursos_qaminds.txt','r')
        archivo = file.readlines()
        
        #for list in archivo:
            cursos_list = list.split(',')
        while index < len(mis_cursos):
            cursos = mis_cursos['mis_cursos'] 
            curso = cursos[index]
            if curso['nom_curso'] == nom_curso:
                if opcion == 2:
                    return index
                elif opcion == 3:
                    return curso
            index +=1
        return None
        #mis_cursos.close

def imprimir(opcion, cusrso):
    if opcion == 1:
        print('Curso:\n')
        imprimir_valores(curso)
    elif opcion == 2 :
        print('Cursos:\n')
        for cusrso in mis_cursos['mis_cursos']:
            imprimir_valores(curso)

def imprimir_valores (curso):
    for key , value in curso.items():
        print(f'{key} - {value}')
    print('-----')

def consulta ():
    consulta = int(input(''' 
        1. Consultar Curso:
        2. Consultar Cursos:
        0. Regresar al menu anterior
        Dame una opcion: '''))
    return consulta

#def modificar (index):


operador = opciones()

while operador != 0:
    if operador == 1:
        #agregar curso
        curso = agregar()
        alta(curso)
    elif operador == 2:
        #modificar curso
        nom_curso = buscar()
        index = consultar(operador, nom_curso)
        if index is not None:
            #modificar
            print('modificar')
        else:
            print('Curso no existe')
    elif operador == 3:
        #consultas
        operador2 = consulta()
        while operador2 != 0:
            if operador2 == 1:
                #Consultar curso
                nom_curso = buscar()
                curso = consultar(operador, nom_curso)
                if curso is not None:
                    imprimir(operador2,curso)
                else:
                    print('Curso no existe, intente de nuevo')
            elif operador2 == 2:
                #Consultar Curso               
                imprimir(operador2, None)
            else:
               print('Opcion incorrecta selecciona opcion') 

            operador2 = consulta()

    else:
        print('Opcion incorrecta selecciona opcion')

    operador = opciones()