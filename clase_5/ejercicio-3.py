billetera = 200
chocolate = 150
agua = 100

def imprimir_compra(total, saldo, dinero_suficiente):
    print(f"""Total de la compra: {total}
    Dinero Disponible en la billetera: {saldo} 
    El usuario tiene suficiente dinero para la compra?: {dinero_suficiente}""" ) 
def calcular_compra(pro1, pro2):
    return pro1 + pro2
def calcular_si_hay_suficiente_dinero(saldo, total):
    return saldo>=total

total = calcular_compra(chocolate, agua)
dinero_suficiente = calcular_si_hay_suficiente_dinero(billetera, total)
imprimir_compra(total, billetera,dinero_suficiente)

total = calcular_compra(chocolate, 0)
dinero_suficiente = calcular_si_hay_suficiente_dinero(billetera, total)
imprimir_compra(total, billetera,dinero_suficiente)
