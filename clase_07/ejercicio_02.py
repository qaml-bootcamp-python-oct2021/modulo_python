def imprimir_numeros_formato(numero_a, numero_b):
    numero=numero_a+1
    cadena_numero=''
    while(numero< numero_b):
        cadena_numero+=f'{numero},'
        numero+=1
    print(cadena_numero)

def imprimir_numeros(numero_a, numero_b):
    numero_in=numero_a+1
    while(numero_in< numero_b):
        print(numero_in)
        numero_in+=1

num_inicial=5
num_final=8
imprimir_numeros_formato(num_inicial,num_final)