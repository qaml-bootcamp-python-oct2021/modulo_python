edad = 13
altura = 1.60

def subeMontana(edad,altura):
    if edad >= 14 and altura >= 1.64:
        print('La persona puede subir a la montaña rusa')
    else:
        if edad < 14 and altura >= 1.64:
            print('La persona no puede subir a la montaña rusa, la edad minima es 14 años')
        elif edad >= 14 and altura < 1.64:
            print('La persona no puede subir a la montaña rusa, la altura minima es 1.64 metros')
        elif edad < 14 and altura < 1.64:
            print('La persona no puede subir a la montaña rusa, la edad y la altura minima es 14 años y 1.64 metros')

subeMontana(edad,altura)