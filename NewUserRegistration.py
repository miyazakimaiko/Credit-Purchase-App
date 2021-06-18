import os
def ValidatePhoneNumber(UserPhoneNumber):
    isnumeric = UserPhoneNumber.isnumeric()
    islengthcorrect=len(UserPhoneNumber)
    status = isnumeric and (islengthcorrect==10)
    if status==False:
         print("Sorry, invalid phone number. Please enter correct number in digital format (10 digits) ")
    return status

# if the customer already registered with the phone number provided, the registration is impossib;e and should be cancelled
def CheckPhoneNumber(UserPhoneNumber):
    Found=False
    fo = open("userdetails.txt", "r")
    for x in fo:
        index = x.find(";")
        if (index<0):
            continue
        if (UserPhoneNumber == x[0:index]):
            Found=True
            print("Sorry, the user with phone number "+UserPhoneNumber +" already registered, registration cancelled ")
            break   
    fo.close()  
    return Found
    

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
    user = None


    while(selection != "2"):
        selection = showMenu()
        clearScreen()
    
        if(selection == "1"):
            PhoneNumber = input("Please enter your Phone Number!\n")
            if (ValidatePhoneNumber(PhoneNumber)==False):
                break
            else:
                if (CheckPhoneNumber(PhoneNumber)==True):
                    break
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
            # if ((planselection=="1") or(planselection=="2")or (planselection=="3")):
            if planselection in("1","2","3"):
                user = {"PhoneNumber":PhoneNumber, "FirstName": FirstName, "LastName": LastName, "Email": Email, "Password": Password,
                "Plan": planselection}
                print("Thank you!You are registered, now you can log in using your phone number and password")
            elif(planselection!= "4"):
                print("Please return to menu and select a digit from 1 to 4")
                input("Return to continue...")
        elif(selection != "2"):
            print("Please return to menu and select a digit from 1 to 2")
            input("Return to continue...")

# if users data has been added to the dictionary, we write it down to the file userdetails.txt 
    if (user!=None):
        fo = open("userdetails.txt", "a")
        fo.write(str(user['PhoneNumber'])+ ";"+ str(user['FirstName'])+ ";"+ str(user['LastName'])+ 
        ";"+ str(user['Email'])+";"+ str(user['Password'])+";"+str(user['Plan']) +"\n")
        fo.close()

NewCustomerRegistration()


