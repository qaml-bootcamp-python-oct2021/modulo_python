'''Try except'''
import logging

logging.basicConfig(filename='logs.log',encoding='UTF-8',level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s') #Configurar logs, guardarse en archivos

def division (num_a, num_b):
    logging.info('Inicia división::::::')    
    try:
        return num_a/num_b
    except ZeroDivisionError as error:
        logging.warning(f'No se puede dividir:: {error}')
        raise  ValueError ('Se lanza error  división de cero') #Lazar excepcion, se puede lanzar cualquioer tipo de  error
    except (TypeError,NameError) as error:
          logging.warning(f'Error en tipo o name:: {error}')
    except Exception as error:
          logging.warning(f'Error gral:: {error}')

def iniciar():
    try:
        logging.warning(division(10,0))
    except ValueError:
        logging.warning('No se puede realizar la operación')
    finally:
        logging.info('Siempre se ejecuta')    

iniciar()

