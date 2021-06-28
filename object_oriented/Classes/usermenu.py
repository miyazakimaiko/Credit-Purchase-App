from .user import User
import os

class Usermenu:

    def __init__(self,data):
        #self.data=data
        self.user_list=data
        #self.usermenu=user_menu
        

    def clear_screen(self):
        os.system('cls')

    def display_usermenu(self):  # Displaying  user menu
        self.clear_screen()
        current_usernumber="0862173794"
        topup_amount=0
        choice="0"
        option=""
        print("")
        print("     Customer Login Menu")
        print("      *****************")
        print("1.  View Balance")
        print("2.  Top-up")
        print("3.  Change plan")
        print("4.  View Statement")
        print("5.  Exit")
        choice=input("Please enter your option[1/2/3/4/5] : ")

        if (choice=="1"):
            self.clear_screen()
            print("  Customer Balance   ")
            print(" ")
            #current_usernumber="0862173794"
            for user in self.user_list:
                if(current_usernumber==user.phone_number):
                    print("Phone Number      :   ",user.phone_number)
                    print("First  Name       :   ",user.first_name)
                    print("last  Name        :   ",user.last_name)
                    print("Account balance   :   ",user.current_balance)

            input("Enter return to continue")
            self.clear_screen()
            self.display_usermenu()
        elif(choice=="2"):
            self.clear_screen()
            print("    Credit top up")
            print("    *************")
            print("1. £5")
            print("2. £10")
            print("3. £15")
            print("4. £20")
            print("5. £25")
            print("6. Exit") #will close the app
            choice1=input("Enter your option :   ")
            if (choice1 =="1"):
                    topup_amount=5.00
                    self.credit_top_up(current_usernumber,topup_amount)
                    print("")
                    input("please enter return to continue.....")
                    self.clear_screen()
                    self.display_usermenu()
            elif choice1 == "2":
                        topup_amount=10
                        self.credit_top_up(current_usernumber,topup_amount)
                        print("You have topped up with £10")
                        input("please enter return to continue")
                        self.clear_screen()
                        self.display_usermenu()
                    
            elif choice1 == "3":
                        topup_amount=15
                        self.credit_top_up(current_usernumber,topup_amount)
                        print("You have topped up with £15")
                        input("please enter return to continue")
                        self.clear_screen()
                        self.display_usermenu()
                        
            elif choice1 =="4":
                        topup_amount=20
                        self.credit_top_up(current_usernumber,topup_amount)
                        print("You have topped up with £20")
                        input("please enter return to continue")
                        self.clear_screen()
                        self.display_usermenu()
                        
            elif choice1 == "5":
                        topup_amount=25
                        self.credit_top_up(current_usernumber,topup_amount)
                        print("You have topped up with £25")
                        input("please enter return to continue")
                        self.clear_screen()
                        self.display_usermenu
                    
            elif choice1 == "6":
                        self.clear_screen()
                        self.display_usermenu()
                    
            else:
                    print("Invalid Entry")
                    self.display_usermenu()
                    print("Enter return to continue")
                    self.clear_screen()
                    self.display_usermenu()
        elif(choice=="3"):
            ######################## plan change
            self.clear_screen()
            choice2=""
            new_plan=0
            print("    Change your plan")
            print("    ****************")
            print("1. Prepay")
            print("2. Bill pay")
            print("3. Sim-only")
            print("4. Exit")
            choice2=input("Enter your choice  :  ")
            if choice2 =="1":
                new_plan=1
                #self.change_plan(self,current_usernumber,new_plan)
                print("You have switched over to pre pay")
                input("Enter return to continue...")
                self.clear_screen()
                self.display_usermenu()         
            elif choice2 =="2":
                new_plan=2
                print("You have switched over to bill pay")
                input("Enter return to continue....")
                self.clear_screen()
                self.display_usermenu()
            elif choice2 =="3":
                new_plan=3
                print("You have switched over to a sim-only plan")
                input("Enter return to continue....")
                self.clear_screen()
                self.display_usermenu()
            elif choice2 =="4":
                self.clear_screen()
                self.display_usermenu()
            else:
                print("Invalid Entry ...")
                self.change_plan()
                ##########################
                print("Enter return to continue")
                self.clear_screen()
                self.display_usermenu()
        elif(choice=="4"):
            #self.view_statement()
            print("Enter return to continue")
            self.clear_screen()
            self.display_usermenu()
        elif(choice=="5"):
            exit()
        else:
            option=input("Invalid Entry, Do you want to try again? [Y/N] : ")
            option=option.upper()
            if (option=="Y"):
                print("")
                self.display_usermenu()
            else:
                exit()


    

        
    ##function for credit top up########
    def credit_top_up(self,current_usernumber,topup_amount):
        for user in self.user_list:
                if(current_usernumber==user.phone_number):
                    #balance=user.current_balance
                    #balance=balance+topup_amount
                    #user.current_balance=balance
                    user.add_balance(topup_amount)
        print("")
        print(" Your topup amount is  : ", topup_amount)
        print(" Youraccount balance is ", user.current_balance)
                    

        
        


    ####function for changing plan####
    
    def change_plan(self,current_usernumber,new_plan):
        for user in self.data.user_list:
                if(current_usernumber==user.phone_number):
                    user.plan=new_plan

                     
##############################################################