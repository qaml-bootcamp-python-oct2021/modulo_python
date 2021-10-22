dineroBilletera = 200
chocolate = 150
agua = 100

costoTotal = chocolate + agua
disponible = dineroBilletera >= costoTotal
print(f'El costo total es de {costoTotal}')
print(f'Tu dinero disponible es {dineroBilletera}')
print(f'¿Tienes suficnete dinero para comprarlo? {disponible}')