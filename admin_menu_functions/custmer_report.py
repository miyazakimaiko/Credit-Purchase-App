#===============================================================================================
# REQUIREMENTS
# 
# 1. Reports per User specified by Phone Number
#   - Two Options: (A)Last Month (B)Date Range
# 
#   After selection - Reports display all customer's details (name, plan, phone number), 
#   top-ups with dates, current balance
# 
#   Does it start from a search function or a list of customers? \
#   The search is by phone number. The system will prompt for this input (Please, enter the phone number)
#===============================================================================================



def get_all_customers():


    # read txt file and create a list of customers here
    customers = []

    customer1 = {"phoneNumber": 123456, "firstName": "aaaa", "lastName": "bbbbbb", "email": "myzkmik@gmail.com", "password": "skdmfbir33", "plan": 1, "current balance": 100}
    customer2 = {"phoneNumber": 163455, "firstName": "bbbb", "lastName": "dddddd", "email": "myzkmik@gmail.com", "password": "skdmfbir33", "plan": 2, "current balance": 100}
    customer3 = {"phoneNumber": 245456, "firstName": "cccc", "lastName": "eeeeee", "email": "myzkmik@gmail.com", "password": "skdmfbir33", "plan": 3, "current balance": 100}

    customers.append(customer1)
    customers.append(customer2)
    customers.append(customer3)

    for dic in customers:
        print(dic)

    print("Total Number of Customers: ", len(customers))

# Test
# get_all_customers()