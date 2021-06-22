import datetime
import calendar
from admin_menu_functions.general_report import *
from admin_menu_functions.per_plan_report import *

def show_admin_main_menu():
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
        print("\n")
        print("=================")
        print("SELECTED: 1. View a customer report")

        show_user_selection_menu()
        show_admin_main_menu()

    elif selection == 2:
        print("\n")
        print("=================")
        print("SELECTED: 2. View per plan report")

        show_per_plan_report_plan_selection_menu()
        show_admin_main_menu()

    elif selection == 3:
        print("\n")
        print("=================")
        print("SELECTED: 3. View general report")

        show_general_report_date_range_selection_menu()
        show_admin_main_menu()

    elif selection == 4:
        print("\n")
        print("=================")
        print("SELECTED: 4. View all customers")

        # get_all_customers()

    elif selection == 5:
        print("\n")
        print("exit")

        # loginOrRegisterMenu()


def show_user_selection_menu():
    phonenumber = input("Please enter phone number :")

    print("run get_cusomter_report_by_phone_number({0})".format(phonenumber))


def show_per_plan_report_plan_selection_menu():
    print("Selection:")
    print("1. Pay as You Go <- ready to test")
    print("2. Top-Up-20 Plan <- ready to test")
    print("3. Premium Plan <- ready to test")
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
        show_per_plan_report_date_range_selection_menu(plan)

    elif(plan == 4):
        exit()


def show_per_plan_report_date_range_selection_menu(plan_number):
    print("Selection:")
    print("1. Last Month <- ready to test")
    print("2. Custom <- ready to test")
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
        today = datetime.now()
        prev_month = today.month - 1
        prev_monthrange = calendar.monthrange(today.year, prev_month)
        start = datetime(today.year, prev_month, 1)
        end = datetime(today.year, prev_month, prev_monthrange[1])

        get_selected_plans_topups_by_date_range(plan_number, start, end)

    elif selection == 2:
        show_per_plan_report_custom_date_range_menu(2)

    elif selection == 3:
        print("Exit")


def get_start_date():
    date = input("Please enter START DATE in dd/mm/yyyy format :")

    try:
        date = datetime.strptime(date, "%d/%m/%Y")
    except:
        # Keep asking user a date if the input is invalid date format
        date = get_start_date()
    
    return date


def get_end_date():
    date = input("Please enter END DATE in dd/mm/yyyy format :")

    try:
        date = datetime.strptime(date, "%d/%m/%Y")
    except:
        # Keep asking user a date if the input is invalid date format
        date = get_end_date()
    
    return date


def show_per_plan_report_custom_date_range_menu(plan_number):
    start = get_start_date()
    end = get_end_date()

    get_selected_plans_topups_by_date_range(plan_number, start, end)


def show_general_report_date_range_selection_menu():
    print("Selection:")
    print("1. Last Month <- ready to test")
    print("2. Custom <- ready to test")
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
        today = datetime.now()
        prev_month = today.month - 1  # What happens if today is January??
        prev_monthrange = calendar.monthrange(today.year, prev_month)
        start = datetime(today.year, prev_month, 1)
        end = datetime(today.year, prev_month, prev_monthrange[1])

        get_all_topups_by_date_range(start, end)

    elif selection == 2:
        show_general_report_custom_date_range_menu()

    elif selection == 3:
        print("Exit")


def show_general_report_custom_date_range_menu():
    start = get_start_date()
    end = get_end_date()

    get_all_topups_by_date_range(start, end)