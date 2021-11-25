from jugador import Jugador
from partida import Partida
import estados_jugador, estados_partida, file_handler, utils

jugadores = []
partidas = []

def menu_option():
    print('Torneo de Starcraft 2')
    try:
        return int(input('''
    1 - Crear Jugador
    2 - Crear Partida
    3 - Finalizar Partida
    4 - Mostrar Jugadores
    5 - Mostrar Partidas
    6 - Exportar Partidas y Jugadores
    0 - Para salir
    '''))
    except ValueError:
        return -1

def crear_jugador():
    nickname = input('Ingrese nickname del jugador:\n')
    if nickname != '':
        email = input('Ingrese email del jugador:\n')
        if email != '':
            raza = escoger_raza()
            if raza != '':
                id_jugador = generar_id_jugador()
                jugador = Jugador(id_jugador, nickname, email, raza)
                jugadores.append(jugador)
        else:
            utils.mostrar_mensaje_valor_invalido()
    else:
        utils.mostrar_mensaje_valor_invalido()

def escoger_raza():
    raza = ''
    print('Seleccione la Raza del jugador:')

    try:
        int_raza = int(input('''1 - Terran\n2 - Zerg\n3 - Protoss\n'''))

        if int_raza == 1:
            raza = 'Terran'
        elif int_raza == 2:
            raza = 'Zerg'
        elif int_raza == 3:
            raza = 'Protoss'
        else:
            utils.mostrar_mensaje_valor_invalido()
    except ValueError:
        utils.mostrar_mensaje_valor_invalido()

    return raza

def generar_id_jugador():
    if jugadores:
        ultimo_jugador : Jugador
        ultimo_jugador = jugadores[-1]
        ultimo_id_jugador = ultimo_jugador.get_id()
        return ultimo_id_jugador + 1
    else:
        return 1

def mostrar_jugadores():
    for jugador in jugadores:
        print(jugador.get_info())

def hay_jugadores_disponibles():
    jugadores_sin_jugar = 0
    index = 0
    while jugadores_sin_jugar < 2 and index != len(jugadores):
        if jugadores[index].get_estado() == estados_jugador.NO_JUGANDO or jugadores[index].get_estado() == estados_jugador.GANADOR:
            jugadores_sin_jugar +=1
        index +=1
    if jugadores_sin_jugar >=2:
        return True
    else:
        return False

def crear_partida():
    nombre = input('Ingrese el nombre de la partida\n')
    if nombre != '':
        jugador_a = buscar_jugador_a()
        if jugador_a:
            jugador_b = buscar_jugador_b(jugador_a)
            if jugador_b:
                id_partida = generar_id_partida()
                partida = Partida(id_partida, nombre, jugador_a, jugador_b)
                cambiar_estado_jugador_jugando(jugador_a)
                cambiar_estado_jugador_jugando(jugador_b)
                partidas.append(partida)
                print(partida.get_info())
    else:
        utils.mostrar_mensaje_valor_invalido()

def buscar_jugador(nickname):
    index = 0
    while index < len(jugadores):
        if jugadores[index].get_nickname() == nickname:
            if jugadores[index].get_estado() == estados_jugador.NO_JUGANDO or jugadores[index].get_estado() == estados_jugador.GANADOR:
                return jugadores[index]
            else:
                print('Jugador no disponible, por favor ingrese otro jugador')
                break
        index +=1
    if index == len(jugadores):
        print('Jugador no encontrado, intente de nuevo')

def buscar_jugador_a():
    nickname = input('Ingrese el nickname del jugador A:\n')
    return buscar_jugador(nickname)

def buscar_jugador_b(jugador : Jugador):
    nickname = input('Ingrese el nickname del jugador B:\n')
    jugador_b = buscar_jugador(nickname)
    if jugador_b:
        if int(jugador_b.get_id()) == int(jugador.get_id()):
            print('Jugador invalido, por ingrese jugadores diferentes')
        else:
            return jugador_b

def generar_id_partida():
    if partidas:
        ultima_partida : Partida
        ultima_partida = partidas[-1]
        ultimo_id_partida = ultima_partida.get_id()
        return ultimo_id_partida + 1
    else:
        return 1

def cambiar_estado_jugador_jugando(jugador : Jugador):
    index = 0
    while index < len(jugadores):
        if int(jugadores[index].get_id()) == int(jugador.get_id()):
            jugadores[index].set_estado(estados_jugador.JUGANDO)
            break
        index +=1

def hay_partidas_activas():
    partidas_activas = 0
    index = 0
    while partidas_activas < 1 and index != len(partidas):
        if partidas[index].get_estado() == estados_partida.ACTIVA:
            partidas_activas +=1
        index +=1
    if partidas_activas >=1:
        return True
    else:
        return False

def finalizar_partida():
    listar_partidas_activas()
    try:
        id_partida = int(input('Seleccione una partida:\n'))
        if id_partida_valido(id_partida):
            listar_jugadores_de_partida(id_partida)
            ganador = input('Seleccione al ganador: A o B\n')
            guardar_ganador_partida_cambiar_estado_partida(id_partida, ganador)
        else:
            utils.mostrar_mensaje_valor_invalido()
    except ValueError:
        utils.mostrar_mensaje_valor_invalido()

def listar_partidas_activas():
    print('Partidas Activas:\n')
    for partida in partidas:
        if partida.get_estado() == estados_partida.ACTIVA:
            print(f'{partida.get_id()} - {partida.get_nombre()}')

def id_partida_valido(id_partida):
    index = 0
    while index < len(partidas):
        if partidas[index].get_id() == id_partida:
            return True
        index +=1
    if index == len(partidas):
        return False

def listar_jugadores_de_partida(id_partida):
    print('Jugadores:')
    index = 0
    while index < len(partidas):
        if partidas[index].get_id() == id_partida:
            print(f'A: {partidas[index].get_jugador_a().get_nickname()} Raza: {partidas[index].get_jugador_a().get_raza()}')
            print(f'B: {partidas[index].get_jugador_b().get_nickname()} Raza: {partidas[index].get_jugador_b().get_raza()}')
        index +=1

def guardar_ganador_partida_cambiar_estado_partida(id_partida, ganador):
    index = 0
    while index < len(partidas):
        if partidas[index].get_id() == id_partida:
            if ganador == 'A':
                partidas[index].set_ganador(partidas[index].get_jugador_a())
                partidas[index].set_perdedor(partidas[index].get_jugador_b())
                
            elif ganador == 'B':
                partidas[index].set_ganador(partidas[index].get_jugador_b())
                partidas[index].set_perdedor(partidas[index].get_jugador_a())
                
            else:
                print('Opcion invalida, intente de nuevo')
                break
            
            
            partidas[index].get_ganador().set_puntos(3)
            partidas[index].get_ganador().set_estado(estados_jugador.GANADOR)
            partidas[index].get_perdedor().set_puntos(1)
            partidas[index].get_perdedor().set_estado(estados_jugador.INACTIVO)
            cambiar_estado_partida_finalizada(id_partida)
        index +=1

def cambiar_estado_partida_finalizada(id_partida):
    index = 0
    while index < len(partidas):
        if partidas[index].get_id() == id_partida:
            partidas[index].set_estado(estados_partida.FINALIZADA)
            break
        index +=1

def mostrar_partidas():
    for partida in partidas:
        print(partida.get_info())

opcion = menu_option()

while opcion != 0 :

    if opcion == 1:
        crear_jugador()
    if opcion == 2:
        if hay_jugadores_disponibles():
            crear_partida()
        else:
            print('No hay suficientes jugadores, por favor agregue un jugador')
    if opcion == 3:
        if hay_partidas_activas():
            finalizar_partida()
        else:
            print('No hay partidas activas, por favor cree una nueva partida')
    if opcion == 4:
        mostrar_jugadores()
    if opcion == 5:
        mostrar_partidas()
    if opcion == 6:
        file_handler.exportar_info_partidas(partidas)
        file_handler.exportar_info_jugadores(jugadores)
    if opcion == -1 or opcion > 6 or opcion < -1:
        utils.mostrar_mensaje_valor_invalido()

    opcion = menu_option()