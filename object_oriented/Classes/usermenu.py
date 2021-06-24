import os
class Usermenu:
    def clear_screen(self):
        os.system('cls')
    def display_usermenu(self):  # Displaying  user menu
        self.clear_screen()
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
            self.view_balance()
            input("Enter return to continue")
            self.clear_screen()
            self.display_usermenu()
        elif(choice=="2"):
            self.credit_top_up()
            print("Enter return to continue")
            self.clear_screen()
            self.display_usermenu()
        elif(choice=="3"):
            self.change_plan()
            print("Enter return to continue")
            self.clear_screen()
            self.display_usermenu()
        elif(choice=="4"):
            self.view_statement()
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


    ######## function for displaying balance###
    def view_balance(self):
        print("")

        
    ##function for credit top up########
    def credit_top_up(self):
        choice1=""
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
                print("You have topped up with £5")
                input("please enter return to continue")
                self.clear_screen()
                self.display_usermenu()
        elif choice1 == "2":
                    print("You have topped up with £10")
                    input("please enter return to continue")
                    self.clear_screen()
                    self.display_usermenu()
                   
        elif choice1 == "3":
                    print("You have topped up with £15")
                    input("please enter return to continue")
                    self.clear_screen()
                    self.display_usermenu()
                    
        elif choice1 =="4":
                    print("You have topped up with £20")
                    input("please enter return to continue")
                    self.clear_screen()
                    self.display_usermenu()
                    
        elif choice1 == "5":
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

   



    ####function for changing plan####
    def change_plan(self):
        self.clear_screen()
        choice2=""
        print("    Change your plan")
        print("    ****************")
        print("1. Prepay")
        print("2. Bill pay")
        print("3. Sim-only")
        print("4. Exit")
        choice2=input("Enter your choice  :  ")
        if choice2 =="1":
            print("You have switched over to pre pay")
            input("Enter return to continue...")
            self.clear_screen()
            self.display_usermenu()         
        elif choice2 =="2":
            print("You have switched over to bill pay")
            input("Enter return to continue....")
            self.clear_screen()
            self.display_usermenu()
        elif choice2 =="3":
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


    #####function for  view mini statement######

    def view_statement(self):
        self.clear_screen()
        print("  Statement")
        print("  ********* ")
        input("Enter return to continue.....")
        self.clear_screen()
        self.display_usermenu()




       ##################################################

usermenu=Usermenu()
usermenu.display_usermenu()
    
            

                     

