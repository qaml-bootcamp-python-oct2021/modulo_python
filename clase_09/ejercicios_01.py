#Construye un script que permita guardar los registros de un contacto telefónico en un archivo de texto de la siguiente forma:
#nombre, apellido, número

nombre = input('Ingrese el nombre del contacto:\n')
apellido = input('Ingrese el apellido del contacto:\n')
numero = input('Ingrese el numero del contacto:\n')

file = open('nuevo_archivo','a')
file.write(f'{nombre} , {apellido}, {numero}\n')
file.close