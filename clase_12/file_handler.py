agenda = {
    "alumnos" : []
}

def leer_agenda():
    agenda_existe()
    with open(AGENDA_FILE,'r') as file:
        data = json.load(file)
    return data

def agenda_existe():
    if not os.path.exists(AGENDA_FILE):
        with open(AGENDA_FILE,'w') as file:
            json.dump(agenda,file)


def guardar_alumno(alumno):
    agenda_data = leer_agenda()
    agenda_data['alumnos'].append(alumno)
    with open(AGENDA_FILE,'w') as file:
        json.dump(agenda_data,file)