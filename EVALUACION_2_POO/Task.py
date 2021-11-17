import States
class Task:
    def __init__(self, description ='', title ='', priority ='', asigned_user ='') -> None:
        self.__title = title
        self.__description = description
        self.__priority = priority
        self.__asigned_user = asigned_user
        self.__state = States.BACKLOG

    def set_state(self, state):
        self.__state = state
    def get_state(self):
        return self.__state
    def get_title(self):
        return self.__title
    def get_description(self):
        return self.__description
    def get_priority(self):
        return self.__priority
    def get_asigned_user(self):
        return self.__asigned_user
    def get_info(self):
        return f'Title: {self.__title} - Description: {self.__description} - Priority: {self.__priority} - User Asigned: {self.__asigned_user} - State: {self.__state}'