from Partida import Partida
from Jugador import Jugador
import jugador_functions
import json
import estado_jugador
import estado_partidas
import mensajes_
import utils
import file_handler

ganador =  estado_jugador.GANADOR
activo = estado_jugador.ACTIVO
jugando = estado_jugador.JUGANDO
inactivo = estado_jugador.INACTIVO

activas = estado_partidas.ACTIVAS
finalizadas = estado_partidas.FINALIZADAS

partidas = []
partidas = utils.obtener_partidas_desde_archivo()
# jugadores_l = []



def crear_partida():

    jugadores = {
      1: '',
      2: ''
    }
    adversario_segun_estado_p_jug= ''
    partida = None
    nombre_partida = input(f'{mensajes_.text_nombre_partida}')
    jugador_a_email = input(f'{mensajes_.text_introducir_correo}')
    jugador_a = jugador_functions.buscar_jugador(jugador_a_email.lower(), adversario_segun_estado_p_jug)
    

    while(jugador_a is None and jugador_a != 'Menu'):
      jugador_a =jugador_functions.estado_jugando_inactivo_unknown_menu()


    if(jugador_a is not None and type(jugador_a) is not str):
      
      if(jugador_a.get_estado() == ganador):
         adversario_segun_estado_p_jug = ganador
      elif jugador_a.get_estado() == activo: adversario_segun_estado_p_jug = activo
      
      jugador_b_email = input(f'{mensajes_.text_introducir_correo_adversario}')
      jugador_b_email = jugador_functions.verificar_nombres_repetidos(jugador_b_email, jugador_a.get_email())

      jugador_b = jugador_functions.buscar_jugador(jugador_b_email, adversario_segun_estado_p_jug)
    
      while(jugador_b is None  and jugador_b != 'Menu'): 
        jugador_b =jugador_functions.estado_jug_ganadores_activos_menu(adversario_segun_estado_p_jug, jugador_a.get_email())

      if(jugador_b is not None and type(jugador_b) is not str):

        jugador_a.set_estado(jugando)
        jugador_b.set_estado(jugando)
        
        if jugador_a.get_estado() == ganador and jugador_b.get_estado() == ganador:
           jugador_a.set_puntaje(jugador_a.get_puntaje())
           jugador_b.set_puntaje(jugador_b.get_puntaje())
        
        primer_jugador = jugador_a 
        segundo_jugador = jugador_b 
       
        jugadores[1] = primer_jugador
        jugadores[2] = segundo_jugador

        partida = Partida(nombre_partida,jugadores)
        partidas.append(partida)

        jugador_functions.actualizar_lista_de_jugadores()
        actualizar_lista_de_partidas()
        print("Partida Creada Exitosamente... :)")
    return partida


def actualizar_lista_de_partidas():
    partida = {
        "partidas" : []
    }
    for partida_a in partidas:
        partida_dict = utils.convertir_partida_a_dict(partida_a)
        partida['partidas'].append(partida_dict)
    file_handler.guardar_partidas(partida)


def print_info_partida(partida: Partida):
    print(partida.get_info_partida())

def mostrar_partidas():
    print("Todas las partidas: ")
    index = 0
    for partida in partidas:
        index+=1
        print(f'{mensajes_.ID_} {index}')
        print_info_partida(partida)
    return partidas
    
def finalizar_partida():
    partida_encontrada = buscar_en_partidas_activas()
    while partida_encontrada is None and partida_encontrada != 'Menu':
      partida_encontrada = mostrar_menu_partida_no_encontrada()

def mostrar_menu_partida_no_encontrada():
    opcion = int(input(f'''
       {mensajes_.text_opcion_seleccionar}
    0. {mensajes_.text_buscar_otra_partida}
    1. Mostrar {mensajes_.text_mostrar_partidas_activas} {activas}
    2. {mensajes_.text_salir_busqueda}
    '''
   ))
    return menu_partida_no_encontrada(opcion)

def menu_partida_no_encontrada(opcion):
   partida = None
   if opcion == 0:
      partida = buscar_en_partidas_activas()
   elif opcion == 1:
      mostrar_partidas_activas()
   else:
      partida = 'Menu'  
      print(f'{mensajes_.text_salir_menu}') 
   return partida

def buscar_en_partidas_activas():
    data_partidas = partidas_por_estado(activas)
    index = 0
    partida_encontrada = None
    
    nombre_partida = input(f'{mensajes_.text_nombre_partida}')
    nombre_partida = nombre_partida.lower()
    
    while index < len(data_partidas):
      if(data_partidas[index].get_nombre_partida().lower() == nombre_partida):
         partida_encontrada: Partida = data_partidas[index]
         print(f'La partida: "{partida_encontrada.get_nombre_partida()}" ha sido encontrada!')
         partida_encontrada = menu_preguntar_para_finalizar_partida(partida_encontrada)
         break
      index+=1
    if(partida_encontrada is None):
      print(f'{mensajes_.text_partida_no_encontrada}')
    return partida_encontrada

def menu_preguntar_para_finalizar_partida(partida_encontrada: Partida):

   opcion = int(input(f'''
   {mensajes_.text_confirmar_para_finalizar}
     1. Si
     2. No y salir del Menu
    '''
   ))
   if(opcion == 1):
      partida_encontrada = aceptar_finalizar_partida(partida_encontrada)
   else: 
      partida_encontrada = 'Menu'
      print(mensajes_.text_salir_menu)
   return partida_encontrada

def aceptar_finalizar_partida(partida_encontrada: Partida):
    jugador_1: Jugador = partida_encontrada.get_jugadores().get(1)
    jugador_1_nombre = jugador_1.get_nombre_jugador()
    #jugador_1_nombre = jugador_1.get('Nombre')
    #print('jugador_1_nombre', jugador_1_nombre)

    jugador_2: Jugador = partida_encontrada.get_jugadores().get(2)
    jugador_2_nombre = jugador_2.get_nombre_jugador()
    #jugador_2_nombre = jugador_2.get('Nombre')
    #print('jugador_2_nombre', jugador_2_nombre)

    print(f'{mensajes_.text_definir_ganador}')
    definir_ganador = definir_jugador_ganador_menu(jugador_1_nombre, jugador_2_nombre)
    if(definir_ganador == 1):
        #print('jugador_1_estado', jugador_1.get_estado())
        jugador_1.set_estado(ganador)
        jugador_1.dar_puntaje(3)
        jugador_2.set_estado(inactivo)
        jugador_2.dar_puntaje(1) 

    elif(definir_ganador == 2): 
        jugador_2.set_estado(ganador)
        jugador_2.dar_puntaje(3) 
        jugador_1.set_estado(inactivo)
        jugador_1.dar_puntaje(1)  
        
    partida_encontrada.set_estado(finalizadas)
    #print("Partida Actualizada: ", json.dumps(partida_encontrada.get_info_dict(),sort_keys=False, indent=5))
    print(f'Partida Actualizada: ')
    print_info_partida(partida_encontrada)
    jugador_functions.actualizar_lista_de_jugadores()
    actualizar_lista_de_partidas()
    return partida_encontrada


def definir_jugador_ganador_menu(jug_1, jug_2):
     print(f'''Lista de Jugadores en la partida: 
               1 - Para Jugador 1: {jug_1}
               2 - Para Jugador 2: {jug_2}
               ''')
     opcion_menu = int(input(f'{mensajes_.text_opcion_ganador}'))
     return opcion_menu

def partidas_por_estado(estado):
    data_partidas = []
    index = 0
    for partida in partidas:
        partida: Partida = partidas[index] 
        if(partida.get_estado() == estado):
           data_partidas.append(partida)
        index+=1
    return data_partidas

def mostrar_partidas_activas():
    partidas = partidas_por_estado(activas)
    index = 0
    print(f'Listando {mensajes_.text_mostrar_partidas_activas} {activas}')
    for partida in partidas:
        #partida: Partida = json.dumps(partida.get_info_dict(),sort_keys=False, indent=5)
        index+=1
        print(f'{mensajes_.ID_} {index}')
        print_info_partida(partida)
        #print(partida)

def finalizar_torneo():
    cantidad_partidas = len(partidas)
    cantidad_partidas_finalizadas = len(partidas_por_estado(finalizadas))
    cantidad_partidas_activas = len(partidas_por_estado(activas))

    jug_1 = partidas[cantidad_partidas-1].get_jugadores().get(1).get_puntaje() #get_info_jugador_dict().get('Puntos Ganados')
    jug_2 = partidas[cantidad_partidas-1].get_jugadores().get(2).get_puntaje() #get_info_jugador_dict().get('Puntos Ganados')

    if (cantidad_partidas%2==1 and cantidad_partidas == cantidad_partidas_finalizadas):
        jug_1 = partidas[cantidad_partidas-1].get_jugadores().get(1)
        jug_1_puntaje = jug_1.get_puntaje()
        jug_2 = partidas[cantidad_partidas-1].get_jugadores().get(2)
        jug_2_puntaje = jug_2.get_puntaje() 
        
        if(jug_1_puntaje > jug_2_puntaje):
           jug_ganador = jug_1.get_nombre_jugador()
           jug_g_p = jug_1_puntaje
        else: 
           jug_ganador = jug_2.get_nombre_jugador()
           jug_g_p = jug_2_puntaje

        print('El torneo ha finalizado....') 
        print(f'El ganador de la partida es el jugador: {jug_ganador} con un total de puntos: {jug_g_p}')   
    else:
      if (cantidad_partidas != cantidad_partidas_finalizadas):
            print(f'''
              El torneo no puede finalizar....
              Aun quedan {cantidad_partidas_activas}  partidas activas pendientes por finalizar.
            ''')  
      elif  (cantidad_partidas%2!=1):
             print(f'''
              El torneo no puede finalizar....
              Hay muchos Ganadores, defina un ganador programando una nueva partida.
            ''') 


