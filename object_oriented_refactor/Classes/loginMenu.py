import os
from .usermenu import Usermenu
from .user import User
from .admin_menu import Admin_menu

class LoginMenu():

    # def __init__(self, data, number=None, user_menu=None, admin_menu=None):
    #     self.user_list = data.user_list
    #     self.admin_list = data.admin_list
    #     self.phone_number = number
    #     self.user_menu = user_menu
    #     self.admin_menu = admin_menu

    #printing the menu options  
    def get_selection(self, data_object):

        selection = "0"

        while(selection != "4"):
            print("Menu Options - Login or Register")
            print("1. Login - customer")
            print("2. Login - admin")
            print("3. Register")
            print("4. Exit Application")

            selection = input("Please choose option (1-4): ")
            if(selection == "1"):
                print("You have selected 'Login - customer'")
                self.login(data_object.user_list)
            elif(selection == "2"):
                print("You have selected 'Login - admin'")
                self.login_admin(data_object)
            elif(selection == "3"):
                print("You have selected 'Register'")
                self.new_user_registration(data_object.user_list)
            elif(selection != "1" and selection !="2" and selection != "3" and selection != "4"):
                print(f"Selection is invalid '{selection}', select return and try again")

        print("Application Closed") 

    def login(self, user_list):
        print("CUSTOMER LOGIN")
        print("==============")
        username = input("Please enter phone number: ")
        password = input("Please enter password: ") 

        self.validate_phone_number(username)
        #user = User(phone_number, first_name, last_name, email_address, password, plan, current_balance, topup_history=[])

        found_user = False

        for user in user_list:
            if(user.phone_number == username):

                found_user = True
                if(user.password == password):
                    print("Login Successful")
                    input("Press return to continue...")
                    user_menu = Usermenu()
                    user_menu.display_usermenu(user)
                else:
                    print("Password invalid.")
                    input("Press return to continue...")

                break

        if(found_user == False):
            print("Username not found. Please try again.")
            input("Press return to continue...")


    def login_admin(self, data_object):
        print("ADMIN LOGIN")
        print("===========")
        employee_number = input("Please enter employee number: ")
        password = input("Please enter password: ") 

        found_admin_user = False

        for admin_user in data_object.admin_list:
            if(admin_user.employee_number == employee_number):

                found_admin_user = True
                if(admin_user.password == password):
                    print("Login Successful")
                    input("Press return to continue...")
                    admin_menu = Admin_menu()
                    admin_menu.show_admin_menu(data_object)
                else:
                    print("Password invalid.")
                    input("Press return to continue...")

                break

        if(found_admin_user == False):
            print("Employee number not found. Please try again.")
            input("Press return to continue...")            


    def validate_phone_number(self,user_phone_number):
         isnumeric = user_phone_number.isnumeric()
         islengthcorrect=len(user_phone_number)
         status = isnumeric and (islengthcorrect==10)
         if status==False:
          print("Sorry, invalid phone number. Please enter correct number in digital format (10 digits) ")
         return status
    
    def user_registration_menu(self):

        #clearScreen()
        print("Welcome!Please follow instructions and provide details for your registration\n")
        print("New user registration:")
        print("1. Enter details")
        print("2. Exit\n")
        return input("Please choose an option (1-2): ")

    def user_registration_plan_menu(self):
        print("Please choose your mobile plan or press 4 to exit:")
        print("1. Pay As You Go (Can top up by any amount, no expiration)")
        print("2. Top-Up-20 Plan (Minimum top-up is 20, credit expires in 1 month")
        print("3. Premium Plan (Minimum top-up is 30, receive 5 euro free credit, expires in 1 month")   
        print("4. Exit\n")       
        return input("Please choose an option (1-4): ")

    def new_user_registration(self, user_list):
         # 1. Pay As You Go (Can top up by any amount, no expiration)
    # 2. Top-Up-20 Plan (Minimum top-up is 20, credit expires in 1 month)
    # 3. Premium Plan (Minimum top-up is 30, receive 5 euro free credit, expires in 1 month) 
    # "Plan ' ' chosen..Thank You"

     selection = "0"
     planselection="0"
     PhoneNumber=""
     FirstName = ""
     LastName =""
     Email=""
     Password=""

     user = None
     while(selection != "2"):
         selection = self.user_registration_menu()
        #clearScreen()
    
         if(selection == "1"):
            PhoneNumber = input("Please enter your Phone Number!\n")
            if (self.validate_phone_number(PhoneNumber)==False):
                break
            #else:
                #if (CheckPhoneNumber(PhoneNumber)==True):
                    #break
            print("Please enter your First name!\n")
            FirstName = input()
            print("Please enter your Last name!\n")
            LastName = input()
            print("Please enter your Email!\n")
            Email = input()
            print("Please enter your Password!\n")
            Password = input()
            planselection = self.user_registration_plan_menu()
            #clearScreen()
            # if ((planselection=="1") or(planselection=="2")or (planselection=="3")):
            if planselection in("1","2","3"):
                user = User(PhoneNumber, FirstName, LastName, Email, Password, planselection, 0.0)
                user_list.append(user)
                print("Thank you!You are registered, now you can log in using your phone number and password")
            elif(planselection!= "4"):
                print("Please return to menu and select a digit from 1 to 4")
                input("Return to continue...")
         elif(selection != "2"):
            print("Please return to menu and select a digit from 1 to 2")
            input("Return to continue...")
