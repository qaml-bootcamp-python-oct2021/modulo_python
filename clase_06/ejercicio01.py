def temporada(mes):
    if mes == 12 or mes ==1 or mes==2:
        print ("Es invierno")
    elif mes >=3 and mes <= 5:
        print("Es primavera")
    elif mes >= 6 and mes <= 8:
        print ("Es verano")
    elif mes >= 9 and mes <= 11:
        print ("Es otoño")
    else:
        print('''El mes ingresado no existe
        Por favor verifique e intente de nuevo
        'La Gerencia' ''')


temporada(10)