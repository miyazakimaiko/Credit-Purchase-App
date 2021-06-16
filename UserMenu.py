def mainMenu():
    print("Select an option")
    print("1. View balance") #just here for the purpose of menu
    print("3. Top Up") 
    print("4. Change mobile plan")
    print("5. Reports")
    print("6. Exit")

    #loop 
    while True:
        try:
            selection = int(input())
            if selection ==1:
                account_balance()
            elif selection ==2:
                top_up()
                break     #breaks the loop to stop continuously looping
            elif selection ==3:
                change_plan()
                break
            elif selection ==4:
                change_plan()
                break
            elif selection ==5:
                reports()
                break
            elif selection ==6:
                exit()
                break
            else:
                print("Invalid option , please select from 1-6")
                #calls on main menu again to get use input
                mainMenu()
        except ValueError:
            print("Invalid input , please choose from option 1-6")


#functions to be called on through user input     
def account_balance():
    print("")

def top_up():
    print("Please select your top up option below")
    print("1. £5")
    print("2. £10")
    print("3. £15")
    print("4. £20")
    print("5. £25")
    print("6. Return to main menu") #will call on mainMenu function
    print("7. Exit") #will close the app

    while True:
        try:
            choice = int(input())
            if choice ==1:
                print("You have topped up with £5")
                break
            elif choice == 2:
                print("You have topped up with £10")
                break
            elif choice == 3:
                print("You have topped up with £15")
                break
            elif choice ==4:
                print("You have topped up with £20")
                break
            elif choice ==5:
                print("You have topped up with £25")
                break
            elif choice ==6:
                mainMenu()  #take user back to main menu
                break
            elif choice ==7:
                exit()
            else:
                print("Invalid option , please select from 1-7")
                top_up() #calls on top up menu as user input is invalid
        
        except ValueError:
            print("Invalid input , please choose from option 1-7")

   

def change_plan():
    print("Please select a plan below")
    print("1. Prepay")
    print("2. Bill pay")
    print("3. Sim-only")
    print("4. Return to main menu")
    print("5. Exit")

    while True:
        try:
            choice2 = int(input())

            if choice2 ==1:
                print("You have switched over to pre pay")
                break
            elif choice2 ==2:
                print("You have switched over to bill pay")
                break
            elif choice2 ==3:
                print("You have switched over to a sim-only plan")
                break
            elif choice2 ==4:
                mainMenu() #returns to main menu
                break
            elif choice2 ==5:
                exit() #closes app
            else:
                print("Invalid option , please select from 1-5")
                change_plan()

        except ValueError:
            print("Invalid input , please choose from option 1-5")


def reports():
    print("Please select an option below")
    print("1. Top Up History")
    print("2. Mobile Plan History")
    print("3. Return to main menu")
    print("4. Exit")

    while True:
        try:
            choice3 = int(input())

            if choice3 ==1:
                print("This is your top up history") #placeholder for text file that can show user top up history
                break
            elif choice3 ==2:
                print("This is your mobile plan history") # like the above another placeholder
                break
            elif choice3 ==3:
                mainMenu()  #take uer back to main menu
                break
            elif choice3 ==4:
                exit()
            else:
                 print("Invalid option , please select from 1-4")
                 reports()

        except ValueError:
            print("Invalid input , please choose from option 1-5")
    
    
#function called upon to close app
def exit():
    exit
       


#runs main menu 
mainMenu()