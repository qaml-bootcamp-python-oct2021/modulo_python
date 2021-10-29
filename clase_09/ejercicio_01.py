#libreria

libreria = {
    'libros' : [

    ]
}

def crear_libro(titulo, autor, genero):
    return {
        'titulo' : titulo,
        'autor' : autor,
        'genero' : genero
    }

def agregar_libro(libro):
    libreria['libros'].append(libro)

def print_libros(libreria):
    for libro in libreria['libros']:
        print(libro)

libro = crear_libro('HP 1', 'JKR', 'Fantasia')
agregar_libro(libro)
libro = crear_libro('HP 2', 'JKR', 'Fantasia')
agregar_libro(libro)
libro = crear_libro('HP 3', 'JKR', 'Fantasia')
agregar_libro(libro)

print_libros(libreria)