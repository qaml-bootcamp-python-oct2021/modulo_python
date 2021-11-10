#Crea un script que basado en un número aleatorio pueda crear una escalera descendiente

import random
numero = random.randint(0,10)

for ciclo in range(numero):
    print('*' * ciclo)