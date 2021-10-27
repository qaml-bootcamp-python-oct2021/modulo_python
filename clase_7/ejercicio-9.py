# Metodo Sort
lista  = [1, 10,11,2,3]
lista.sort()
print(lista) 

# Metodo JOIN: Convierte una lista en un string con un separador
lista  = ["1", "2","3","4"]
string = "-".join(lista)
print(string) 

# Metodo Split: Convierte un string en una lista pasandole un separador
string  = '1,2,3,4'
lista = string.split(',')
print(lista) 

# Metodo Extend: Unir dos listas
lista_a  = [1, 2,3,4]
lista_b =  ['a', 'b']
lista_res = lista_a.extend(lista_b)
print(lista_res) 

# Clonar una lista
lista_a  = [1, 2,3,4]
lista_b =  lista
lista_c = list(lista_a)

print(f"{lista_a == lista_b}") 
print(lista_a == lista_c) 

# contar un elemento 'x' en una lista
lista_a = ['a', 'b', 'c', 'b']
item_b = lista_a.count('b')
print(item_b)
