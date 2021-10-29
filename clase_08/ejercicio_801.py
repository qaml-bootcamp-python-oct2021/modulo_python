import random

valor_aleatorio  = random.randint(1,10)
my_list = [1,2,3,4,5]


def imprimir_lista(lista):
    print(lista)
    print(f"Tamaño de la lista: {len(lista)}")

def agregar_a_lista(lista,valor):
    lista.append(valor)
    return lista

def remover_de_lista(lista,indice):
    lista.pop(indice)
    return lista

def encontrar_en_lista(lista,valor):
    indice = 0

    if lista.count(valor) == 0:
        return -1
    else:
        size = len(lista)

        while (lista[indice] != valor):
            indice += 1

        return indice

def decision_lista(lista,valor):
    posicion = encontrar_en_lista(lista,valor)
    nueva_lista = []

    print("-----Lista Inicial-----")
    imprimir_lista(lista)

    print(f"Valor aleatorio: {valor}")

    print("¿Se encuentra en la lista?")
    if(posicion == -1):
        print("No se encuentra en la lista, agregando valor...")
        nueva_lista = agregar_a_lista(lista,valor)
    else:
        print("Valor ya existe en la lista, eliminando valor...")
        nueva_lista = remover_de_lista(lista,posicion)

    print("-----Lista Final-----")
    imprimir_lista(lista)


decision_lista(my_list,valor_aleatorio)

