class Admin:

    # Do we want to generate employee_number automatically
    # when creating objects...like this?
    employee_number = 1

    def __init__(self, password): #SEE IF WE WILL INCLUDE USERNAME??
        self.employee_number = Admin.employee_number
        self.password = password

        # Increment employee number for the next object that will be created
        Admin.employee_number += 1

    def __repr__(self):
        return f"({self.employee_number}, {self.password})"