my_dicc = {
    'libros' : [
    {
        'titulo' : 'titulo1',
        'autor' : 'autor1',
        'genero' : 'genero1',
    }
    ]
}

print(my_dicc.values())

nuevo_libro = {
    'titulo' : 'titulo2',
    'autor' : 'autor2',
    'genero' : 'genero2'
}

my_dicc['libros'].append(nuevo_libro)

print('-----nuevo libro----')
print(my_dicc.values())
