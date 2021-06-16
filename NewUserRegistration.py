import os

def clearScreen():
    os.system('cls')


def showMenu():
        clearScreen()
        print("Welcome!Please follow instructions and provide details for your registration\n")
        print("New user registration:")
        print("1. Enter details")
        print("2. Exit\n")
        
        return input("Please choose an option (1-2): ")

def showPlanMenu():
        clearScreen()
        print("Please choose your mobile plan or press 4 to exit:")
        print("1. Pay As You Go (Can top up by any amount, no expiration)")
        print("2. Top-Up-20 Plan (Minimum top-up is 20, credit expires in 1 month")
        print("3. Premium Plan (Minimum top-up is 30, receive 5 euro free credit, expires in 1 month")   
        print("4. Exit\n")       
        return input("Please choose an option (1-4): ")


def NewCustomerRegistration():
    
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



    while(selection != "2"):
        selection = showMenu()
        clearScreen()
    #    print(f"selection = {selection}")
        if(selection == "1"):
            print("Please enter your Phone Number!\n")
            PhoneNumber = input()
            print("Please enter your First name!\n")
            FirstName = input()
            print("Please enter your Last name!\n")
            LastName = input()
            print("Please enter your Email!\n")
            Email = input()
            print("Please enter your Password!\n")
            Password = input()
            planselection = showPlanMenu()
            clearScreen()
            if ((planselection=="1") or(planselection=="2")or (planselection=="3")):
                    userdetails.append({"PhoneNumber":PhoneNumber, "FirstName": FirstName, "LastName": LastName, "Email": Email, "Password": Password,
                    "Plan": planselection})
                    print("Thank you!You are registered, now you can log in using your phone number and password")
            elif(planselection!= "4"):
                    print("Please return to menu and select a digit from 1 to 4")
                    input("Return to continue...")
        elif(selection != "2"):
            print("Please return to menu and select a digit from 1 to 2")
            input("Return to continue...")

# if users data has been added to the dictionary, we write it down to the file userdetails.txt 
    if (userdetails):
        fo = open("userdetails.txt", "w")
        for details in userdetails:
            fo.write(str(details['PhoneNumber'])+ ";"+ str(details['FirstName'])+ ";"+ str(details['LastName'])+ 
            ";"+ str(details['Email'])+";"+ str(details['Password'])+";"+str(details['Plan']) +"\n")
        fo.close()

NewCustomerRegistration()


