from .utils import Utils 
#from user import User ###?????????
#from data import Data

#from data import admin_list ### how to do it?

#import datetime
#import calendar

class Admin_menu:

    def __init__(self, data):
        self.admin_list = data.admin_list
        
        
     
    def show_admin_menu(self): 
        print("=================")
        print("\n")
        print("ADMIN MAIN MENU")
        print("\n")
        print("Selection:")
        print("1. View a customer report <- x")
        print("2. View per plan report <- ready to test")
        print("3. View general report <- ready to test")
        print("4. View all customers <- x")
        print("5. Exit")
        print("\n")

        selection = self.get_selection() ##selection from admin_menu

        if selection == 1:
            print("\n")
            print("=================")
            print("SELECTED: 1. View a customer report")
            Utils.clear_screen()
            self.show_user_selection_menu()
            self.show_admin_menu()

        elif selection == 2: ###### doing it
            print("\n")
            print("=================")
            print("SELECTED: 2. View per plan report")
            Utils.clear_screen()
            self.show_per_plan_report_plan_selection_menu()
            self.show_admin_menu()

        elif selection == 3:
            print("\n")
            print("=================")
            print("SELECTED: 3. View general report")
            Utils.clear_screen()
            #show_general_report_date_range_selection_menu()
            self.show_admin_menu()

        elif selection == 4:
            print("\n")
            print("=================")
            print("SELECTED: 4. View all customers")
            Utils.clear_screen()
            self.show_admin_menu()
            #get_all_customers()

        elif selection == 5:
            print("\n")
            print("exit")
            exit()
            # loginOrRegisterMenu()

    def get_selection(self): #Class diagram -ok
        number = input("Please choose an option (1-5): ")

        try:
            number = int(number)
        except:
            # Keep asking user a number if the input is invalid
            number = self.get_selection()

        if number > 5 or number <= 0:
            number = self.get_selection() 

        return number

####function to have a report - input phone number
    def show_user_selection_menu(self): ### user need to enter phone to have a report
        phonenumber = input("Please enter phone number: ")
        print("run get_customer_report_by_phone_number({0})".format(phonenumber))
        
        ####function for selection 1. View a customer report 
        ###added28/05#######################################  it is not working
        #for phone_number in self.user_list:
            #if phone_number == self.show_user_selection_menu(phonenumber):
                #print(self.first_name, self.last.name, self.phone_number, self.current_balance )
 ########################TODO###################################

    

    ####function for selection 2. View per plan report 
    def show_per_plan_report_plan_selection_menu(self):
        print("Selection:")
        print("1. Pay as You Go <- ready to test")
        print("2. Top-Up-20 Plan <- ready to test")
        print("3. Premium Plan <- ready to test")
        print("4. Exit\n")


        def get_plan(self):
            number = input("Please choose a plan(1-3) or Exit(4):")

            try:
                number = int(number)
            except:
                # Keep asking user a number if the input is invalid
                number = self.get_plan()

            if number > 4 or number <= 0:
                number = self.get_plan() 

            return number


        plan = get_plan()

        if plan in range(1, 4): #range will be 1, 2 and 3
            self.show_per_plan_report_date_range_selection_menu(plan)

        elif(plan == 4):
            exit()


    ####function for selection 3. View general report 

    ####function for selection 4. View all customers
   


    
    
#admin_menu=Admin_menu()
#admin_menu.show_admin_menu()
#admin_menu.get_selection()
#admin_menu.show_user_selection_menu()
