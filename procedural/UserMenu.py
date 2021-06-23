def mainMenu():
    print("Select an option")
    print("1. View balance") #just here for the purpose of menu
    print("2. Top Up") 
    print("3. Change mobile plan")
    print("4. Reports")
    print("5. Exit")

    #loop 
    while True:
        try:
            selection = int(input())
            if selection ==1:
                account_balance()
            elif selection ==2:
                toppingUp()
                break     #breaks the loop to stop continuously looping
            elif selection ==3:
                change_plan() #decided to go with user card details first before choosing amount
                break
            elif selection ==4:
                reports()
                break
            elif selection ==5:
                exit()
                break
            else:
                print("Invalid option , please select from 1-5")
                #calls on main menu again to get use input
                mainMenu()
        except ValueError:
            print("Invalid input , please choose from option 1-5")


#functions to be called on through user input     
def account_balance():
    print("")

def top_up_amount():
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
                top_up_amount() #calls on top up menu as user input is invalid
        
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
       
#top up history 
def topUpHistory():
    print("read from text file") #still need to implement

#user entering and validating card details for to up
def toppingUp():
    #print("please enter your 16 didgit card number ") this is redundant
    while True:
        card_number = input("Please enter your 16 digit card number: ")
        if not card_number.isdigit(): # check if a string contains a number with .isdigit()
            print("Enter only numbers\n")
            continue
        elif len(card_number) != 16:
            print ("Enter your 16 digit card number \n")
            continue
        else:
            break
    #once above is validated the user goes to the next step
    print("Please enter you expiry date in form MMYY (e.g. 0121) ")
    while True:
        expiry_date = input("Enter expiry date here ")
        if not expiry_date.isdigit(): #validates the user input is in digit form
            print("Enter numbers only \n") #if not prompts the user to try again
            continue #continuous loop till user is validated
        elif len (expiry_date) != 4: #user must input 4 digits
            print("Please enter a 4 digit expiry number ")
            continue
        else:
            break
    #once above is validated the user goes to the next step
    print("Please enter your 3 digit CVC (appears behind your card ")
    while True:
        cvc_number = input("Enter CVC here ")
        if not cvc_number .isdigit():
            print("Enter numbers only \n")
            continue
        elif len (cvc_number) != 3:
            print("Please enter a 3 digit CVC ")
            continue
        else:
            break
    #once all card details validated the user can choose top up amount
    print(top_up_amount()) #calls on fun for user to pick a top up amount


        
    
        
        
   
       
#runs main menu 
# mainMenu()