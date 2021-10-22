edad = 14
altura = 1.62

def verificar_edad(edad):
    return edad > 14

def verificar_altura(altura):
    return altura >= 1.62

def puede_subir_montania_rusa (edad,altura):
    
    if edad and altura:
        print('Puede subirse al "Push-Pull"')
    elif edad and not altura:
        print('No tiene altura necesaria')
    elif altura and not edad:
        print('No tiene edad necesaria')
    else:
        print('No cumple ninguno')

edad_valida = verificar_edad(edad)
altura_valida = verificar_altura(altura)

puede_subir_montania_rusa(edad_valida, altura_valida)