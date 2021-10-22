edad_persona = 14
tamaño_persona = 1.55

def validar_edad(edad):
    return edad > 14

def validar_tamaño(tamaño):
    return tamaño >= 1.62
       
def subir_montaña_rusa(edad_montaña,tamaño_montaña):
    edad_valida = validar_edad(edad_montaña)
    tamaño_valido = validar_tamaño(tamaño_montaña)

    if edad_valida and tamaño_valido :
        print('Sí se puede subir a la montaña rusa "Push-Pull"')
    elif edad_valida and not tamaño_valido:
         print('No se puede subir a la montaña rusa "Push-Pull" porque no tiene el tamaño necesario')
    elif not edad_valida and tamaño_valido:
        print('No se puede subir a la montaña rusa "Push-Pull" porque no tiene la edad necesaria')
    else:
        print('No se puede subir a la montaña rusa "Push-Pull" porque no tiene el tamaño ni edad necesarios')


subir_montaña_rusa(edad_persona,tamaño_persona)