#tipos de archivos: Texto, excel, json, xml.

#--------------------------------------------------
#manejo de archivos
#--------------------------------------------------
#abrir archivo:
open()

#leer archivos:
#leer todo el archivo
read()
#lee solo una linea
readline()
#regresa una lista con cada ñinea que existe en el archivo
readlines()

#escribir archivo
write()

#cerrar archivo:
close()

#--------------------------------------------------
#paths
#--------------------------------------------------
#windows: \
#Linux: /
#python identifica el separador para el SO en uso:
import os
sep = os.path.sep
print/('my_path{}to_folder{}to_file.txt'.format(sep,sep))

#--------------------------------------------------
#generar archivo
#--------------------------------------------------
file = open('my_file_test.txt','a')
file.write('This is my data to storage')
file.close

file = open('./clase_10/archivo_ejemplo.txt','a')
file.write('Este es mi primer archivo')
file.close

#Los archivos al momento de escribirse se pueden guardar en modo:
#append (a) = suma la informacion al archivo
#overwrite (w) = sobreescribe la informacion del archivo
file = open('my_file_test','a')
file.write('This is my data storage\n')
file.write('This is other data to storage\n')
file.close()

file = open('my_file_test.txt','w')
file.write('This data will replace the old data storaged\n')
file.close()

#--------------------------------------------------
#leer archivo
#--------------------------------------------------
#modo read (r)
#metodo read()
file = open('my_file_test.txt','r')
print(file.read())
file.close()

my_file = open('./clase_10/archivo_ejemplo.txt','r')
data = my_file.read()
my_file.close()
print(data)

#metodo readline()
file = open('my_file_test.txt','r')
print(file.readline())
print(file.readline())
file.close()

my_file = open('./clase_10/archivo_ejemplo.txt','r')
print(my_file.readline())
print(my_file.readline())
my_file.close()
 
#readlines()
#que imprima todo menos la ultima linea >> print(line[:-1])
file = open('my_file_test.txt','r')
lines = file.readlines()
for line in lines:
    print(line[:-1])
file.close()

#--------------------------------------------------
#with = es otra forma de lectura que permite trabajar con recursos como archivos
#--------------------------------------------------
with open('mi_agenda.csv','r') as my_file:
    print(my_file.read())
#ya no es necesario cerrar el archivo, with funcione como un bloque condicional donde cerrara la lectura del archivo al fianlizar.
my_file = open('mi_agenda.csv','r')
print(my_file.read())
my_file.close

#--------------------------------------------------
#archivos json = lenguaje ideal para el intercambio de datos
#--------------------------------------------------
#esta compuesto por el esquema de key:value
{
    'name' : 'frank',
    'age' : 39,
    'isEmployed' : True
}

#es necesaria la librearia para que funcione:
import json

with open('./clase_10/mi_archivo_json.json','r') as file:
    #el json se transforma a un tipo diccionario para poder manipularlo
    #load es para deserializar
    data = json.load(file)
    print(type(data))
    
    nuevo_contacto = {
        'nombre':"Pepito",
        'telefono':1234,
        'email':"pepito@mail.com"
    }
    data['contactos'].append(nuevo_contacto)
    print(data)

#json.dump() = para escribir la data de un diccionario a un archivo json
#dump = serializar, de un objeto diccionario, por ejemplo, a json
import json

contact_list = []
#levantar un archivo json y convertirlo para manipularlo
with open('mi_archivo_json.json','r') as file:
    data = json.load(file)
    contact_list = data['contactos']

#operaciones que queramos realizar en el json
with open('mi_archivo_json.json','r') as file:
    new_contact = {
        "nombre":"Santiago",
        "telefono":"123456789",
        "mail":"mail@mail.com"
    }
    contact_list.append(new_contact)
    data['contactos']=contact_list
    
    #para escribir en el json, se indica la data que se quiere grabar y el archivo donde se quiere grabar
    json.dump(data,file)

#al final queda terminada la escritura, lo guarda en el formato que corresponde
with open('mi_archivo_json.json','r') as file:
    data=json.load(file)
    for contact in data['contactos']:
        print(contact)