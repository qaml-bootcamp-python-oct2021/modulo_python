import random

random_number = random.randint(1,10)

def tabla_de_multiplicar(number_random):
    for number in range(10):
        number += 1
        result = number * number_random
        print(result)

tabla_de_multiplicar(random_number)