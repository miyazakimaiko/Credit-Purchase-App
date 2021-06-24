import os
from Classes.user import User


class LoginMenu():
    def clearscreen(self):
        os.system('cls')        
    #printing the menu options  
    def loginOrRegisterMenu(self):
         print("Menu Options - Login or Register")
         print("1. Login - customer")
         print("2. Login - admin")
         print("3. Register")
         print("4. Exit Application")

         selection = "0"

         while(selection != "4"):
             selection = input("Please choose option (1-4): ")
             if(selection == "1"):
                 print("You have selected 'Login - customer'")
                 #login()
             elif(selection == "2"):
                print("You have selected 'Login - admin'")
                #login_admin
             elif(selection == "3"):
                 print("You have selected 'Register'")
                 #register_user()
             elif(selection != "1" and selection !="2" and selection != "3" and selection != "4"):
                 print(f"Selection is invalid '{selection}', select return and try again")

         print("Application Closed")    

loginMenu = LoginMenu()
loginMenu.loginOrRegisterMenu()     
    

    

        
         

 