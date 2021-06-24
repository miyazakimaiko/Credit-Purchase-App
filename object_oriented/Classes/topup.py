class Topup:

    def __init__(self, phone_number, amount, plan, topup_date):
        self.phone_number = phone_number
        self.amount = amount
        self.plan = plan
        self.topup_date = topup_date

    def __repr__(self):
        return f"({self.phone_number}, {self.amount}, {self.plan}, {self.topup_date})"