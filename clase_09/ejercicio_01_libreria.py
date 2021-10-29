libreria=[]
def almacenar_libro(libro):
    libreria.append(libro)

def crear_libro(titulo, autor, genero):
    libro= {
        'titulo': titulo,
        'autor':autor,
        'genero':genero   
    }
    return libro
    
def imprimir_libros():
    for libro in libreria:
            print(f'Libro:::  {libro}')

almacenar_libro(crear_libro('titulo A','Autor A', 'Genero A'))
almacenar_libro(crear_libro('titulo B','Autor B', 'Genero B'))
imprimir_libros()