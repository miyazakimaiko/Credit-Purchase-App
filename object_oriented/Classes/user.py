class User:

    def __init__(self, phone_number, first_name, last_name, email_address, password, plan, current_balance):
        self._phone_number = phone_number
        self._first_name = first_name
        self._last_name = last_name
        self._email_address = email_address
        self._password = password
        self._plan = plan
        self._current_balance = current_balance

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, number):
        self._phone_number = number

    def __repr__(self):
        return f"({self._phone_number}, {self._first_name}, {self._last_name}, {self._email_address}, {self._plan}, {self._current_balance})"

    






