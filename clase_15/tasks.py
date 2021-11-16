import states

class Task:
    def __init__(self, title='',description='',priority='',assignee='') -> None:
        self.__title = title
        self.__description = description
        self.__priority = priority
        self.__state = states.BACKLOG
        self.__assignee = assignee

    def set_title(self,title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_description(self,description):
        self.__description = description

    def get_description(self):
        return self.__description

    def set_priority(self,priority):
        self.__priority = priority

    def get_priority(self):
        return self.__priority

    def set_state(self,state):
        self.__state = state

    def get_state(self):
        return self.__state

    def set_assignee(self,assignee):
        self.__assignee = assignee

    def get_assignee(self):
        return self.__assignee

    def get_task_info(self):
        return f"""-- Title: {self.__title}\n-- Description: {self.__description}\n-- Priority: {self.__priority}\n-- Assignee: {self.__assignee}\n-- State: {self.__state}"""
