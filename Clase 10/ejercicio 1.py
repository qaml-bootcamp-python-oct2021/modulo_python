nombre = input('Dame el Nombre:\n')
apellido = input('Dame el Apellido:\n')
numero = input('Dame el Numero:\n')

file = open('mi_archivo','a')
file.write(f"{nombre} , {apellido}, {numero}\n")
file.close

