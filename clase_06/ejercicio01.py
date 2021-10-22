def temporada(mes):
    if mes == 12 or mes ==1 and mes==2:
        print ("Es invierno")
    elif mes >=3 and mes <= 5:
        print("Es primavera")
    elif mes >= 6 and mes <= 8:
        print ("Es verano")
    elif mes >= 9 and mes <= 12:
        print ("Es otoño")
    else:
        print("Error. Verifique por favor")


temporada(10)