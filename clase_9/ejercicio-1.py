#libreria = dict()
#libros_j = []
libreria = {
    'libros': []
}
def almacenar_libros(libro_f):
    libreria['libros'].append(libro_f)
    print(libreria)

libro_1 = {
   "titulo": "Titulo_01",
   "autor": "Autor_01",
   'genero': "Genero_01"
}
libro_2 = {
   "titulo": "Titulo_02",
   "autor": "Autor_02",
   'genero': "Genero_02"
}
almacenar_libros(libro_1)
almacenar_libros(libro_2)
