import random
  
def lista_de_aleatorios():
    lista = []
    length_lista = 9
    for index in range(length_lista):
        numero_aleatorio = int(random.randint(1,10))
        lista.append(numero_aleatorio)
    print(f"La lista es: {lista}")
    return lista

def buscar_numeros_respetidos(lista):
    index = 0 
    count = 0
    while index < len(lista):
        if lista.count(lista[index]) > 1:
            count+=1
            break
        index+=1
    if count > 0: print(f"Hay  numeros repetidos en la lista")
    else: print(f"No existe numeros repetidos en la lista")

buscar_numeros_respetidos(lista_de_aleatorios())