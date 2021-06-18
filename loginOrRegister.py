
import os
import NewUserRegistration
import admin_menu
import UserMenu




userList = []
userList.append({"phoneNumber": "0876621111", "firstName":"Anna", "lastName":"Tim", "email":"anna123@gmail.com", "password":"123456", "plan":"2"})
userList.append({"phoneNumber": "0871112345", "firstName":"Emma", "lastName":"Brown", "email":"emma@brown.ie", "password":"qwerty", "plan":"3"})
userList.append({"phoneNumber": "0861234567", "firstName":"Esther", "lastName":"Smith", "email":"esther@smyth.ie", "password":"123123123", "plan":"1"})
userList.append({"phoneNumber": "0851231234", "firstName":"Maiko", "lastName":"Watson", "email":"maiko@watson.com", "password":"yuiop12345", "plan":"2"})

adminList = []
adminList.append({"username":"managerTom", "employeeNumber":"1234", "password":"manager1"})
adminList.append({"username":"managerBrian", "employeeNumber":"4321", "password":"manager2"})

    
def loginOrRegisterMenu():
    print("Menu Options - Login or Register")
    print("1. Login - customer")
    print("2. Login - admin")
    print("3. Register")
    print("4. Exit Application")

def LoginCustomer():
    print("CUSTOMER LOGIN")
    print("==============")

    username = input("Please enter phone number:  ")
    password = input("Please enter password:  ")

    #accessing items from userList
    userPhoneNumber = ""
    userPassword = ""
    foundUser = None

    for user in userList:
        if(user['phoneNumber'] == username):
            userPhoneNumber = user['phoneNumber']
            foundUser = user
            break

    if(foundUser != None):
        userPassword = foundUser['password']

    if(username == userPhoneNumber and password == userPassword):
            print("Login Successful")
            UserMenu.mainMenu()
        
    elif(username != userPhoneNumber and password != userPassword):
            print("Username & Password Invalid")
    elif(username != userPhoneNumber):
            print("Invalid Username")
    elif(password != userPassword):
            print("Invalid Password")
        
def LoginAdmin():
    print("ADMIN LOGIN")
    print("===========")

    aUsername = input("Please enter employee number:  ")  
    aPassword = input("Please enter password:  ") 

    #accessing items from admin list
    adminEmployeeNo = ""
    adminPassword = ""
    foundAdmin = 0

    for admin in adminList:
        if(admin['employeeNumber'] == aUsername):
            adminEmployeeNo = admin['employeeNumber']
            foundAdmin = admin
            break

    if foundAdmin != 0:
        adminPassword = foundAdmin['password']
    
    if(aUsername == adminEmployeeNo and aPassword == adminPassword):
            print("Login Successful")
            admin_menu.admin_main_menu()
    elif(aUsername != adminEmployeeNo and aPassword != adminPassword):
            print("Username and login invalid")
    elif(aUsername != adminEmployeeNo):
            print("Invalid Username")
    elif(aPassword != adminPassword):
            print("Invalid Password")

    
userType = "0"
while(userType != "4"):
    loginOrRegisterMenu()
    userType = input("Please choose option (1-4): ")
    if(userType == "1"):
        print("You have selected 'Login - customer'")
        LoginCustomer()
    elif(userType == "2"):
        print("You have selected 'Login - admin'")
        LoginAdmin()
    elif(userType == "3"):
        print("You have selected 'Register'")
        NewUserRegistration.NewCustomerRegistration()
    elif(userType !="1" and userType != "2" and userType != "3" and userType != "4"):
        print("Invalid Choice - try again")

print("Application Closed")


