from Classes.user import User


user_list = []

def add_users(): #TODO: include current_balance

    user_list.append(User("0871112345", "Emma", "Brown", "emma@brown.ie", "qwerty", 3, 100.00))
    #user_list.append(User("089940", "firstName":"Emma", "lastName":"Brown", "email":"emma@brown.ie", "password":"qwerty", "plan":"3"})
    #user_list.append({"phoneNumber": "0861234567", "firstName":"Esther", "lastName":"Smith", "email":"esther@smyth.ie", "password":"123123123", "plan":"1"})
    #user_list.append({"phoneNumber": "0851231234", "firstName":"Maiko", "lastName":"Watson", "email":"maiko@watson.com", "password":"yuiop12345", "plan":"2"})

    

admin_list = []


def add_admin():
    admin_list.append({"username":"managerTom", "employeeNumber":"1234", "password":"manager1"})
    admin_list.append({"username":"managerBrian", "employeeNumber":"4321", "password":"manager2"})
    
topup_list = []

def add_topups():
    topup_list.append()



add_users()

print(user_list)