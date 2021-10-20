#Ejercicio 5.03 - Tony De La Torre

saldo = 200
chocolate = 150
agua = 100

def transaccion(monto_compra,balance):
    res = monto_compra <= balance
    return res


resultado = transaccion(chocolate+agua,saldo)
print(f"Monto de la compra: {chocolate+agua}")
print(f"Saldo: {saldo}")
print(f"¿Saldo suficiente?: {resultado}")

resultado = transaccion(agua,saldo)
print(f"Monto de la compra: {agua}")
print(f"Saldo: {saldo}")
print(f"¿Saldo suficiente?: {resultado}")