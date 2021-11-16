from tasks import Task
from assignees import Assignee
import priorities, states, utils, file_handler


#declaring initial lists
my_tasks = utils.get_tasks_from_file()
my_assignees = utils.get_assignees_from_file()


#main menu
def main_menu():
    return int(
        input("""
        **** Agile Board - Main Menu ***
        1. Create Assignee.
        2. Create Task.
        3. Transition Task.                
        4. Show Board.
        5. Show Tasks by State.
        6. Show Tasks by Assignee.
        7. Exit
        """)
    )

#Create assignee
def create_assignee(assignees):
    name = input('Enter assignee\'s name:\n')
    email = input('Enter assignee\'s e-mail:\n')
    assignee = Assignee(name,email)
    assignees.append(assignee)
    update_assignee(assignees)
    return assignees

#Assignee list transformed into a dictionary to have whole current list overwritten on the file
def update_assignee(assignees):
    usrs = {
        "assignees" : []
    }
    for user in assignees:
        user_dict = utils.convert_assignee_to_dict(user)
        usrs['assignees'].append(user_dict)
    file_handler.save_users(usrs)

#Display full list of registered assignees in a numbered list. 
def print_assignees(assignees):
    index = 1

    print("---- List of available assignees: ----")
    for person in assignees:
        print(f"{index}.- {person.get_assignee_info()}")
        index += 1

#Return selected assignee for task creation. If a wrong option is entered, error message is shown.
def select_assignee(assignees):

    print_assignees(assignees)
    choice = -1
    name = ''

    while choice not in range(len(assignees)):
        choice = int(input("Select task's assignee by index: "))
        choice-= 1
        
        if choice in range(len(assignees)):
            name = assignees[choice].get_name()
        else:
            print("Wrong selection, please select an assignee from the list (by index):")
            choice = -1

    return name

#Prompts user to select priority. Returns pre-set priority value.
def select_priority():

    priority = -1
    priority_value = ''

    print("""
            Choose task\'s priority:
            1. High.
            2. Medium.
            3. Low.
            """)

    while priority not in range(4):

        priority = int(input("--> "))

        if priority == 1:
            priority_value = priorities.HIGH
        elif priority == 2:
            priority_value = priorities.MEDIUM
        elif priority == 3:
            priority_value = priorities.LOW
        else:
            print("Wrong selection, please select a valid priority from the list:")
            priority = -1
    
    return priority_value

#Prompts user to select Task State. Returns pre-set task value.
def select_state():

    state = -1
    state_value = ''

    print("""
            Choose task\'s state:
            1. Backlog.
            2. To Do.
            3. In Progress.
            4. Resolved
            """)

    while state not in range(5):

        state = int(input("--> "))

        if state == 1:
            state_value = states.BACKLOG
        elif state == 2:
            state_value = states.TODO
        elif state == 3:
            state_value = states.INPROGRESS
        elif state == 4:
            state_value = states.RESOLVED
        else:
            print("Wrong selection, please select a valid priority from the list:")
            state = -1
    
    return state_value


#Transition task. Backlog -> To Do -> In Progress -> Resolved. If task is already resolved, message will be displayed
def transition_task(tasks):

    if not tasks:
        print("We're sorry, Board is currently empty...")
    else:

        index = 1

        for task in tasks:
            print(f"{index}.- {task.get_task_info()}")
            print("----------------------------------")
            index += 1

        choice = -1

        while choice not in range(len(tasks)):
            choice = int(input("Select task by index: "))
            choice -= 1
            
            if choice in range(len(tasks)):

                if tasks[choice].get_state() == states.BACKLOG:
                    print(f"Transitioning Task \'{tasks[choice].get_title()}\' from {tasks[choice].get_state()} to {states.TODO}")
                    tasks[choice].set_state(states.TODO)
                    update_task(tasks)
                elif tasks[choice].get_state() == states.TODO:
                    print(f"Transitioning Task \'{tasks[choice].get_title()}\' from {tasks[choice].get_state()} to {states.INPROGRESS}")
                    tasks[choice].set_state(states.INPROGRESS)
                    update_task(tasks)
                elif tasks[choice].get_state() == states.INPROGRESS:
                    print(f"Transitioning Task \'{tasks[choice].get_title()}\' from {tasks[choice].get_state()} to {states.RESOLVED}")
                    tasks[choice].set_state(states.RESOLVED)
                    update_task(tasks)
                else:
                    print(f"Task \'{tasks[choice].get_title()}\' is already {tasks[choice].get_state()}")           
            else:
                print("Wrong selection, please select a task list (by index):")
                choice = -1


#Create task and assign to existing assignee. If assignees don't exist, user cannot create task. All tasks are created with default state = Backlog
def create_task(tasks, assignees):

    if not assignees:
        print("No assignees registered yet, please add one before creating a task.")
    else:
        title = input('Enter task\'s title:\n')
        description = input('Enter task\'s description:\n')
        priority = select_priority()

        #Select assignee from the list (print all the list and assign a number to it)
        name = select_assignee(assignees)
            
        task = Task(title, description, priority, name)
        tasks.append(task)
        update_task(tasks)

    return tasks

#Task list transformed into a dictionary to have whole current list overwritten on the file
def update_task(tasks):
    brd = {
        "tasks" : []
    }
    for task in tasks:
        task_dict = utils.convert_board_to_dict(task)
        brd['tasks'].append(task_dict)
    file_handler.save_board(brd)

#Fetch tasks by state
def fetch_tasks_by_state(tasks,state):

    temp_task_list = []

    for task in tasks:
        if(task.get_state() == state):
            temp_task_list.append(task)

    return temp_task_list

#Fetch tasks by assignee
def fetch_tasks_by_assignee(tasks,name):

    temp_task_list = []

    for task in tasks:
        if(task.get_assignee() == name):
            temp_task_list.append(task)

    return temp_task_list

#Printing tasks by state
def print_tasks_by_state(tasks):

    if tasks:
        state = select_state()
        tasks_by_state = fetch_tasks_by_state(tasks, state)

        if tasks_by_state:
            print("----------------------------------")
            for task in tasks_by_state:
                print(task.get_task_info())
                print("----------------------------------")
        else:
            print("We're sorry, no current tasks exist on selected state...")
    else:
        print("We're sorry, Board is currently empty...")

#Printing tasks by state
def print_tasks_by_assignee(tasks, assignees):

    if not assignees:
        print("No assignees are registered yet...")
    elif not tasks:
        print("We're sorry, Board is currently empty...")
    else:
        name = select_assignee(assignees)

        tasks_by_assignee = fetch_tasks_by_assignee(tasks,name)

        if tasks_by_assignee:
            print("----------------------------------")
            for task in tasks_by_assignee:
                print(task.get_task_info())
                print("----------------------------------")
        else:
            print("We're sorry, no current tasks exist assigned to selected user...")
    

#Printing entire board
def print_board(tasks):

    if tasks:
        temp_list = []
        
        states_list = [states.BACKLOG,states.TODO,states.INPROGRESS,states.TODO]

        for state in states_list:
            temp_list = fetch_tasks_by_state(tasks,state)

            if temp_list:
                print(f"**********  {state} **********")

                for task in temp_list:
                    print(task.get_task_info())
                    print("----------------------------------")

    else:
        print("We're sorry, Board is currently empty...")

#"Main" method
def start(tasks, assignees):

    menu_option = 0

    while menu_option != 7:

        menu_option = main_menu()

        if menu_option == 1:
            #Create assignee
            assignees = create_assignee(assignees)
            menu_option = 0

        elif menu_option == 2:
            #Create task (if there are assignees)
            tasks = create_task(tasks, assignees)
            menu_option = 0

        elif menu_option == 3:
            #Transition Task
            transition_task(tasks)

        elif menu_option == 4:
            #Show Board
            print_board(tasks)

        elif menu_option == 5:
            #Show Tasks by state
            print_tasks_by_state(tasks)

        elif menu_option == 6:
            #Show Tasks by Assignee
            print_tasks_by_assignee(tasks,assignees)

        elif menu_option == 7:
            print("Goodbye!")
        else:
            print("Incorrect choice, please select a valid option:")
            menu_option = 0


# ************************* Main ******************************************+

start(my_tasks,my_assignees)
