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

def division(num_a,num_b):
    try:
        return num_a/num_b
    except TypeError:
        log.warning('No se puede dividir datos que no sean numeros')
        raise ValueError('Numeros invalidos')
    except ZeroDivisionError:
        log.warning('No se puede dividir por cero')
        raise ValueError('Numeros invalidos')
    except Exception as err:
        log.warning(f'Error general: {err}')
        raise ValueError('Numeros invalidos')

def operacion():
    result = 0
    try:
        result = division(10,5)
        log.info('Division Exitosa')
    except ValueError:
        log.warning('No se pudo dividir los nuemros')
        result = -1
    finally:
        return result

print(operacion())