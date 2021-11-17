from Task import Task
from User import User
import utils , file_handler, States

tasks = utils.get_tasks_from_file()
users = utils.get_users_from_file()

def menu_option():
    return int(input('''
    1 - Para crear una Tarea
    2 - Para crear un Usuario 
    3 - Para mostrar todas las Tareas
    4 - Para mostrar todos los Usuarios
    5 - Para editar estado de una tarea
    6 - Para mostrar las tareas por estado
    7 - Para mostrar las tareas por usuario
    8 - Para salir
    '''))

def add_task():
    title = input('Ingrese un titulo para la tarea\n')
    description = input('Ingrese una descripcion para la tarea\n')
    priority = input('Ingrese una prioridad \n')
    asigned_user = input('Asigne un usuario \n')
    task = Task(title, description, priority, asigned_user)
    tasks.append(task)
    update_list_tasks()

def update_list_tasks():
    task = {
        "tasks" : []
    }
    for task_i in tasks:
        task_dict = utils.convert_task_to_dict(task_i)
        task['tasks'].append(task_dict)
    file_handler.save_tasks(task)

def add_user():
    name = input('Ingrese un nombre para el usuario\n')
    email = input('Ingrese un email para el usuario\n')
    user = User(name, email)
    users.append(user)
    update_list_users()

def update_list_users():
    user = {
        "users" : []
    }
    for user_i in users:
        user_dict = utils.convert_user_to_dict(user_i)
        user['users'].append(user_dict)
    file_handler.save_users(user)

def print_data_task(task : Task):
    print(task.get_info())


def print_data_user(user : User):
    print(user.get_info())


def display_tasks():
    for task in tasks:
        print('---- Tasks ----')
        print_data_task(task)
        print()
        
def display_users():
    for user in users:
        print('---- Users ----')
        print_data_user(user)
        print()



def search_task():
    title = input('Ingrese el titulo de la tarea\n')
    index = 0
    while index < len(tasks):
        task :Task = tasks[index]
        if title == task.get_title():
            return task
        index += 1
    
    print('No existe la tarea con ese titulo')
    return None


def edit_state_task(task : Task):
    print(f'El estado actual de la tarea: {task.get_title()} es: {task.get_state()}')
    option = input('Desea modificar el estado? Y/N\n')
    if option == 'Y':
        option_state = int(input(f'''
        1 - Para {States.BACKLOG}
        2 - Para {States.TODO}
        3 - Para {States.DOING}
        4 - Para {States.RESOLVED}
        '''))
        guardar = utils.setear_state_task(task,option_state)
        
        if guardar:
            update_task(task)
            update_list_tasks()
            print('Estado actualizado satisfactoriamente')
            
def update_task(task : Task):
    index = 0
    result = False
    while index < len(tasks) and not result:
        task_lista :Task = tasks[index]
        if task.get_title() == task_lista.get_title():
            tasks[index] = task
            result = True
        index += 1
    if not result:
        print('No hay alumno en el listado de Alumnos con ese nombre.')

def state_task():
     print("Error No Solucionado")
def task_user():
     print("Error No Solucionado")

option = menu_option()

while option != 0 :

    if option == 1:
        add_task()
    if option == 2:
        add_user()
    if option == 3:
        display_tasks()
    if option == 4:
        display_users()
    if option == 5:
        task = search_task()
        if task is not None:
            edit_state_task(task)
    if option == 6:
        state_task()
    if option == 7:
        task_user()

    option = menu_option()