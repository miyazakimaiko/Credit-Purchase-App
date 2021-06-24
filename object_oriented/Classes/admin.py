class Admin:

    def __init__(self, employee_number, password): #SEE IF WE WILL INCLUDE USERNAME??
        self.employee_number = employee_number
        self.password = password

    def __repr__(self):
        return f"({self.employee_number}, {self.password})"