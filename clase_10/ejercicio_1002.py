#archivos - añadir registros en agenda JSON
import os
import json

agenda = {
    "Contactos" : []
}

def generar_path():
    separador = os.path.sep
    path_archivo = f'.{separador}clase_10{separador}mi_agenda_json.json'

    return path_archivo

def agregar_contacto_en_archivo(dict_agenda):
    
    path_archivo = generar_path()

    with open(path_archivo,'w') as mi_json:
        json.dump(dict_agenda,mi_json)


def generar_contacto(dict_agenda):
    nombre = input('Digite su nombre: ')
    apellido = input("Digite su apellido: ")
    email = input("Digite su e-mail: ")
    telefono = input('Digite su número telefónico: ')
    
    contacto = {
        'Nombre': nombre,
        'Apellido': apellido,
        'Email': email,
        'Telefono': telefono
    }

    dict_agenda['Contactos'].append(contacto)

    return dict_agenda
    

def imprimir_agenda():
    path_archivo = generar_path()

    with open(path_archivo,'r') as mi_json:
        print(json.load(mi_json))

def opciones():
    opcion = input("""Seleccione una opción:
            * 1. Crear Contacto
            * 2. Ver Agenda
            * 3. Salir
            --> """)
    return opcion


def inicio(dict_agenda):

    seleccion = "0"
    while seleccion != "3":
        seleccion = opciones()
 
 
        if (seleccion == str(1)):
            agenda = generar_contacto(dict_agenda)
            agregar_contacto_en_archivo(dict_agenda)
            seleccion = "0"
        elif (seleccion == str(2)):
            imprimir_agenda()
            seleccion = "0"
        elif (seleccion == str(3)):
            print("Gracias por usar la agenda. ¡Hasta luego!")
        else:
            print("Opcion incorrecta, seleccione una opción válida...")
            seleccion = "0"

inicio(agenda)