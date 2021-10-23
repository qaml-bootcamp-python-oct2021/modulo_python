
def escalera(numero):

    for number in range(1,numero,1):
        res = number*'*'
        print(f"{res} \n")    
       
escalera(7)