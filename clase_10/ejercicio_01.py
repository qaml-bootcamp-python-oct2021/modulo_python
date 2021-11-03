nombre = input('Ingrese el nombre\n')
apellido = input('Ingrese el apellido\n')
numero = input('ingrese el numero\n')

file = open('./clase_10/agenda.txt', 'a')
file.write(f'{nombre}, {apellido}, {numero}\n')
file.close()

file = open('./clase_10/agenda.txt', 'r')
agenda = file.read()
file.close()
print(agenda)
