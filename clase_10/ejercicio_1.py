def crear_contacto():
    nombre = input('Ingrese nombre de contacto\n')
    apellido = input('Ingrese apellido de contacto\n')
    numero = input('Ingrese nuumero de contacto\n')
    contacto = f'{nombre}, {apellido}, {numero}'
    return contacto

my_agenda = open('./clase_10/agenda.txt','a')
my_agenda.write(crear_contacto())
my_agenda.close()
