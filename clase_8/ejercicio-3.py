from operator import index
import random
val_tupla = (1,2,3,4,5)

def length_tuple(val_tupla_a):
    length = len(val_tupla_a)
    print(f"La longitud es: {length}")
    return length
def numero_aleatorio():
    return random.randint(1,5)
def encontrar_numero_repetido(val_tupla_a):
    val_numero_aleatorio = numero_aleatorio()
    index = 0
    while index < len(val_tupla_a):
        if(val_tupla_a[index] == val_numero_aleatorio):
            break
        index+=1
    # print(f"nueva tupla{nueva_tupla}")

length_tuple(val_tupla)
encontrar_numero_repetido(val_tupla)