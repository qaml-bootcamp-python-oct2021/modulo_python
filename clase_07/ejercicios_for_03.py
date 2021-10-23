import random

def crear_escalera():
    num = random.randint(1,10)
    print(num)
    for x in range(num+1):
        linea = '*' * x
        print(linea)

crear_escalera()