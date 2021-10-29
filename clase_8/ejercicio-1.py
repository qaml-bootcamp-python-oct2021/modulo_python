import random
def length_lista(lista):
    return  len(lista)
    
def numero_aleatorio_esta_en_lista(lista):
    lenght_lista_val = length_lista(lista)
    print(f"Longitud lista: {lenght_lista_val}")
    numero_aleatorio = random.randint(1,10)
    # numero_aleatorio = 5
    lista.append(numero_aleatorio)
    print(f"Lista actual adicionando numero aleatorio : {lista}")
    
    if lista.count(numero_aleatorio) > 1:
       index = 0 
       while index < len(lista):
           if numero_aleatorio == lista[index]:
              lista.pop(index)
              break
           index+=1
    else: lista.pop(0)
    print(f"Longitud lista actual: {lenght_lista_val}")
    print(f"Lista actual: {lista}")
    
numero_aleatorio_esta_en_lista([1,2,3,4]) 