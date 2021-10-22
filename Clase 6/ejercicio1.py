

mes = 1

if mes >=3 and mes<=5:
    print("Estamos en Primavera")
elif mes >=6 and mes<=8:
    print("Estamos en Verano")
elif mes >=9 and mes<=11:
    print("Estamos en Otoño")
elif mes  ==12 or mes >=1 and mes<=2 :
    print("Estamos en Invierno")
else: 
    print("""El mes ingresado no existe
             Por favor verifique e intente de nuevo
             'La Gerencia' """)