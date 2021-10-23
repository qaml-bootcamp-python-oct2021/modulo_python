numero_a = 8
numero_b = 3


def es_numero_mayor(numero1, numero2):
    if (numero1>numero2): return numero1
    return numero2
def es_numero_menor(numero1, numero2):
    if (numero1<numero2): return numero1
    return numero2

def numeros_entre(numero1, numero2):
    mayor = es_numero_mayor(numero1, numero2)
    menor = es_numero_menor(numero1, numero2)
    numeros = ''
    mayor = mayor -1
    while menor < mayor:
        menor+=1
        numeros += '{},'.format(menor)
    print(f"{numeros}")
        
numeros_entre(numero_a, numero_b)

# numero += 'f{numero}'


