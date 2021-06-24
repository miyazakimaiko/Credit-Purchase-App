class User:

    def __init__(self, phone_number, first_name, last_name, email_address, password, plan, current_balance):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.password = password
        self.plan = plan
        self.current_balance = current_balance

    def __repr__(self):
        return f"({self.phone_number}, {self.first_name}, {self.last_name}, {self.email_address}, {self.plan}, {self.current_balance})"

    






