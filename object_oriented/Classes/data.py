from .user import User
from .admin import Admin
from .loginMenu import LoginMenu


class Data:

    def __init__(self):
        self.user_list = []
        self.admin_list = []


    def add_users(self):
        self.user_list.append(User("0871112345", "Emma", "Brown", "emma@brown.ie", "qwerty", 3, 100.00))
        self.user_list.append(User("0862173794", "Silpa", "Pravin", "silpa@brown.ie", "1234", 1, 200.00))
        self.user_list.append(User("0899409520", "Bruna", "Weber", "bruna@brown.ie", "5678", 2, 300.00))
        self.user_list.append(User("0834837641", "Maiko", "Miyazaki", "maiko@brown.ie", "1987", 3, 100.00))
        
    def add_admins(self):
        self.admin_list.append(Admin("0000", "manager0"))
        self.admin_list.append(Admin("1111", "manager1"))
        self.admin_list.append(Admin("2222", "manager2"))
        self.admin_list.append(Admin("3333", "manager3"))

