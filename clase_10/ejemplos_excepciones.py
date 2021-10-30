''' Try / Except '''




# numero = 11
# if numero % 2 == 0:
#     print('Numero par')
# else:
#     raise ValueError('El numero no es impar')

# try:
#     with open('test.txt','r') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('Al archivo de datos no existe, por ende no se puede ejecutar el Test')

import logging

logging.basicConfig(level=logging.DEBUG,filename='./clase_10/logs.log',format='%(levelname)s - %(asctime)s - %(message)s')
log = logging.getLogger()

num_a = 10
num_b = None

result = 0
try:
    try:
        result = num_a/num_b
        logging.info('Division Exitosa')
    except TypeError:
        logging.warning('No se puede dividir datos que no sean numeros')
        raise ValueError('Numeros invalidos')
    except ZeroDivisionError:
        logging.warning('No se puede dividir por cero')
        raise ValueError('Numeros invalidos')
    except Exception as err:
        logging.warning(f'Error general: {err}')
        raise ValueError('Numeros invalidos')    
except ValueError:
    logging.warning('No se pudo dividir los numeros')
    result = -1
finally:
    print(result)
