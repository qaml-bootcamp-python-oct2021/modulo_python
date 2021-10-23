#sumar numeros impares dentro el rango
result = 0
for numero in range(1,10):
    if numero % 2 == 0:
        print(f'este numero es par: {numero} y los numeros par no se procesan')
        continue
    result += numero

print(result)