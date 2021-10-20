billetera = 200
chocolate = 150
agua = 100


def calcular_compra(pro1, pro2):
    return pro1 + pro2
def calcular_si_hay_suficiente_dinero(saldo, total):
    return saldo>=total
def calcular_saldo_disponible(billetera, total):
    return billetera-total
def imprimir_compra(total, saldo, dinero_suficiente):
    print(f"Total de la compra: {total}")
    print(f"Saldo Disponible: {saldo}")
    print(f"El usuario tiene suficiente dinero para la compra?: {dinero_suficiente}") 
    
total = calcular_compra(chocolate, agua)
saldo = calcular_saldo_disponible(billetera,total)
dinero_suficiente = calcular_si_hay_suficiente_dinero(billetera, total)
imprimir_compra(total, saldo,dinero_suficiente)

print('-------------------------')

total = agua
saldo = calcular_saldo_disponible(billetera,total)
dinero_suficiente = calcular_si_hay_suficiente_dinero(billetera, total)
imprimir_compra(total, saldo,dinero_suficiente)
