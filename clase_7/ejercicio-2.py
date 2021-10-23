numero = 8
def sum_pares(num):
    cont=0 
    s = 0
    while(cont<num):
        if es_par(cont): 
            s+=cont
        cont += 1
    print(f"La sumatoria es: {s}")

def es_par(numero_f):
    if numero_f%2==0: return True
    return False

sum_pares(numero)