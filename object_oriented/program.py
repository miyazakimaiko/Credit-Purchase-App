from Classes.user import User
from Classes.admin import Admin
from Classes.topup import Topup


user_list = []

def add_users(): #TODO: include current_balance

    user_list.append(User("0871112345", "Emma", "Brown", "emma@brown.ie", "qwerty", 3, 100.00))
    user_list.append(User("0862173794", "Silpa", "Pravin", "silpa@brown.ie", "1234", 1, 200.00))
    user_list.append(User("0899409520", "Bruna", "Weber", "bruna@brown.ie", "5678", 2, 300.00))
    user_list.append(User("0834837641", "Maiko", "Miyazaki", "maiko@brown.ie", "1987", 3, 100.00))
    

admin_list = []


def add_admin():
    admin_list.append(Admin("0000", "manager0"))
    admin_list.append(Admin("1111", "manager1"))
    admin_list.append(Admin("2222", "manager2"))
    admin_list.append(Admin("3333", "manager3"))
    
topup_list = []

def add_topups():
    topup_list.append(Topup("0871112345", 30.00, 3, "01/01/2021"))



add_users()
add_admin()
add_topups()

# print(user_list)
# print(admin_list)
# print(topup_list)


# ====== test for setter -- Working :) ======
print(user_list[3])

# user_list[3].phone_number = "0000000"
# user_list[3].first_name = "mmmmmm"
# user_list[3].last_name = "yyyyy"
# user_list[3].email_address = "eeeeee"
# user_list[3].password = "pppppppp"
# user_list[3].plan = 1
# user_list[3].add_balance = 10
# user_list[3].add_topup = Topup("0871112345", 30.00, 3, "01/01/2021")

# Now it changed all the values
print(user_list[3])
# ====== test for setter -- Working :) ======