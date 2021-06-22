# ===============================================================================
# REQUIREMENTS
# 
# Selection 3. General Plan Report - Two Options: (A)Last Month (B)Date Range 
# - Display all top-ups - Display "Total:" 
# ===============================================================================


from datetime import datetime

# only accept start and end date format -- dd/mm/yyyy

def get_all_topups_by_date_range(start_date, end_date):

    # with text file read it and create a list of topups here..
    all_topups = []

    all_topups.append({"phone_number": "123456", "charged": 30, "plan": 3, "date": "08/01/2021"})
    all_topups.append({"phone_number": "123456", "charged": 40, "plan": 1, "date": "12/01/2021"})
    all_topups.append({"phone_number": "123456", "charged": 50, "plan": 1, "date": "15/01/2021"})
    all_topups.append({"phone_number": "343848", "charged": 60, "plan": 2, "date": "18/01/2021"})
    all_topups.append({"phone_number": "123456", "charged": 20, "plan": 1, "date": "01/02/2021"})
    all_topups.append({"phone_number": "343848", "charged": 30, "plan": 2, "date": "04/02/2021"})
    all_topups.append({"phone_number": "123456", "charged": 40, "plan": 3, "date": "08/02/2021"})
    all_topups.append({"phone_number": "123456", "charged": 50, "plan": 1, "date": "12/02/2021"})
    all_topups.append({"phone_number": "123456", "charged": 60, "plan": 1, "date": "15/02/2021"})
    all_topups.append({"phone_number": "343848", "charged": 20, "plan": 2, "date": "18/02/2021"})
    all_topups.append({"phone_number": "123456", "charged": 20, "plan": 3, "date": "22/02/2021"})
    all_topups.append({"phone_number": "123456", "charged": 30, "plan": 1, "date": "25/02/2021"})
    all_topups.append({"phone_number": "123456", "charged": 40, "plan": 1, "date": "01/03/2021"})
    all_topups.append({"phone_number": "343848", "charged": 50, "plan": 2, "date": "04/03/2021"})
    all_topups.append({"phone_number": "123456", "charged": 60, "plan": 3, "date": "08/03/2021"})
    all_topups.append({"phone_number": "123456", "charged": 70, "plan": 1, "date": "12/03/2021"})
    all_topups.append({"phone_number": "123456", "charged": 20, "plan": 1, "date": "15/03/2021"})
    all_topups.append({"phone_number": "343848", "charged": 20, "plan": 2, "date": "18/03/2021"})
    all_topups.append({"phone_number": "123456", "charged": 30, "plan": 3, "date": "22/03/2021"})
    all_topups.append({"phone_number": "123456", "charged": 40, "plan": 1, "date": "25/03/2021"})
    all_topups.append({"phone_number": "123456", "charged": 30, "plan": 1, "date": "01/04/2021"})
    all_topups.append({"phone_number": "343848", "charged": 20, "plan": 2, "date": "04/04/2021"})
    all_topups.append({"phone_number": "123456", "charged": 20, "plan": 3, "date": "08/04/2021"})
    all_topups.append({"phone_number": "123456", "charged": 20, "plan": 1, "date": "12/04/2021"})
    all_topups.append({"phone_number": "123456", "charged": 20, "plan": 1, "date": "15/04/2021"})
    all_topups.append({"phone_number": "343848", "charged": 20, "plan": 2, "date": "18/04/2021"})
    all_topups.append({"phone_number": "123456", "charged": 40, "plan": 3, "date": "22/04/2021"})
    all_topups.append({"phone_number": "123456", "charged": 20, "plan": 1, "date": "25/04/2021"})
    all_topups.append({"phone_number": "123456", "charged": 20, "plan": 1, "date": "01/05/2021"})
    all_topups.append({"phone_number": "343848", "charged": 30, "plan": 2, "date": "02/05/2021"})
    all_topups.append({"phone_number": "123456", "charged": 30, "plan": 3, "date": "03/05/2021"})
    all_topups.append({"phone_number": "128656", "charged": 40, "plan": 1, "date": "06/05/2021"})
    all_topups.append({"phone_number": "123236", "charged": 50, "plan": 1, "date": "08/05/2021"})
    all_topups.append({"phone_number": "343848", "charged": 60, "plan": 2, "date": "10/05/2021"})
    all_topups.append({"phone_number": "343848", "charged": 30, "plan": 2, "date": "12/05/2021"})
    all_topups.append({"phone_number": "123456", "charged": 30, "plan": 3, "date": "15/05/2021"})
    all_topups.append({"phone_number": "666456", "charged": 40, "plan": 1, "date": "16/05/2021"})
    all_topups.append({"phone_number": "565456", "charged": 50, "plan": 1, "date": "18/05/2021"})
    all_topups.append({"phone_number": "343848", "charged": 60, "plan": 2, "date": "20/05/2021"})
    all_topups.append({"phone_number": "123456", "charged": 50, "plan": 3, "date": "22/05/2021"})
    all_topups.append({"phone_number": "137456", "charged": 40, "plan": 1, "date": "25/05/2021"})
    all_topups.append({"phone_number": "123876", "charged": 30, "plan": 1, "date": "01/06/2021"})
    all_topups.append({"phone_number": "343848", "charged": 20, "plan": 2, "date": "04/06/2021"})
    all_topups.append({"phone_number": "123456", "charged": 20, "plan": 3, "date": "08/06/2021"})
    all_topups.append({"phone_number": "123346", "charged": 20, "plan": 1, "date": "12/06/2021"})
    all_topups.append({"phone_number": "122346", "charged": 30, "plan": 1, "date": "15/06/2021"})
    all_topups.append({"phone_number": "343848", "charged": 20, "plan": 2, "date": "18/06/2021"})

    # demo data end

    print("\n")
    print("=================")
    print("Result")
    print("\n")
    print("Start Date: ", start_date)
    print("End Date: ", end_date)

    # Header of the topup history table
    print("\n")
    print("Phone Number".ljust(15) + "Charged".ljust(10) + "Plan".ljust(10) + "Date")
    print("----------------------------------------------")

    total_charge = 0

    for topup in all_topups:
        topup_date = datetime.strptime(topup["date"], "%d/%m/%Y")

        if start_date <= topup_date and end_date >= topup_date:
            total_charge += topup["charged"]
            print(f"{topup['phone_number'].ljust(15)}\
                {str(topup['charged']).ljust(10)}\
                {str(topup['plan']).ljust(10)}\
                {topup['date']}")

    print("\nTotal Charge: ", total_charge, "\n")