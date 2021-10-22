num_mes = 1

def temporada (quemes):
    if num_mes >=3 and num_mes <=5:
        print ("usted esta en primavera. Disfrute :D")
    elif num_mes >=6 and num_mes <=8:
        print ("usted esta en verano. Tome agua!")
    elif num_mes >=9 and num_mes <=11:
        print ("Usted esta en Otonio. Vaya lavando la ropa de frio")
    elif num_mes == 12 or num_mes ==1 or num_mes==2:
        print ("Usted esta en invierno. Tapese bien")
    else: 
        print ("""El mes ingresado no existe
                Por favor verifique e intente de nuevo
                'La Gerencia'""")

temporada(num_mes)