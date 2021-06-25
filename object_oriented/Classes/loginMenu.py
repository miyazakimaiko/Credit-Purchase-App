import os
from user import User
from admin import Admin


class LoginMenu():
    def clearscreen(self):
        os.system('cls')        
    #printing the menu options  
    def get_selection(self):
         print("Menu Options - Login or Register")
         print("1. Login - customer")
         print("2. Login - admin")
         print("3. Register")
         print("4. Exit Application")

       
         while(selection != "4"):
             selection = input("Please choose option (1-4): ")
             if(selection == "1"):
                 print("You have selected 'Login - customer'")
                 #self.login()
             elif(selection == "2"):
                print("You have selected 'Login - admin'")
                #self.login_admin
             elif(selection == "3"):
                 print("You have selected 'Register'")
                 #self.register_user()
             elif(selection != "1" and selection !="2" and selection != "3" and selection != "4"):
                 print(f"Selection is invalid '{selection}', select return and try again")

         print("Application Closed") 

    def login(self, user):
        print("CUSTOMER LOGIN")
        print("==============")
        username = input("Please enter phone number: ")
        password = input("Please enter password: ") 

        self.validate_phone_number(username)
        #user = User(phone_number, first_name, last_name, email_address, password, plan, current_balance, topup_history=[])

        user_list = []

        user_phone_number = ""
        user_password = ""
        found_user = None

        for user in user_list:
            if(user.phone_number == username):
                user_phone_number = user.phone_number
                found_user = user
                break
        if(found_user != None):
            user_password = found_user.user.password
        if(username == user.phone_number and user.password == user_password):
            print("Login Successful")
            #userlogin class
        elif(username != user_phone_number and user.password != user_password):
            print("Username and password invalid ")
        elif(username == user_phone_number and user.password != user_password):
            print("Password Incorrect")
        elif(username != user_phone_number and user.password == user_password):
            print("Username Correct")
    
    #def login_admin(self, admin):

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

    def new_user_registration(self, user):
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
     Plan=""

     userdetails = []
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
                user = {"PhoneNumber":PhoneNumber, "FirstName": FirstName, "LastName": LastName, "Email": Email, "Password": Password,
                "Plan": planselection}
                print("Thank you!You are registered, now you can log in using your phone number and password")
            elif(planselection!= "4"):
                print("Please return to menu and select a digit from 1 to 4")
                input("Return to continue...")
         elif(selection != "2"):
            print("Please return to menu and select a digit from 1 to 2")
            input("Return to continue...")




# loginMenu = LoginMenu()
# loginMenu.loginOrRegisterMenu()    
# 
# 
#loginMenu_object = LoginMenu()
#loginMenu_object.get_selection()
    

    

        
         

 