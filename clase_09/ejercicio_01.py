
libreria = {
    'libros' : [
        {
            'titulo' : 'La luna azul',
            'autor' : 'Alicia Delgado',
            'genero' : 'Novela'
        },
        {
            'titulo' : 'Bolita de patas',
            'autor' : 'Juan Lazos',
            'genero' : 'Infantil'
        },
        {
            'titulo' : 'El lago de la colina',
            'autor' : 'Paola Machado',
            'genero' : 'Drama'
        }
    ]
}


libreria = {
    'libros' : []
}

def crear_libro(titulo,autor,genero):
    return {
        'titulo':titulo,
        'autor':autor,
        'genero':genero
    }

def guardar_libro(libro):
    libreria['libros'].append(libro)


    

['libros']


print(libros.items)