def get_all_customers():

    # read txt file and create a list of customers here
    customers = []

    customer1 = {"phoneNumber": 123456, "firstName": "aaaa", "lastName": "bbbbbb", "email": "myzkmik@gmail.com", "password": "skdmfbir33", "plan": 1, "current balance": 100}
    customer2 = {"PhoneNumber": 124556, "FirstName": "cccc", "LastName": "ddddd", "Email": "myzkmik@gmail.com", "Password": "skdmfbir33", "Plan": 2, "current balance": 100}
    customer3 = {"PhoneNumber": 135656, "FirstName": "eeee", "LastName": "ffffff", "Email": "myzkmik@gmail.com", "Password": "skdmfbir33", "Plan": 3, "current balance": 100}

    customers.append(customer1)
    customers.append(customer2)
    customers.append(customer3)

    for dic in customers:
        print(dic)

    print("Total Number of Customers: ", len(customers))

# Test
get_all_customers()