#Desarrollar un script que dado un monto de dinero en la billetera (200), el usuario pueda o no comprar un chocolate (150) y un agua (100) y que informe el costo total, el dinero disponible e imprima si el usuario tiene suficiente dinero para commprarlo.

billetera = 200
chocolate = 150
agua = 100

print("Comprar ambos productos")
def comprarproductos(billetera,chocolate,agua):
    compra_total = chocolate + agua
    presupuesto_total = billetera >= compra_total
    saldo_faltante = compra_total - billetera
    print(f'La compra total es de: {compra_total}')
    print(f'¿Cuento con el presupuesto para comprar ambos productos?{presupuesto_total}')
    print(f'El saldo faltante para realizar la compra es de: {saldo_faltante}')
comprarproductos(billetera,chocolate,agua)

print("-----------")

#Hacer el mismo escenario pero solo con alguno de los dos productos (chocolate o agua)

print("Comprar chocolate")
def comprarchocolate(billetera,chocolate):
    total_chocolate = chocolate
    presupuesto_chocolate = billetera >= total_chocolate
    saldo_chocolate = billetera - total_chocolate
    print(f'El costo del chocolate es: {total_chocolate}')
    print(f'¿Cuento con el presupuesto para comprar el chocolate? {presupuesto_chocolate}')
    print(f'El saldo final después de comprar el chocolate es de: {saldo_chocolate}')
comprarchocolate(billetera,chocolate)

print("-----------")
print("Comprar agua")
def compraragua(billetera,agua):
    total_agua = agua
    presupuesto_agua = billetera >= total_agua
    saldo_agua = billetera - total_agua
    print(f'El costo del agua es: {total_agua}')
    print(f'¿Cuento con el presupuesto para comprar el agua? {presupuesto_agua}')
    print(f'El saldo final después de comprar el agua es de: {saldo_agua}')
compraragua(billetera,agua)