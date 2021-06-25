import os

class Admin_menu:

    def show_admin_menu(self): #Class diagram - ok
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

        selection = self.get_selection() ####?????

        if selection == 1:
            print("\n")
            print("=================")
            print("SELECTED: 1. View a customer report")

            self.show_user_selection_menu()
            self.show_admin_menu()

        elif selection == 2:
            print("\n")
            print("=================")
            print("SELECTED: 2. View per plan report")

            #show_per_plan_report_plan_selection_menu()
            self.show_admin_menu()

        elif selection == 3:
            print("\n")
            print("=================")
            print("SELECTED: 3. View general report")

            #show_general_report_date_range_selection_menu()
            self.show_admin_menu()

        elif selection == 4:
            print("\n")
            print("=================")
            print("SELECTED: 4. View all customers")

            # get_all_customers()

        elif selection == 5:
            print("\n")
            print("exit")
            exit()
            # loginOrRegisterMenu()

    def show_user_selection_menu(self):
        phonenumber = input("Please enter phone number :")

        print("run get_cusomter_report_by_phone_number({0})".format(phonenumber))


    def get_selection(self): #Class diagram -ok
        number = input("Please choose an option (1-5):")

        try:
            number = int(number)
        except:
            # Keep asking user a number if the input is invalid
            number = self.get_selection()

        if number > 5 or number <= 0:
           number = self.get_selection() 

        return number


    
    
admin_menu=Admin_menu()
admin_menu.show_admin_menu()
#admin_menu.get_selection()
