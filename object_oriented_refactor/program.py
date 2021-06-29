
from Classes.data import Data
from Classes.usermenu import Usermenu
from Classes.user import User
from Classes.utils import Utils 
from Classes.loginMenu import LoginMenu 

Utils.clear_screen()

data_object = Data()

########   Emma   Loginmenu   #####

login_menu = LoginMenu()
login_menu.get_selection(data_object)

##############################

#########   Silpa    User menu  ########
# user_menu=Usermenu(data_object.user_list)
# user_menu.display_usermenu()

#########################################

######### Bruna    Admin menu  ############









