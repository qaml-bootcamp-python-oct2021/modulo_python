billetera = 200
chocolate = 150
agua = 100

def imprimir_msg(total, saldo, dinero_suficiente):
    print(f"""Total de la compra: {total}
    Dinero Disponible en la billetera: {saldo} 
    El usuario tiene suficiente dinero para la compra: {dinero_suficiente}""" ) 
def calcular_compra_saldo(saldo, total):
    imprimir_msg(total, saldo, saldo>=total)

calcular_compra_saldo(billetera,(chocolate+agua))
calcular_compra_saldo(billetera,chocolate)