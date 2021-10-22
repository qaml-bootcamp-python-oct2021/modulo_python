# primevera: Marzo 3, Abril 4, Mayo 5
# verano: Junio 6, Julio 7, Agosto 8
# otoño: Septiembre 9, Octubre 10, Noviembre 11
# invierno: Diciembre 12, Enero 1, Febrero 2

month_number = 11

def now_season(month_number):
    
    if month_number >= 3 and month_number <= 5:
        print('primavera')
    elif month_number >= 6 and month_number <= 8:
        print('verano') 
    elif month_number >= 9 and month_number <= 11:
        print('otoño')
    elif month_number >= 12 and month_number <= 2:
        print('invierno')
    else:
        print('''El mes ingresado no existe.
Por favor verifique e intente de nuevo 
"La Gerencia"''')

now_season(month_number)