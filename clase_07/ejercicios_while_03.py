# script dado 2 numeros muestre todos los numeros que existen entre ambos

def mostrar_numeros_en_medio (num_mayor, num_menor):
    num_medios = num_menor + 1
    while num_mayor > num_medios:
        print(num_medios)
        num_medios +=1
        
        
mostrar_numeros_en_medio(10,0)

