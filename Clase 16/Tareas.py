def menu():
    return int(input('''
    1 - Crear Tareas
    2 - Alta de Usuario
    3 - Consutar Tareas
    4 - Modificar Estado de tareas
    0 - Para salir
    '''))

opcion = menu()

while opcion != 0 :

    if opcion == 1:
        crear_alumno()
    if opcion == 2:
        alumno = buscar_alumno()
        if alumno is not None:
            imprimir_datos_alumno(alumno)
    if opcion == 3:
        alumno = buscar_alumno()
        editar_estado_alumno(alumno)
    if opcion == 4:
        mostrar_alumnos()

    opcion = menu()