libreria = {
    'libros' : [
        {
            'titulo' : 'LibroA',
            'autor' : 'AutorA',
            'genero' : 'GeneroA'
        },
        {
            'titulo' : 'LibroB',
            'autor' : 'AutorB',
            'genero' : 'GeneroB'
        },
        {
            'titulo' : 'LibroC',
            'autor' : 'AutorC',
            'genero' : 'GeneroC'
        }
    ]
}

print(libreria)

def nuevoLibro(titulo,autor,genero):
    return{
        'titulo' : titulo,
        'autor' : autor,
        'genero' : genero 
    }

#def ingresarLibro(libro)

#alumnos['alumnos'].append(nuevo_alumno)