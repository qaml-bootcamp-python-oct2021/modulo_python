import os
import json



AGENDA_FILE='./clase_13/ejercicio_01_agenda/agenda.json'
def agenda_existe():
    if not os.path.exists(AGENDA_FILE):
        with open(AGENDA_FILE,'w') as file:
            json.dump({ "alumnos" : []},file)

def leer_agenda():
    agenda_existe()
    with open(AGENDA_FILE,'r') as file:
        data = json.load(file)
    return data  

def guardar_agenda(agenda):
    with open(AGENDA_FILE,'w') as file:
        json.dump(agenda,file)