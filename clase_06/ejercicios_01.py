# primevera: Marzo 3, Abril 4, Mayo 5
# verano: Junio 6, Julio 7, Agosto 8
# otoño: Septiembre 9, Octubre 10, Noviembre 11
# invierno: Diciembre 12, Enero 1, Febrero 2

month_number = 11
    
if month_number == 3 or month_number == 4 or month_number == 5:
    print('primavera')
elif month_number == 6 or month_number == 7 or month_number == 8:
    print('verano')
elif month_number == 9 or month_number == 10 or month_number == 11:
    print('otoño')
elif month_number == 12 or month_number == 1 or month_number == 2:
    print('invierno')
else:
    print('''El mes ingresado no existe.
Por favor verifique e intente de nuevo 
"La Gerencia"''')