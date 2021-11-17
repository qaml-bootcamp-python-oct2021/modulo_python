import os , json

TASK_FILE = 'task.json'
USER_FILE = 'user.json'

task = {
    "tasks" : []
}
user = {
    "users" : []
}

    
def file_task_exists():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE,'w') as file:
            json.dump(task,file)

def file_user_exists():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE,'w') as file:
            json.dump(user,file)
            
def read_tasks():
    file_task_exists()
    with open(TASK_FILE,'r') as file:
        data = json.load(file)
    return data

def read_users():
    file_user_exists()
    with open(USER_FILE,'r') as file:
        data = json.load(file)
    return data

def save_tasks(task):
    with open(TASK_FILE,'w') as file:
        json.dump(task,file)

def save_task(task):
    task = read_tasks()
    task['tasks'].append(task)
    with open(TASK_FILE,'w') as file:
        json.dump(task,file)

def save_users(user):
    with open(USER_FILE,'w') as file:
        json.dump(user,file)

def save_user(user):
    user = read_tasks()
    user['users'].append(user)
    with open(USER_FILE,'w') as file:
        json.dump(user,file)

