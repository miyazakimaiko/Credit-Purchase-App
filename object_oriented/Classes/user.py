class User:

    def __init__(self, phone_number, first_name, last_name, email_address, password, plan, current_balance, topup_history=[]):
        self._phone_number = phone_number
        self._first_name = first_name
        self._last_name = last_name
        self._email_address = email_address
        self._password = password
        self._plan = plan
        self._current_balance = current_balance
        self._topup_history = topup_history

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email_address(self):
        return self._email_address

    @property
    def password(self):
        return self._password

    @property
    def plan(self):
        return self._plan

    @property
    def current_balance(self):
        return self._current_balance

    @property
    def topup_history(self):
        return self._topup_history


    @phone_number.setter
    def phone_number(self, number):
        self._phone_number = number

    @first_name.setter
    def first_name(self, fname):
        self._first_name = fname

    @last_name.setter
    def last_name(self, lname):
        self._last_name = lname

    @email_address.setter
    def email_address(self, email):
        self._email_address = email

    @password.setter
    def password(self, pwd):
        self._password = pwd

    @plan.setter
    def plan(self, number):
        self._plan = number

    @current_balance.setter
    def add_balance(self, amount):
        self._current_balance += amount

    @topup_history.setter
    def add_topup(self, topup):
        self._topup_history.append(topup)

    def __repr__(self):
        return f"({self._phone_number}, {self._first_name}, {self._last_name}, {self._email_address}, {self._plan}, {self._current_balance}, {self._topup_history})"

    






