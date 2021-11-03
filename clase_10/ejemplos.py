# ''' Creacion de Archivo '''
# my_file = open('./clase_10/archivo_ejemplo.txt','a')
# my_file.write('''Esto es un parrafo
# que tiene multioples 
# lineas''')
# my_file.close()

# ''' Lectura - Read '''
# my_file = open('./clase_10/archivo_ejemplo.txt','r')
# data = my_file.read()
# my_file.close()
# print(data)

# ''' Lectura - Readline '''
# my_file = open('./clase_10/archivo_ejemplo.txt','r')
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# my_file.close()

# ''' Lectura - Readlines '''
# my_file = open('./clase_10/archivo_ejemplo.txt','r')
# lines = my_file.readlines()
# my_file.close()
# for line in lines:
#     if 'parrafo' in line:
#         print(line[:-1])


# ''' Lectura - With'''
# lines = []
# with open('./clase_10/archivo_ejemplo.txt','r') as my_file:
#     lines = my_file.readlines()

# for line in lines:
#     if 'parrafo' in line:
#         print(line[:-1])


''' Archivo - JSON '''
import json
data = None
with open('./clase_10/mi_archivo_json.json','r') as json_file:
    data = json.load(json_file)


nuevo_contacto = {
    'nombre': "Pepito",
    'telefono':1234,
    'email': "pepito@mail.com"
}
data['contactos'].append(nuevo_contacto)



with open('./clase_10/mi_archivo_json.json','r') as json_file:
    print(json.load(json_file))