respuesta = 'y'

while respuesta == 'y':
    nombre = input('Ingresa nombre: ')
    apellido = input('Ingresa apellido: ')
    numero = input('Ingresa numero: ')

    mi_archivo_texto = open('./clase_10/agenda.txt','a')
    mi_archivo_texto.write(f'{nombre} ,{apellido} ,{numero}\n')
    mi_archivo_texto.close()

    respuesta = input('¿Ingresar otro contacto? y/n  ')