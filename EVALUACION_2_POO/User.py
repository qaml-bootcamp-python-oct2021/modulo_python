class User:
    def __init__(self, name ='', email ='') -> None:
        self.__name = name
        self.__email = email


    def get_email(self):
        return self.__email
    def get_name(self):
        return self.__name
    def get_info(self):
        return f'Name: {self.__name} - Email: {self.__email} '