from datetime import datetime
from .user import User
from .admin import Admin
from .topup import Topup
#from .loginMenu import LoginMenu


class Data:

    def __init__(self):
        self.user_list = []
        self.admin_list = []

        self.add_users()
        self.add_admins()


    def add_users(self):
        topup_history = []
        topup_history.append(Topup(20.0, 1, datetime.strptime("02/05/2021", "%d/%m/%Y")))
        topup_history.append(Topup(30.0, 1, datetime.strptime("04/05/2021", "%d/%m/%Y")))
        topup_history.append(Topup(20.0, 1, datetime.strptime("07/05/2021", "%d/%m/%Y")))

        user = User("0871112345", "Emma", "Brown", "emma@brown.ie", "qwerty", 3, 100.00)
        user.topup_history = topup_history
        self.user_list.append(user)

        self.user_list.append(User("0862173794", "Silpa", "Pravin", "silpa@brown.ie", "1234", 1, 200.00))
        self.user_list.append(User("0899409520", "Bruna", "Weber", "bruna@brown.ie", "5678", 2, 300.00))
        self.user_list.append(User("0834837641", "Maiko", "Miyazaki", "maiko@brown.ie", "1987", 3, 100.00))
        
    def add_admins(self):
        self.admin_list.append(Admin("9876", "manager0"))
        self.admin_list.append(Admin("9877", "manager1"))
        self.admin_list.append(Admin("9878", "manager2"))
        self.admin_list.append(Admin("9879", "manager3"))

