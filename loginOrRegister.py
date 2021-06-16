import os


def loginOrRegisterMenu():
    print("Menu Options - Login or Register")
    print("1. Login - customer")
    print("2. Login - admin")
    print("3. Register")
    print("4. Exit Application")


def Register():
    phoneNumber = input("Phone Number:")
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    password = input("Password: ")
    #plan menu

    #adds data to useres.txt file to be stored
    file = open("users.txt", "a")
    file.write(phoneNumber)
    file.write(",")
    file.write(firstName)
    file.write(",")
    file.write(lastName)
    file.write(",")
    file.write(password)
    file.write("\n")
    file.close()
    print("Account Registered")
    
userType = "0"
while(userType != "4"):
    loginOrRegisterMenu()
    userType = input("Please choose option (1-4): ")
    if(userType == "1"):
        print("You have selected 'Login - customer'")
        #LoginCustomer()
    elif(userType == "2"):
        print("You have selected 'Login - admin'")
        #LoginAdmin()
    elif(userType == "3"):
        print("You have selected 'Register'")
        Register()
    elif(userType !="1" and userType != "2" and userType != "3" and userType != "4"):
        print("Invalid Choice - try again")

print("Application Closed")


