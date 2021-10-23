import random



def iniciar_juego():
    numero_aleatorio=random.randint(1,10)
    print(f'Número aleatorio: {numero_aleatorio}')
    numero_usuario=0
    intentos=0

    while numero_aleatorio != numero_usuario:
        numero_usuario=pedir_numero()
        intentos+=1
    return intentos

def pedir_numero():
    return int(input('Ingrese un numero del 1 al 10:: '))

print(f'Intentos realizados hasta encontrar el numero aleatorio: {iniciar_juego()}')