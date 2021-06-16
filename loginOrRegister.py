import os

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
    print("LOGIN")
    print("=====")
    
    username = input("Please enter phone number")
    password = input("Please enter password")

    #accessing items from userList
    userPhoneNumber = userList["phoneNumber"]
    userPassword = userList["password"]

    if(username == userPhoneNumber and password == userPassword ):
        print("Login Successful")
        #plans code / function
    elif(username != userPhoneNumber):
        print("Invalid Username")
    elif(password != userPassword):
        print("Invalid Password")
     


def Register():
    print()
   #import Anna registration function
    
userType = "0"
while(userType != "4"):
    loginOrRegisterMenu()
    userType = input("Please choose option (1-4): ")
    if(userType == "1"):
        print("You have selected 'Login - customer'")
        LoginCustomer()
    elif(userType == "2"):
        print("You have selected 'Login - admin'")
        #LoginAdmin()
    elif(userType == "3"):
        print("You have selected 'Register'")
        Register()
    elif(userType !="1" and userType != "2" and userType != "3" and userType != "4"):
        print("Invalid Choice - try again")

print("Application Closed")


