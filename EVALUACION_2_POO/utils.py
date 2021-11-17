from Task import Task
from User import User
import file_handler , States

def convert_task_to_dict(task : Task):
    dict_task = {
        "title" : task.get_title(),
        "description" : task.get_description(),
        "priority" : task.get_priority(),
        "asigned_user" : task.get_asigned_user(),
        "state" : task.get_state()
    }
    return dict_task

def convert_user_to_dict(user : User):
    dist_user = {
        "name" : user.get_name(),
        "email" : user.get_email(),
    }
    return dist_user

def get_tasks_from_file():
    list_tasks = []
    tasks = file_handler.read_tasks()
    tasks = tasks['tasks']
    for task in tasks:
        task_o = Task(task['title'],task['description'],task['priority'], task['asigned_user'])
        task_o.set_state(task['state'])
        list_tasks.append(task_o)
    return list_tasks

def get_users_from_file():
    list_users = []
    users = file_handler.read_users()
    users = users['users']
    for user in users:
        user_o = User(user['name'],user['email'])
        list_users.append(user_o)
    return list_users

def convert_state_option(option):
    if option == 1:
        return States.BACKLOG
    elif option == 2:
        return States.TODO
    elif option == 3:
        return States.DOING
    elif option == 4:
        return States.RESOLVED
    else:
        return None

def setear_state_task(task : Task, option_state):
    guardar = True
    if option_state == 1:
        task.set_state(States.BACKLOG)
    elif option_state == 2:
        task.set_state(States.TODO)
    elif option_state == 3:
        task.set_state(States.DOING)
    elif option_state == 4:
        task.set_state(States.RESOLVED)
    else:
        print('Opcion invalida, intente de nuevo.')
        guardar = False
    return guardar