from Jugador import Jugador
import estado_jugador
import mensajes_
import utils
import file_handler

jugadores = []
partidas = []


jugadores_activos = []
jugadores_ganadores = []


activo =   estado_jugador.ACTIVO
inactivo = estado_jugador.INACTIVO
jugando =  estado_jugador.JUGANDO
ganador =  estado_jugador.GANADOR


jugadores = utils.obtener_jugadores_desde_archivo()

def crear_jugador():
    nombre = input("Ingresar Nombre del jugador Nuevo: ")
    email  = input("Ingresar E-mail del jugador: ")
    raza   = int(input('''Seleccionar una opcion para la raza del jugador: 
         1 - Para Terran
         2 - Para Zerg
         3 - Para Protoss
    '''))
    nuevo_jugador = Jugador(nombre, email, raza)
    jugadores.append(nuevo_jugador)
    
    actualizar_lista_de_jugadores()
    print(f'{mensajes_.text_jugador_adicionado}')
    return nuevo_jugador

def actualizar_lista_de_jugadores():
    jugador = {
        "jugadores" : []
    }
    for jugador_a in jugadores:
        jugador_dict = utils.convertir_jugador_a_dict(jugador_a)
        jugador['jugadores'].append(jugador_dict)
    file_handler.guardar_jugadores(jugador)



def print_info_jugador(jugador: Jugador):
    print(jugador.get_info_jugador())

def mostrar_jugadores():
    index = 0
    print(f'{mensajes_.text_listar_todos_los_jugadores}')
    for jugador in jugadores:
        index+=1
        print(f'{mensajes_.ID_} {index}')
        print_info_jugador(jugador)
    return jugadores
    
def estado_jugando_inactivo_unknown_menu():
   opcion = int(input(f'''
       {mensajes_.text_opcion_seleccionar}
    1. {mensajes_.text_buscar_otro_jugador}
    2. {mensajes_.text_mostrar_jugador_estado} {activo}
    3. {mensajes_.text_mostrar_jugador_estado} {ganador}
    4. {mensajes_.text_salir_busqueda}
    '''
   ))
   return menu_busqueda_todo_estado(opcion)

def estado_jug_ganadores_activos_menu(adversario_estado, jugador_email_a):
  opcion = int(input(f'''
        {mensajes_.text_opcion_seleccionar}
     0. {mensajes_.text_buscar_otro_jugador} {adversario_estado}
     1. {mensajes_.text_mostrar_jugador_estado} {adversario_estado}
     2. {mensajes_.text_anular_partida}
     '''
   ))
  return menu_busqueda_ganador_activo(opcion, adversario_estado, jugador_email_a)

def print_jugadores_activos(jugador: Jugador):
    return jugador.get_estado()

def mostrar_jugadores_por_estado(estado):
    index = 0
    print(f'{mensajes_.text_listar_jugador_estado} {estado}')
    for jugador in jugadores:
        index+=1
        if( print_jugadores_activos(jugador) == estado):
          print(f'{mensajes_.ID_} {index}')
          print_info_jugador(jugador)
          if estado == activo: jugadores_activos.append(jugador)
          elif estado == ganador: jugadores_ganadores.append(jugador)
    return None

def consultar_lista_ganadores_activos(estado):
    data_jugadores = []
    for jugador in jugadores:
        if( print_jugadores_activos(jugador) == estado):
           data_jugadores.append(jugador)
    return data_jugadores

def buscar_jugador_todos_estados(jugador_email):
    index = 0
    jugador_to_append = None
    flag_inactivo_jugando = False
    while index < len(jugadores):
     jugador: Jugador = jugadores[index]
     if(jugador_email == jugador.get_email().lower()):
        if(jugador.get_estado() == activo or jugador.get_estado() == ganador):
             jugador_to_append = jugador
             if jugador.get_estado() == ganador:
                 print(f'''{mensajes_.text_jugador_gano_partidas}
                           {jugador.get_info_basica_jugador()}''')
                 print(f'{mensajes_.text_adicionado_a_partida}')
                 print(f'Nota: El adversario debe estar con estado: {ganador}')
             else:
                 print(f'''{mensajes_.text_jugador_encontrado}
                           {jugador.get_info_basica_jugador()}''')
                 print(f'{mensajes_.text_adicionado_a_partida}')
             break
        elif jugador.get_estado() == jugando or jugador.get_estado() == inactivo:
             if jugador.get_estado() == jugando:
                print(f'''{mensajes_.text_jugador_en_partida} {jugando}, no puede jugar esta partida
                          {jugador.get_info_basica_jugador()}''')
             else:
                print(f'''El jugador se encuentra con estado {inactivo}, no puede jugar...
                          {jugador.get_info_jugador()}''')
             jugador_to_append = None 
             flag_inactivo_jugando = True
             break
     index+=1
      
    if(jugador_to_append is None and flag_inactivo_jugando is False): 
            print(f'El jugador con el correo electronico: {jugador_email} no ha sido encontrado... :(')
          
    return jugador_to_append 

def buscar_adversario_segun_estado_p_jug(jugador_email, es_adversario_estado):
    index = 0
    jugador_ganador_to_append = None
    data_consulta = consultar_lista_ganadores_activos(es_adversario_estado)
    while index < len(data_consulta): 
     jugador: Jugador = data_consulta[index]
     if(jugador_email == jugador.get_email().lower()):
        print(f'''{mensajes_.text_jugador_encontrado}
                     {jugador.get_info_basica_jugador()}
                   ''')
        jugador_ganador_to_append = jugador
        break
     index+=1
    if(jugador_ganador_to_append is None): 
        print(f'El jugador con el correo electronico: {jugador_email} no ha sido encontrado en la lista de jugadores con estado: {es_adversario_estado}')

    return jugador_ganador_to_append 
         
def buscar_jugador(jugador_email, es_adversario):
    if es_adversario != '':
        jugador = buscar_adversario_segun_estado_p_jug(jugador_email, es_adversario)
    else:
        jugador = buscar_jugador_todos_estados(jugador_email) 
    
    return jugador

def menu_busqueda_todo_estado(opcion):
    jugador = None
    #if opcion == 0:
        #jugador = crear_jugador()
    if opcion == 1:
        jugador_email = input(f'{mensajes_.text_introducir_correo}')
        jugador_email = jugador_email.lower()
        jugador = buscar_jugador(jugador_email,'')
    elif opcion == 2:
        jugador = mostrar_jugadores_por_estado(activo)

        if len(jugadores_activos) == 0:
            print(f'{mensajes_.text_sin_jug_activos}')
            jugador = 'Menu'

    elif opcion == 3:
        jugador = mostrar_jugadores_por_estado(ganador)
        
        if len(jugadores_ganadores) == 0:
           print(f'{mensajes_.text_sin_jug_gandores}')
           jugador = 'Menu'
    else:
        jugador = 'Menu' 
        print(f'{mensajes_.text_salir_menu}') 
    return jugador

def menu_busqueda_ganador_activo(opcion, adversario_estado, jugador_email_a):
    jugador = None
    if opcion == 0:
     jugador_email_adversario = input(f'{mensajes_.text_introducir_correo_adversario}')
     jugador_email_adversario_verf = verificar_nombres_repetidos(jugador_email_adversario,jugador_email_a)
     jugador = buscar_adversario_segun_estado_p_jug(jugador_email_adversario_verf, adversario_estado)
    #elif opcion == 1:
     #   jugador = crear_jugador()
    elif opcion == 1:
     mostrar_jugadores_por_estado(adversario_estado)
    else:
        jugador = 'Menu'  
        print(f'{mensajes_.text_salir_menu}') 
    return jugador

def verificar_nombres_repetidos(jugador_b_email, jugador_a_email):
    jugador_a_email = jugador_a_email.lower()
    jugador_b_email = jugador_b_email.lower()
    while jugador_b_email == jugador_a_email:
         print(mensajes_.text_nombres_repetidos)
         jugador_b_email = input(f'{mensajes_.text_introducir_correo_adversario}')
    return jugador_b_email.lower()

