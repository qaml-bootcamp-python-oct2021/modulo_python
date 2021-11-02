#archivos - añadir registros en agenda
import os

def abrir_archivo():
    separador = os.path.sep
    path_archivo = f'.{separador}clase_10{separador}mi_agenda.txt'
    mi_archivo = open(path_archivo,'a')
    return mi_archivo

def cerrar_archivo(mi_archivo):
    mi_archivo.close()

def agregar_contacto_en_archivo(mi_archivo, contacto):
    mi_archivo.write(contacto)
    return mi_archivo

def crear_contacto(mi_archivo):
    nombre = input('Digite su nombre: ')
    apellido = input("Digite su apellido: ")
    telefono = input('Digite su número telefónico: ')
    
    contacto = f'{nombre},{apellido},{telefono}\n'

    mi_archivo = agregar_contacto_en_archivo(mi_archivo, contacto)

    return mi_archivo
    

def imprimir_agenda(mi_archivo):
    print(mi_archivo.read())

def opciones():
    opcion = input("""Seleccione una opción:
            * 1. Crear Contacto
            * 2. Ver Agenda
            * 3. Salir
            --> """)
    return opcion


def inicio():
    agenda_txt = abrir_archivo()

    seleccion = "0"
    while seleccion != "3":
        seleccion = opciones()
 
        if (seleccion == str(1)):
            agenda_txt = crear_contacto(agenda_txt)
            seleccion = "0"
        elif (seleccion == str(2)):
            imprimir_agenda(agenda_txt)
            seleccion = "0"
        elif (seleccion == str(3)):
            print("Gracias por usar la agenda. ¡Hasta luego!")
            cerrar_archivo(agenda_txt)
        else:
            print("Opcion incorrecta, seleccione una opción válida...")
            seleccion = "0"

inicio()