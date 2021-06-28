
from Classes.data import Data
from Classes.usermenu import Usermenu
from Classes.user import User

#from Classes.user import User


import os

def clearscreen():
    os.system('cls')

clearscreen()   

data_object = Data()
data_object.add_users()
#data_object.add_admins()


########   Emma   Loginmenu   #####

#login_menu = LoginMenu(data_object)
#login_menu.get_selection()

##############################

#########   Silpa    User menu  ########
user_menu=Usermenu(data_object.user_list)
user_menu.display_usermenu()

#########################################

######### Bruna    Admin menu  ############









