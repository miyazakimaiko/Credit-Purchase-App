import datetime
from admin_menu_functions import get_all_topups_by_date_range

def admin_main_menu():
    print("=================")
    print("Selection:")
    print("1. View a customer report")
    print("2. View per plan report")
    print("3. View general report")
    print("4. View all customers")
    print("5. Exit\n")

    def get_selection():
        number = input("Please choose an option (1-5):")

        try:
            number = int(number)
        except:
            # Keep asking user a number if the input is invalid
            number = get_selection()

        if number > 5 or number <= 0:
           number = get_selection() 

        return number

    selection = get_selection()

    if selection == 1:
        print("SELECTED: 1. View a customer report")
        user_selection_menu()
    elif selection == 2:
        print("SELECTED: 2. View per plan report")
        per_plan_report_plan_selection_menu()
    elif selection == 3:
        print("SELECTED: 3. View general report")
        general_report_date_range_selection_menu()
    elif selection == 4:
        # get_all_customers()
        print("SELECTED: 4. View all customers")


def user_selection_menu():
    phonenumber = input("Please enter phone number :")
    print("run get_cusomter_report_by_phone_number({0})".format(phonenumber))


def per_plan_report_plan_selection_menu():
    print("=================")
    print("Selection:")
    print("1. Pay as You Go")
    print("2. Top-Up-20 Plan")
    print("3. Premium Plan")
    print("4. Exit\n")

    def get_plan():
        number = input("Please choose a plan(1-3) or Exit(4):")

        try:
            number = int(number)
        except:
            # Keep asking user a number if the input is invalid
            number = get_plan()

        if number > 4 or number <= 0:
           number = get_plan() 

        return number

    plan = get_plan()

    # Reminder.. 4 doesn't include in range when range(1, 4)
    if plan in range(1, 4): 
        per_plan_report_date_range_selection_menu()
    elif(plan == 4):
        exit()


def per_plan_report_date_range_selection_menu():
    print("=================")
    print("Selection:")
    print("1. Last Month")
    print("2. Custom")
    print("3. Exit\n")

    def get_selection():
        number = input("Please choose a date range(1 or 2) or Exit(3):")

        try:
            number = int(number)
        except:
            # Keep asking user a number if the input is invalid
            number = get_selection()

        if number > 3 or number <= 0:
            number = get_selection() 

        return number

    selection = get_selection()

    if selection == 1:
        today = datetime.datetime.now()
        start = today.replace(day=30)
        end = today.replace(day=1)
        get_all_topups_by_date_range(start, end)

    elif selection == 2:
        per_plan_report_custom_date_range_menu()

    elif selection == 3:
        exit()


def get_start_date():
    date = input("Please enter START DATE in dd/mm/yyyy format :")

    try:
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
    except:
        # Keep asking user a date if the input is invalid date format
        get_start_date()
    
    return date


def get_end_date():
    date = input("Please enter END DATE in dd/mm/yyyy format :")

    try:
        date = datetime.datetime.strptime(date, "%d/%m/%Y")
    except:
        # Keep asking user a date if the input is invalid date format
        get_end_date()
    
    return date


def per_plan_report_custom_date_range_menu():

    start = get_start_date()
    end = get_end_date()

    print("run get_all_topups_by_date_range({0}, {1})".format(start, end))


def general_report_date_range_selection_menu():
    print("=================")
    print("Selection:")
    print("1. Last Month")
    print("2. Custom")
    print("3. Exit\n")

    def get_selection():
        number = input("Please choose a date range(1 or 2) or Exit(3):")

        try:
            number = int(number)
        except:
            # Keep asking user a number if the input is invalid
            number = get_selection()

        if number > 3 or number <= 0:
            number = get_selection() 

        return number

    selection = get_selection()

    if selection == 1:
        today = datetime.date.today()
        start = today.replace(day=30)
        end = today.replace(day=1)

        print("run get_all_topups_by_date_range({0}, {1})".format(start, end))

    elif selection == 2:
        general_report_custom_date_range_menu()

    elif selection == 3:
        exit()


def general_report_custom_date_range_menu():
 
    start = get_start_date()
    end = get_end_date()

    print("run get_general_report_by_date_range({0}, {1})".format(start, end))


# Test run
admin_main_menu()