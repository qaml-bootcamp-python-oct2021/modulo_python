billetera = 200
chocolate = 150
agua = 100

def calcular_monto_total(item1, item2):
    return item1 + item2

def monto_disponible(monto):
    print(f'El monto disponible es: {monto}') 

def posible_compra(total,disponible):
    diferencia = disponible >= total
    print('Tiene suficiente credito? {}'.format(diferencia))

def pagar(total, disponible):
    disponible -= total
    return disponible

def mensaje_costo_total(total):
    print(f'El costo total es {total}')    

def mensaje_saldo_disponible(saldo):
    print(f'el saldo disponible es: {saldo}')

    

#escenario 1
total = calcular_monto_total(chocolate,agua)
mensaje_costo_total(total)
posible_compra(total,billetera)
saldo = pagar(total,billetera)
mensaje_saldo_disponible(saldo)

print('------------------------------------')

#escenario 2
total = agua
mensaje_costo_total(total)
posible_compra(total,billetera)
saldo = pagar(total,billetera)
mensaje_saldo_disponible(saldo)

