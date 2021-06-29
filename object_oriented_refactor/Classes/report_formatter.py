import datetime

class ReportFormatter:

    def show_selected_plans_topups_by_date_range(self, users, plan_number, start_date, end_date):

        print("\n")
        print("=================")
        print("Result")
        print("\n")
        print("Start Date: ", start_date.strftime("%d/%m/%Y"))
        print("End Date: ", end_date.strftime("%d/%m/%Y"))

        # Header of the topup history table
        print("\n")
        print("Phone Number".ljust(15) + "Charged".ljust(10) + "Plan".ljust(10) + "Date")
        print("----------------------------------------------")

        total_charge = 0

        for user in users:            
            for topup in user.topup_history:
                if topup.plan == plan_number:
                    if start_date <= topup.topup_date and end_date >= topup.topup_date:
                        total_charge += topup.amount
                        print(f"{user.phone_number.ljust(15)}\
                            {str(topup.amount).ljust(10)}\
                            {str(topup.plan).ljust(10)}\
                            {topup.topup_date}")

        print("\n")
        print("Total Charge: ", total_charge)
        print("\n")    