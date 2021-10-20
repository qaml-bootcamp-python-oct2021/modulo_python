def suma(a,b):
    return a+b

def resta(a,b):
    return b-a

def multiplicacion(a,b):
    return a*b

def div(a,b):
    return b/a

def modulo(a,b):
    return b%a

def int_to_float(num_int):
    return float(num_int)
    
a= 12.5
b= 34
print  (f'Suma:{suma(a,b)}')   
print  (f'Resta:{resta(a,b)}')   
print  (f'Multiplicación:{multiplicacion(a,b)}')   
print  (f'Mod:{modulo(a,b)}')   
print  (f'Int to float:{int_to_float(b)}') 
