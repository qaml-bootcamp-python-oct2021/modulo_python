#lista de paises

paises = 'México, Venezuela, Argentina, Brasil, Colombia, Panama'

lista_paises = paises.split(", ")

print(f"Cadena de países: {paises}")
print(f"Lista de paises: {lista_paises}")

lista_paises.append("Chile")

print(f"Lista de paises + Chile: {lista_paises}")

lista_paises.sort()

print(f"Lista de paises ordenada: {lista_paises}")

paises = "::".join(lista_paises)

print(f"Nueva cadena con nuevo formato: {paises}")
