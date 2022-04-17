import jugador_functions;
import partidas_functions;


def get_menu():
    return int(input('''
    ** Seleccionar: **
    1 - Crear Jugador
    2 - Mostrar todos los Jugadores
    3 - Crear Partida
    4 - Mostrar todas las partidas
    5 - Finalizar Partida
    6 - Finalizar Torneo
    0 - Exit
    '''))


def seleccionar_opcion(menu):
    while menu != 0:
        if menu == 1:
            jugador_functions.crear_jugador()
        elif menu == 2:
            jugadores = jugador_functions.mostrar_jugadores()
            if len(jugadores) == 0:
               print("Sin jugadores, continue adicionando un nuevo jugador")
        elif menu == 3:
            partidas_functions.crear_partida()
        elif menu == 4:
            partidas_functions.mostrar_partidas()
        elif menu == 5:
            partidas_functions.finalizar_partida()
        elif menu == 6:
            partidas_functions.finalizar_torneo()
        else:
            print("Opcion no encontrada")
        menu = get_menu()

menu = get_menu()
seleccionar_opcion(menu)