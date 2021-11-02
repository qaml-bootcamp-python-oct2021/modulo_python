#dictionarios - librería

from types import ClassMethodDescriptorType


def imprimir_libreria(libreria):
    for libro in libreria['libros']:
        print('-----Libros-----')
        for key, value in libro.items():
            print(f"{key}: {value}.")

my_bookstore = {
    'libros': [
        {
            'Titulo': "El Principito",
            'Autor': "Antoine de Saint-Exupéry",
            'Genero': "Infantil"
        },
        {
            'Titulo': "La Historia Interminable",
            'Autor': "Michael Ende",
            'Genero': "Fantasia"
        },
        {
            'Titulo': "Q&A",
            'Autor': "Vikas Swarup",
            'Genero': "Novela"
        }
    ]
}

#Agregar un nuevo libro
nuevo_libro = {
    'Titulo': "Cancion de Fuego y Hielo",
    'Autor': "George R.R. Martin",
    'Genero': "Novela"
}

imprimir_libreria(my_bookstore)

my_bookstore['libros'].append(nuevo_libro)

print("*******************************************")

imprimir_libreria(my_bookstore)
ClassMethodDescriptorType