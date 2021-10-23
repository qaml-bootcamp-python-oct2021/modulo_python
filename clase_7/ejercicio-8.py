import random
def numero_aleatorio():
    return random.randint(1,10) * 2

def suma():
    num_aleatorio = numero_aleatorio()
    # num_aleatorio = 6 
    cont = 1
    sum = 0
    print(f'Numero Aleatorio: {num_aleatorio}')
    while cont <= num_aleatorio:
        sum+=cont
        cont +=1
    print(f"Sumatoria Numeros {sum}")

suma()