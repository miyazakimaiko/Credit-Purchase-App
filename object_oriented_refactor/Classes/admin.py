class Admin:

    # Do we want to generate employee_number automatically
    # when creating objects...like this?
    next_employee_id = 1

    def __init__(self, employee_number, password): #SEE IF WE WILL INCLUDE USERNAME??
        self.employee_id = Admin.next_employee_id
        self.employee_number = employee_number
        self.password = password

        # Increment employee number for the next object that will be created
        Admin.next_employee_id += 1

    def __repr__(self):
        return f"({self.employee_id} {self.employee_number}, {self.password})"