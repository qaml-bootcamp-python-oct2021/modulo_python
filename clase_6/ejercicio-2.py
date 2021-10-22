

def permiso_subir_montania(edad, estatura):
    if p_edad and p_estatura:
       print("Puede subirse a la montania rusa 'Push-Pull'")
    elif not(p_edad) and estatura:
       print("No Puede subirse a la montania rusa 'Push-Pull' por la edad")
    elif p_edad and not(estatura):
       print("No Puede subirse a la montania rusa 'Push-Pull' por la estatura")
    else:
        print("No Puede subirse a la montania rusa 'Push-Pull' por que no cumple con la edad ni con la estatura")
def edad_valida(edad):
    return  edad > 14
def estatura_valida(estatura):
    return  estatura >= 1.62


edad, estatura = 15,1.63 
p_edad= edad_valida(edad)
p_estatura= estatura_valida(estatura)
permiso_subir_montania(p_edad, p_estatura)

edad, estatura = 14,1.63 
p_edad= edad_valida(edad)
p_estatura= estatura_valida(estatura)
permiso_subir_montania(p_edad, p_estatura)

edad, estatura = 16,1.61 
p_edad= edad_valida(edad)
p_estatura= estatura_valida(estatura)
permiso_subir_montania(p_edad, p_estatura)

edad, estatura = 10,1.60 
p_edad= edad_valida(edad)
p_estatura= estatura_valida(estatura)
permiso_subir_montania(p_edad, p_estatura)
