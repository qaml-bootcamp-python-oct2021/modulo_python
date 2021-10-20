#Desarrolla un script que dado un monto de dinero en la billetera (200)el usuario 
#pueda o no comprar un chocolate (150)y un agua (100) y que informe el costo total el 
#dinero disponible e imprima si el usuario tiene el dinero disponible para comprarlo
#hacer el mismo escenario pero solo con uno de los productos
# variables 
billetera = 200
choco = 150
agua = 100

totalcompra = choco + agua

def Noalcanza ():
    return billetera >= totalcompra 

def solochoco ():
    return billetera >= choco

def soloagua ():
    return billetera >= agua 

saldo1 = billetera - totalcompra
saldo2 = billetera - choco
saldo3 = billetera - agua

#Escenario 1
print (f'"La compra total es": {totalcompra}')
print (f'"No es posible llevarte ambas cosas": {Noalcanza()}')
print (f'"El saldo es": {saldo1}')
print ("-----------------")

#Escenario 1
print (f'"La compra total es": {totalcompra}')
print (f'"Te puedes llevar un chocolate": {solochoco()}')
print (f'"Tu saldo es": {saldo2}')
print ("-----------------")

#Escenario 1
print (f'"La compra total es": {totalcompra}')
print (f'"Te puedes llevar un agua": {soloagua()}')
print (f'"Tu saldo es": {saldo3}')
print ("-----------------")