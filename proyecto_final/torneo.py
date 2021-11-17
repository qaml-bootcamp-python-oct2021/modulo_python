from jugador import Jugador

jugadores = []
#Jugadores temporales
jugador_1 = Jugador(1, 'MarceloXc', 'marcelo@email.com', 'Terran')
jugador_2 = Jugador(2, 'Oden222Xc', 'oden222@email.com', 'Zerg')
jugador_3 = Jugador(3, '4X33333Xc', '4x33333@email.com', 'Protoss')
jugador_4 = Jugador(4, 'Shiro44Xc', 'shiro44@email.com', 'Terran')
jugadores.append(jugador_1)
jugadores.append(jugador_2)
jugadores.append(jugador_3)
jugadores.append(jugador_4)

def menu_option():
    print('Torneo de Starcraft 2')
    return int(input('''
    1 - Crear Partida
    2 - Crear Jugador
    3 - Finalizar Partida
    4 - Mostrar Jugadores (temporal)
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

opcion = menu_option()

while opcion != 0 :

    if opcion == 1:
        # if len(jugadores) < 2:
        #     print('Necesita dar de alta al menos 1 usuario antes de crear una tarea')
        # else:
        #     crear_tarea()
        pass
    if opcion == 2:
        crear_jugador()
    if opcion == 3:
        pass
    if opcion == 4:
        mostrar_jugadores()

    opcion = menu_option()