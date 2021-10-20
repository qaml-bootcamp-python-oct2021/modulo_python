def compra(saldo,chocolate, agua):
    costo_total= chocolate+agua
    compra_posible=  saldo>= costo_total
    print(f'Saldo inicial = {saldo}')
    print(f'Costo total = {costo_total}')
    print(f'Compra es posible = {compra_posible}')
    print(f'Saldo despues de la compra = {saldo-costo_total}')

compra(200, 150, 100)
compra(200, 150, 0)