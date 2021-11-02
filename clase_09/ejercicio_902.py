#dictionarios - crear agenda

mi_agenda = {
    'Contactos': []
}

#value = input('ingrese un numero: ')

def crear_contacto(agenda):
    nombre = input('Digite su nombre: ')
    telefono = input('Digite su número telefónico: ')
    email = input("Digite su e-mail: ")

    contacto = {
        "Nombre": nombre,
        "Telefono": telefono,
        "Email": email
    }

    #Agregando contacto a agenda
    agenda['Contactos'].append(contacto)
    print("Contacto creado exitosamente.")

    return agenda

def eliminar_contacto(agenda,posicion):

    agenda['Contactos'].pop(posicion)
    print("Contacto eliminado.")

    return agenda

def imprimir_agenda(agenda):
    if len(agenda['Contactos']) == 0:
        print ("Agenda vacía.")
    else:
        print(f"*******Numero de contactos: {len(agenda['Contactos']) }*****")
        for contacto in agenda['Contactos']:
            print('------------')
            for key, value in contacto.items():
                print(f"{key}: {value}.")

def imprimir_contacto(contacto):
    print("********Contacto********")
    for key, value in contacto.items():
        print(f"{key}: {value}.")

def buscar_contacto(agenda, nombre, opcion):
    if len(agenda['Contactos']) == 0:
        print ("Agenda vacía.")
    else:
        size = len(agenda['Contactos'])
        no_elemento = 0 
        found = False

        for contacto in agenda['Contactos']:
            if(contacto.get('Nombre') != nombre):
                no_elemento += 1
            else:
                found = True
                if (opcion == "2"):
                    imprimir_contacto(contacto)
                else:
                    agenda = eliminar_contacto(agenda,no_elemento)

  
        if(not found):
            print("Contacto no encontrado...")

    return agenda


def opciones():
    opcion = input("""Seleccione una opción:
            * 1. Visualizar Agenda
            * 2. Buscar Contacto por Nombre
            * 3. Crear Contacto
            * 4. Eliminar Contacto
            * 5. Salir
            --> """)
            
    return opcion

def inicio(agenda):

    seleccion = "0"
    while seleccion != "5":
        seleccion = opciones()
 
        if (seleccion == str(1)):
            imprimir_agenda(agenda)
            seleccion = "0"
        elif (seleccion == str(2) or seleccion == str(4)):
            if len(agenda['Contactos']) == 0:
                print("Agenda vacía.")
            else:
                persona = input("Digite nombre de contacto: ")
                agenda = buscar_contacto(agenda,persona,seleccion)
                seleccion = "0"
        elif (seleccion == str(3)):
            agenda = crear_contacto(agenda)
            seleccion = "0"
        elif (seleccion == str(5)):
            print("Gracias por usar la agenda. ¡Hasta luego!")
        else:
            print("Opcion incorrecta, seleccione una opción válida...")
            seleccion = "0"


inicio(mi_agenda)