#Escribe un script que dado la edad de una persona y su altura pueda determinar si la misma puede o no subirse en la montaña rusa "Push-Pull", dado que se debe ser mayor a 14 años y tener una altura no menor de 1.62.
#El script debe ser capaz de informar si puede o no subirse y en el caso de que no, por que razón(Si por edad, por tamaño u ambas)

edad= 13
altura = 1.52

def acceso_juego(edad,altura):
    if edad >14 and altura >=1.62:
        print('Puedes acceder al juego \"Pull-Push\"')
    elif edad <= 14 and altura >=1.62:
        print('No cuentas con la edad necesaria para acceder al juego \"Pull-Push\"')
    elif edad >14 and altura <1.62:
        print('No cuentas con la estatura minima necesaria para acceder al juego \"Pull-Push\"')
    else:
        print('No cuentas con la edad y altura necesaria para acceder al juego \"Pull-Push\"')
    
acceso_juego(edad,altura)