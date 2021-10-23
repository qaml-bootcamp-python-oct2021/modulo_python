agua = 100
chocolate = 150

def dos_productos(saldo):

    total_compra = suma(agua,chocolate)
    disponible = saldo >= total_compra

    print(f'El total de la compra es: {total_compra}')
    print(f'El usuario tiene disponible: {saldo}')
    print(f'La compra se puede hacer {disponible}')

def un_producto(saldo,precio):

    total_compra = precio
    compra_disponible = saldo >= total_compra
    disponible = resta(saldo,total_compra)

    print(f'El total de la compra es: {total_compra}')
    print(f'El usuario tiene disponible: {saldo}')
    print(f'La compra se puede hacer {compra_disponible}')
    print(f'Disponible: {disponible}')


def suma(item1,item2):
    return item1 + item2

def resta(item1,item2):
    return item1 - item2


dos_productos(200)
un_producto(200,100)