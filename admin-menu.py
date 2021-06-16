import datetime

def admin_main_menu():
    print("=================")
    print("Selection:")
    print("1. View a customer report")
    print("2. View per plan report")
    print("3. View general report")
    print("4. View all customers")
    print("5. Exit\n")

    def get_selection():
        selection = input("Please choose an option (1-5):")

        try:
            selection = int(selection)
        except:
            # Keep asking user a number if the input is invalid
            get_selection()

        if selection > 5 or selection <= 0:
           get_selection() 
        else:
            return selection

    selection = get_selection()

    if(selection == 1):
        user_selection_menu()
    elif(selection == 2):
        plan_selection_menu()
    elif(selection == 3):
        print("selection 3")
        # get_general_report()
    elif(selection == 4):
        # get_all_customers()
        print("selection 4")


def user_selection_menu():
    phonenumber = input("Please enter phone number :")
    print("run get_cusomter_report_by_phone_number({0})".format(phonenumber))


def plan_selection_menu():
    print("=================")
    print("Selection:")
    print("1. Pay as You Go")
    print("2. Top-Up-20 Plan")
    print("3. Premium Plan")
    print("4. Exit\n")

    def get_plan():
        selection = input("Please choose a plan(1-3) or Exit(4):")

        try:
            selection = int(selection)
        except:
            # Keep asking user a number if the input is invalid
            get_plan()

        if selection > 4 or selection <= 0:
           get_plan() 
        else:
            return selection

    plan = get_plan()

    if(plan in range(1, 3)):
        date_range_selection_menu()
    elif(plan == 4):
        exit()


def date_range_selection_menu():
    print("=================")
    print("Selection:")
    print("1. Last Month")
    print("2. Custom")
    print("3. Exit\n")

    def get_selection():
        selection = input("Please choose a date range(1 or 2) or Exit(3):")

        try:
            selection = int(selection)
        except:
            # Keep asking user a number if the input is invalid
            get_selection()

        if selection > 4 or selection <= 0:
            get_selection() 
        else:
            return selection

    selection = get_selection()

    if selection == 1:
        today = datetime.date.today()
        start = today.replace(day=30)
        end = today.replace(day=1)

        print("run get_all_topups_by_date_range({0}, {1})".format(start, end))

    elif selection == 2:
        custom_date_range_menu()

    elif selection == 4:
        exit()


def custom_date_range_menu():

    def get_start_date():
        start = input("Please enter START DATE in dd/mm/yyyy format :")

        try:
            start = datetime.datetime.strptime(start, "%d/%m/%Y")
        except:
            # Keep asking user a number if the input is invalid
            get_start_date()


    def get_end_date():
        end = input("Please enter END DATE in dd/mm/yyyy format :")

        try:
            end = datetime.datetime.strptime(end, "%d/%m/%Y")
        except:
            # Keep asking user a number if the input is invalid
            get_start_date()

    start = get_start_date()
    end = get_end_date()

    print("run get_all_topups_by_date_range({0}, {1})".format(start, end))




# Test run
admin_main_menu()