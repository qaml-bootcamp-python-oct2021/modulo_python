import random
def numero_aleatorio():
    return random.randint(1,10)

def numero_usuario():
    numero = int(input("Ingrese un numero: "))
    return numero

def adivinar_numero_usuario():
    cont = 1
    num_aleatorio = numero_aleatorio()
    num_usuario = numero_usuario()
    print(f"Numero aleatorio era: {num_aleatorio}")
    while(num_aleatorio != num_usuario):
        print("--------------------------------------------------")
        num_usuario = numero_usuario()
        cont +=1

    if num_aleatorio == num_usuario:
        print(f"Numeros iguales: {num_usuario} = {num_aleatorio}")
        print(f"Numero de intentos: {cont}")    
       
        
adivinar_numero_usuario()
