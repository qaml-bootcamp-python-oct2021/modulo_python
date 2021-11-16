from tasks import Task
from assignees import Assignee
import file_handler

def convert_board_to_dict(task : Task):
    dict_task = {
        "title" : task.get_title(),
        "description" : task.get_description(),
        "priority" : task.get_priority(),
        "state" : task.get_state(),
        "assignee": task.get_assignee()
    }
    return dict_task

def convert_assignee_to_dict(assignee : Assignee):
    dict_assignee = {
        "name" : assignee.get_name(),
        "email" : assignee.get_email()
    }
    return dict_assignee

def get_tasks_from_file():
    list_tasks = []
    board = file_handler.read_board()
    tasks = board['tasks']
    for task in tasks:
        task_o = Task(task['title'],task['description'],task['priority'],task['assignee'])
        task_o.set_state(task['state'])
        list_tasks.append(task_o)
    return list_tasks

def get_assignees_from_file():
    list_assignees = []
    assignees = file_handler.read_users()
    users = assignees['assignees']
    for user in users:
        user_o = Assignee(user['name'],user['email'])
        list_assignees.append(user_o)
    return list_assignees
