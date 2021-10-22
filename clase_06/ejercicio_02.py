def validar_edad(edad):
     return (edad>14)

def validar_estatura(estatura): 
     return (estatura>=1.62)


def subir_montania(edad, altura):
    if validar_edad(edad) and validar_estatura(altura):
         print("Puede subir a la montaña rusa")
    else: 
        print("No puede subir a la montaña rusa debido a ")
        if not validar_edad(edad): 
            print("No cumple con la edad minima")
        if not validar_estatura(altura):
            print ("No cumple con la altura minima")

subir_montania(15,1.70)