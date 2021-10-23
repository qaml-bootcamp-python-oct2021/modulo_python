import random
def numero_aleatorio():
    return random.randint(1,10)
def multiplicar():
    num_aleatorio = numero_aleatorio()
    for number in range(1,10,1):
        res = number*num_aleatorio
        print(f"{num_aleatorio} x {number} = {res} \n")    
       
multiplicar()
