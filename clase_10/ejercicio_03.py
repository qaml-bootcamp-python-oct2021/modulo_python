import logging, time

var_a = 5
var_b = 0

logging.basicConfig(level=logging.INFO, filename='./clase_10/logs.log', format='%(levelname)s - %(asctime)s - %(message)s')

def division(num_a, num_b):
    try:
        return num_a / num_b
    except ZeroDivisionError:
        raise ValueError('Divisor invalido: 0')

def operacion(num_a, num_b):
    result = 0
    try:
        result = division(num_a, num_b)
        logging.info('Division exitosa')
    except ValueError:
        logging.warning('No se pudo realizar la operacion debido a divisor invalido 0')
        result = -1
    finally:
        print('fin del programa')
    return result


print(operacion(var_a, var_b))
print(operacion(var_b, var_a))