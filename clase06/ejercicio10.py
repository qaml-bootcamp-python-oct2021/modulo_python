import  random

resultado = 1
while resultado != 0:
    a = random.randint(-5,5)
    b = random.randint(-5,5)
    resultado = (a * b)
    print(f"{a}*{b} = {resultado}")