#Ejercicio 6.02 - Tony De La Torre

a = 14
h = 1.62

def ride(age,height):
    if age >= 14 and height >= 1.62:
        print('Bienvenido a Push-Pull... ¡Diviértete!')
    elif age < 14 and height >= 1.62:
            print('Visitante no cumple requerimientos mínimos de edad.')
    elif age >= 14 and height < 1.62:
            print('Visitante no cumple requerimientos mínimos de estatura.') 
    else:
        print('Visitante no cumple requerimientos mínimos de edad ni estatura.') 

ride(a,h)
