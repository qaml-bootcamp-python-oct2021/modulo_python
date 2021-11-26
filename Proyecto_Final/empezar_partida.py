from Jugador import Jugador
from Partidas import  Partida


import util
import Estados_Jugador
import Estados_Partidas
import file_handler
jugadores = []
partidas = []


def crear_jugador():
    nombre = input("Ingrese su nombre: ")
    email =  input("Ingrese un correo electronico")
    raza =   int(input('''
        ** Seleccione una opcion **
        1 - Terran
        2 - Zerg
        3 - Protoss
        '''))
    nuevo_jugador = Jugador(nombre, email, raza)
    jugadores.append(nuevo_jugador)
    print("Jugador creado exitosamente!")
    return nuevo_jugador


def crear_partida():
    nombre_partida = input("Ingrese el nombre de la partida: ")
    jugador_a =  input("Ingrese a Jugador A")
    jugador_b =  input("Ingrese a Jugador B")
    nueva_partida = Partida(nombre_partida, jugador_a, jugador_b)
    partidas.append(nueva_partida)
    print("Partida creada exitosamente!")
    return nueva_partida


def seleccionar_ganador(partida: Partida):
    opcion_ganador = input(f'''Seleccionar Ganador:
            {partida.get_info_jugadores}
             ''')
    ganador: Jugador = partida.get_jugadores().get(opcion_ganador)
    if opcion_ganador == 1:
        opcion_perdedor = 2
    else: opcion_perdedor = 1
    perdedor: Jugador = partida.get_jugadores().get(opcion_perdedor)
    partida.set_ganador(opcion_ganador)
    ganador.add_score(3)
    perdedor.add_score(1)
    ganador.set_status(Estados_Jugador.GANADOR)
    perdedor.set_status(Estados_Jugador.INACTIVO)


def exportar_archivo_jugadores():
    diccionario_jugador =  {'jugadores': []}
    for jugador in jugadores:
        diccionario_jugador['jugadores'].append(util.convertir_jugador(jugador))
    file_handler.exportar_resultado_jugadores(diccionario_jugador)

def exportar_archivo_partidas():
    diccionario_partidas = {'partidas': []}
    for partida in partidas:
        diccionario_partidas['partidas'].append(util.convertir_partida(partida))
    file_handler.existe_archivo_partidas(diccionario_partidas)


def get_menu():
    return int(input('''
    ** Seleccionar: **
    1 - Crear Jugador
    2 - Crear Juego
    3 - Seleccionar Ganador
    4 - Exportar Resultados Jugador
    5 - Exportar Resultados partida
    0 - Exit
    '''))


menu = get_menu()
while menu != 0:
    if menu == 1:
        crear_jugador()

    elif menu == 2:
        crear_partida()

    elif menu == 3:
        seleccionar_ganador()

    elif menu == 4:
        exportar_archivo_jugadores()
    elif menu == 5:
        exportar_archivo_partidas()
    else:
        print("Opcion no encontrada")
    menu = get_menu()