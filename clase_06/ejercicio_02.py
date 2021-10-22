def validar_edad(edad):
    return edad > 14

def validar_altura(altura):
    return altura >= 1.62

def validar_permisos(edad,altura):
    if validar_edad(edad) and validar_altura(altura):
        print('El usuario puede montar la montaña rusa')
    elif not validar_edad(edad) and validar_altura(altura):
        print('El usuario no puede montar la montaña rusa por que no cumple con la edad')
    elif validar_edad(edad) and not validar_altura(altura):
        print('El usuario no puede montar la montaña rusa por la altura insuficiente')
    else:
        print('El usuario no cumple con ambos requisitos para montar la montaña rusa')

validar_permisos(15,1.61)