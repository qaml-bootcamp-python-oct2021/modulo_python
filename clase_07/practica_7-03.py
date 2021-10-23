numero_a = 5
numero_b = 8
numeroSiguiente = 0

if numero_a < numero_b:
    numero_a += 1
    while numero_a < numero_b:
        #numeroSiguiente = numero_a + 1
        #print(numeroSiguiente)
        #numero_a += 1
        print(numero_a)
        numero_a += 1
else:
    numero_b += 1
    while numero_b < numero_a:
        #numeroSiguiente = numero_b + 1
        #print(numeroSiguiente)
        #numero_b += 1
        print(numero_b)
        numero_b += 1