import os , json

BOARD_FILE = 'board.json'
USERS_FILE = 'assignees.json'

users = {
    "assignees" : []
}

board = {
    "tasks" : []
}
    
def board_exists():
    if not os.path.exists(BOARD_FILE):
        with open(BOARD_FILE,'w') as file:
            json.dump(board,file)

def users_exists():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE,'w') as file:
            json.dump(users,file)

def read_board():
    board_exists()
    with open(BOARD_FILE,'r') as file:
        data = json.load(file)
    return data

def read_users():
    users_exists()
    with open(USERS_FILE,'r') as file:
        data = json.load(file)
    return data

def save_board(board):
    with open(BOARD_FILE,'w') as file:
        json.dump(board,file)

def save_users(users):
    with open(USERS_FILE,'w') as file:
        json.dump(users,file)
