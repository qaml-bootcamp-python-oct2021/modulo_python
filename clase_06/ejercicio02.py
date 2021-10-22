edad_persona = 14
tamaño_persona = 1.55

def validar_edad(edad):
    if edad > 14:
        return True
    else:
        return False

def validar_tamaño(tamaño):
    if tamaño_persona>=1.62:
        return True
    else:
        return False

def subir_montaña_rusa(edad_montaña,tamaño_montaña):
    edad_valida = validar_edad(edad_montaña)
    tamaño_valido = validar_tamaño(tamaño_montaña)

    if edad_valida == True and tamaño_valido == True:
        print('Sí se puede subir a la montaña rusa "Push-Pull"')
    elif edad_valida == True and tamaño_valido == False:
         print('No se puede subir a la montaña rusa "Push-Pull" porque no tiene el tamaño necesario')
    elif edad_valida == False and tamaño_valido == True:
        print('No se puede subir a la montaña rusa "Push-Pull" porque no tiene la edad necesaria')
    else:
        print('No se puede subir a la montaña rusa "Push-Pull" porque no tiene el tamaño ni edad necesarios')


subir_montaña_rusa(edad_persona,tamaño_persona)