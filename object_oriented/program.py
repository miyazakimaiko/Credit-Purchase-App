from Classes.loginMenu import LoginMenu
from Classes.data import Data
import os

def clearscreen():
    os.system('cls')

clearscreen()   

data_object = Data()
data_object.add_users()
data_object.add_admins()

login_menu = LoginMenu(data_object)
login_menu.get_selection()
