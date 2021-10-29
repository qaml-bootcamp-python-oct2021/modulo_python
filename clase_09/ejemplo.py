# my_dict = {
#     'nombre' : 'David',
#     'apellido' : 'Gonzalez',
#     'edad' : 33,
#     'altura': 1.68
# }
# my_dict['email'] = 'ds.gon@outlook.com'

# if my_dict.get('email') is not None:
#     print(my_dict['email'])
# else:
#     print('No existe la Key')

''' Lista de Alumnos '''
alumnos = {
    'alumnos' : [
        {
            'nombre' : 'David',
            'edad' : 33,
            'pais' : 'Argentina',
            'libros':[
                {
                    'titulo' : 'TLOR'
                },
                {
                    'titulo' : 'Mujeres'
                },
            ]
        },
        {
            'nombre' : 'Antonieta',
            'edad' : 37,
            'pais' : 'Mexico'
        },
        {
            'nombre' : 'Ivan',
            'edad' : 18,
            'pais' : 'Mexico'
        }
    ]
}

nuevo_alumno = {
    'nombre' : 'Mariela',
    'edad' : 15,
    'pais' : 'Mexico'
}

alumnos['alumnos'].append(nuevo_alumno)

# for key in alumnos['alumnos'][0].keys():
#     print(key)

for alumno in alumnos['alumnos']:
    print('---- Alumno ----')
    for value in alumno.values():
        print(f'{value}')