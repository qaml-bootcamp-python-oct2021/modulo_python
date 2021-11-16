class Assignee:
    def __init__(self, name='',email='') -> None:
        self.__name = name
        self.__email = email

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self,email):
        self.__email = email

    def get_email(self):
        return self.__email

    def get_assignee_info(self):
        return f"{self.__name} (e-mail: {self.__email})"