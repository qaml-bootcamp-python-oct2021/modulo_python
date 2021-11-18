from jugador import Jugador
from partida import Partida
import estados_jugador, estados_partida

jugadores = []
partidas = []

def menu_option():
    print('Torneo de Starcraft 2')
    return int(input('''
    1 - Crear Jugador
    2 - Crear Partida
    3 - Finalizar Partida
    4 - Mostrar Jugadores (temporal)
    5 - Mostrar Partidas (temporal)
    0 - Para salir
    '''))

def crear_jugador():
    nickname = input('Ingrese nickname del jugador\n')
    email = input('Ingrese email del jugador\n')
    raza = escoger_raza()    
    id_jugador = generar_id_jugador()
    jugador = Jugador(id_jugador, nickname, email, raza)
    jugadores.append(jugador)

def escoger_raza():
    raza = ''
    print('Escoja la raza que usara el jugador')

    int_raza = int(input('''
    1 - Terran
    2 - Zerg
    3 - Protoss
    '''))

    if int_raza == 1:
        raza = 'Terran'
    elif int_raza == 2:
        raza = 'Zerg'
    elif int_raza == 3:
        raza = 'Protoss'
    
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

def finalizar_partida():
    listar_partidas_activas()

def listar_partidas_activas():
    print('Partidas Activas:\n')
    for partida in partidas:
        if partida.get_estado() == estados_partida.ACTIVA:
            print(f'{partida.get_id()} - {partida.get_nombre()}')

def mostrar_partidas():
    for partida in partidas:
        print(partida.get_info())

#######################################################
#Jugadores temporales
jugador_1 = Jugador(1, 'MarceloXc', 'marcelo@email.com', 'Terran')
jugador_2 = Jugador(2, 'Oden222Xc', 'oden222@email.com', 'Zerg')
jugador_3 = Jugador(3, '4X33333Xc', '4x33333@email.com', 'Protoss')
jugador_4 = Jugador(4, 'Shiro44Xc', 'shiro44@email.com', 'Terran')
jugadores.append(jugador_1)
jugadores.append(jugador_2)
jugadores.append(jugador_3)
jugadores.append(jugador_4)
#Partidas temporales
partida_1 = Partida(1, 'Marcelo vs Oden', jugador_1, jugador_2)
cambiar_estado_jugador_jugando(jugador_1)
cambiar_estado_jugador_jugando(jugador_2)
partida_2 = Partida(2, '4X vs Shiro', jugador_3, jugador_4)
cambiar_estado_jugador_jugando(jugador_3)
cambiar_estado_jugador_jugando(jugador_4)
partidas.append(partida_1)
partidas.append(partida_2)
#######################################################

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
        finalizar_partida()
    if opcion == 4:
        mostrar_jugadores()
    if opcion == 5:
        mostrar_partidas()

    opcion = menu_option()