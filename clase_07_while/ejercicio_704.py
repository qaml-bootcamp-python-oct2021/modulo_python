#Ejercicio 7.04 - Tony De La Torre

import random

valor_aleatorio = random.randint(0,10)
numero_usuario = -1

#validar numero de entrada
"""def validar_numero(input):
    if (int(input) < 0 or int(input) > 10):
        print(f"Numero ingresado fuera de rango: {input}")
        return False
    else:
        return True"""

#imprimiendo numeros entre A y B
def adivinar(random_no,user_no):
    intentos = 1
    while(random_no != user_no):

        user_no = int(input('Ingrese un número entre del 0 al 10:'))
        
        """while(not validar_numero(user_no)):
            user_no = input('Ingrese un número entre del 0 al 10:')"""

        if(user_no==random_no):
            print(f"¡Felicidades! Has adivinado el número ({user_no}). Te tomó {intentos} intento(s).")
        else:
            print(f"Lo siento, no has adivinado, vuelve a intentarlo.")
            intentos += 1


adivinar(valor_aleatorio,numero_usuario)

