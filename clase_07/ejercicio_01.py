

def cal_suma(numero):
    contador=1
    suma=0
    while contador<numero:
        suma+=contador
        contador+=1
        print(suma)
    return suma


def cal_suma_pares(numero):
    contador=1
    suma=0
    while contador<numero:
        if(contador%2==0):
            suma+=contador
        contador+=1
        print(suma)
    return suma

print(f'Sumatoria: {cal_suma_pares(4)}')