agua = 100
chocolate = 150

def compra_dos_productos(billetera):

    total_compra = suma(agua,chocolate)
    compra_disponible = billetera >= total_compra

    print(f'El total de la compra es: {total_compra}')
    print(f'El usuario tiene disponible: {billetera}')
    print(f'La compra se puede hacer {compra_disponible}')

def compra_un_producto(billetera,precio):

    total_compra = precio
    compra_disponible = billetera >= total_compra
    disponible = resta(billetera,total_compra)

    print(f'El total de la compra es: {total_compra}')
    print(f'El usuario tiene disponible: {billetera}')
    print(f'La compra se puede hacer {compra_disponible}')
    print(f'Disponible: {disponible}')


def suma(item1,item2):
    return item1 + item2

def resta(item1,item2):
    return item1 - item2


compra_dos_productos(200)
compra_un_producto(200,100)