#Construye un script que permita almacenar libros en una librería
#Los datos que componen el libro son: título, autor y género.
#'título' : 'The Hitchhiking Guide To Load Testing Projects: A Fun, Step-by-Step Walk-Through Guide',
#'autor' : 'Leandro Melendez',
#'genero' : 'Educación Tecnológica'

libreria = {
    'libros' : []
}

def crear_libro(titulo,autor,genero):
    return {
        'titulo' : titulo,
        'autor' : autor,
        'genero' : genero
    }

def guardar_libro(libro):
    libreria['libros'].append(libro)

def print_libros():
    for libro in libreria['libros']:
        print(libro)



libro = crear_libro(input('Introduce el nombre del título del libro\n'), input('Introduce el nombre del autor del libro\n'),input('Introduce el genero al que pertenece el libro\n'))
guardar_libro(libro)
print_libros()
